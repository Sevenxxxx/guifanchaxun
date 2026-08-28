"""提交前审查检测器(PreToolUse 钩子调用):判定事件是否为 git 提交命令。

协议:exit 0 = 命中提交类命令(需要门禁检查);exit 1 = 明确非提交,放行;
exit 2 = 检测器异常(JSON 解析失败/python 环境问题),hook 侧放行但打印警告——
只拦不放,门禁是附加检查,不能因检测器问题阻断会话内其他命令。

判定为 token 序列级:git [flags] <subcommand>(flag 值可含空格/引号/多 token)。

覆盖原则(宁可误拦可 CLAUDE_REVIEW_SKIP 绕过,不可漏拦):
- 命令先按 shell 操作符拆段,引号内的操作符不拆(引号感知,`git -m "a|b" commit`
  `git -c "x=$(pwd)" commit` 不绕过);每段独立检测;
- wrapper 形态:bash -c "git commit"、$(git commit)、`git commit`、"$(git commit)"、
  全路径 C:\\...\\git.exe commit、git-commit 都会命中;
- token 化避免 "git" 出现在长词内(如 gitignore)的误判;PowerShell 大小写不敏感,
  GIT/COMMIT 大写形态同样命中;
- 带值 flag(-C/-c/-m/--git-dir/--work-tree/--exec-path/--config)吞值:
  值可多 token(引号未闭合则继续吞);--flag=value 形式值在 token 内不吞;
  无值 flag(--no-pager 等)不吞后续子命令,git log/diff/show 等只读命令不被误拦;
- 提交类子命令集合:{commit, merge, pull, cherry-pick, revert, rebase, am,
  commit-tree}(merge/pull 未必产生提交,保守拦截可 SKIP 绕过);
- 字符串字面量里的 "git commit"(如 --grep "git commit")会命中(误拦可 SKIP 绕过)。

紧急绕过 CLAUDE_REVIEW_SKIP=1:env 赋值必须出现在 git 提交段之前——
[env]? CLAUDE_REVIEW_SKIP=1 为段首(可后跟 git commit 同一段);提交信息里的
字符串("git commit -m \"CLAUDE_REVIEW_SKIP=1\"")、echo 输出不命中。

独立模块(非 heredoc):可被 pytest 直接测试。
"""
import json
import re
import sys

# 带值 flag:吞掉下一个 token(--flag=value 形式值在 token 内,不吞)
VALUE_FLAGS = {"-C", "-c", "-m", "--git-dir", "--work-tree", "--exec-path", "--config"}
# 产生提交的子命令(git 子命令),需门禁检查。注意:bash 预过滤(pre-commit-review.sh)
# 的子命令词表必须与此集合同步,新加子命令需两处更新
COMMIT_SUBS = {"commit", "merge", "pull", "cherry-pick", "revert", "rebase", "am",
               "commit-tree"}
# git 可执行文件 basename(全路径/带扩展名/包装器都命中;比较时转小写)
GIT_BASENAMES = {"git", "git.exe", "git.bat", "git.cmd", "git-commit"}
# shell 操作符(拆段用;引号内的不拆)
SHELL_OPS = set(';&|<>()')
# env 赋值前置词(紧邻 SKIP=1 之前时 SKIP 是赋值而非参数)
_ENV_WORDS = {"env", "/usr/bin/env", "set"}


def _split_segments(cmd):
    """按 shell 操作符拆段,引号(单/双/反引号)内的操作符不拆——
    防 `git -m "a|b" commit` / `git -c "x=$(pwd)" commit` 拆段绕过。"""
    segs, buf, quote = [], [], None
    for ch in cmd:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in '"\'`':
            quote = ch
            buf.append(ch)
        elif ch in SHELL_OPS:
            segs.append(''.join(buf))
            buf = []
        else:
            buf.append(ch)
    segs.append(''.join(buf))
    return segs


def norm(t):
    """token 归一化:先剥引号/反引号,再解 $() 包裹(`"$(git"` 形态必须
    先剥引号才能到 `$(`,顺序不可反)。拆段后 token 不含 shell 操作符。"""
    t = t.strip('"\'`')
    if t.startswith('$('):
        t = t[2:]
    if t.endswith(')'):
        t = t[:-1]
    return t


def git_basename(t):
    return t.split("\\")[-1].split("/")[-1].lower()


def is_git(t):
    """按 basename 判断 git 可执行(全路径 C:\\...\\git.exe 也命中;
    PowerShell 大小写不敏感,GIT.EXE 同样命中)。"""
    return git_basename(t) in GIT_BASENAMES


def is_skip_assign(seg):
    """段首 env 赋值([env]? CLAUDE_REVIEW_SKIP=1 或 [env]? SKIP = 1 三段式)
    或引号内嵌命令开头(bash -c "CLAUDE_REVIEW_SKIP=1 git commit")
    才放行;提交信息里的字符串/echo 输出不命中。"""
    # 引号内嵌命令: 引号内容以 SKIP=1 开头且含 git(SKIP 覆盖了 git 提交)
    mq = re.search(r'["\'`]([^"\'`]*CLAUDE_REVIEW_SKIP\s*=\s*1[^"\'`]*git[^"\'`]*)["\'`]',
                   seg, re.IGNORECASE)
    if mq and mq.group(1).strip().startswith(('CLAUDE_REVIEW_SKIP', '$env:CLAUDE_REVIEW_SKIP')):
        return True
    toks = seg.split()
    if not toks:
        return False
    i = 0
    if toks[0].lower() in _ENV_WORDS:
        i = 1
    if i >= len(toks):
        return False
    w = toks[i].strip('"\'`')
    m = re.fullmatch(r"(?:\$env:)?CLAUDE_REVIEW_SKIP\s*=\s*(\S+)", w)
    if m:
        return m.group(1).strip('"\'') == "1"
    # 三段式赋值,容忍不对称空格(CLAUDE_REVIEW_SKIP =1 的 toks[1]='=1')
    if re.fullmatch(r"(?:\$env:)?CLAUDE_REVIEW_SKIP", w) and len(toks) >= i + 2 \
            and toks[i + 1].startswith("="):
        val = toks[i + 1][1:].strip('"\'')
        if not val and len(toks) >= i + 3:
            val = toks[i + 2].strip('"\'')
        return val == "1"
    return False


def detect_commit(seg):
    """单段内检测:git [flags] <提交子命令>。返回 True 需门禁检查。"""
    toks = seg.split()
    for i, t in enumerate(toks):
        tn = norm(t)
        if not is_git(tn):
            continue
        if git_basename(tn) == "git-commit":
            return True            # git-commit 包装器本身就是提交命令
        j, expect_val, parity = i + 1, False, 0
        while j < len(toks):
            w = norm(toks[j])
            if expect_val:
                # 吞一个值 token;引号跨 token 累计('"my'+'dir"' 合计 2 个为闭合)——
                # 未闭合 → 继续吞值;已闭合 → 下一 token 若是提交子命令则视为子命令
                # (`git -C dir commit` / `git -C "my dir" commit` 都命中;
                #  `git -C commit log` 中 commit 作值,放行)
                parity ^= (toks[j].count('"') + toks[j].count("'")) % 2
                closed = parity == 0
                j += 1
                if closed and j < len(toks) and norm(toks[j]).lower() in COMMIT_SUBS:
                    return True
                continue
            if w.lower() in COMMIT_SUBS:
                return True
            m = re.fullmatch(r"(-[A-Za-z0-9-]+)(?:=(.*))?", w)
            if m:
                flag, inline_val = m.group(1), m.group(2)
                expect_val = flag in VALUE_FLAGS and inline_val is None
                j += 1
                continue
            break                   # 非 flag 非子命令:不是提交命令
    return False


def main():
    # payload 经 stdin 传入(无 32KB 长度限制);argv 兼容旧调用方式
    raw = sys.argv[1] if (len(sys.argv) > 1 and sys.argv[1] != "-") else sys.stdin.read()
    try:
        ev = json.loads(raw)
    except Exception:
        return 2                    # 非 PreToolUse JSON:检测器异常 → hook 放行+警告
    tool = (ev.get("tool_use") or {}).get("name") or ev.get("name") or ""
    if tool not in ("Bash", "PowerShell"):
        return 1
    cmd = ((ev.get("tool_use") or {}).get("input") or {}).get("command") or ""
    segs = _split_segments(cmd)
    for idx, seg in enumerate(segs):
        # SKIP 紧急绕过:env 赋值段(前面无 git 提交段)才放行,提交信息不命中
        if is_skip_assign(seg) and not any(detect_commit(s) for s in segs[:idx]):
            return 1
    for seg in segs:
        if detect_commit(seg):
            return 0
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        sys.exit(2)                 # 检测器异常 → hook 放行+警告(只拦不放)
