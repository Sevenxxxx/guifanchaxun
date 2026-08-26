"""提交前审查检测器（PreToolUse 钩子调用）：判定事件是否为 git commit。

协议：exit 0 = 命中 git commit（需要门禁检查）；exit 1 = 放行；exit 2 = 检测器异常（fail-closed 拦截）。
判定为 token 序列级：git [flags] commit（flag 可带含空格的多 token 值）。

覆盖原则（宁可误拦可 CLAUDE_REVIEW_SKIP 绕过，不可漏拦）：
- wrapper 形态：bash -c "git commit"、$(git commit)、`git commit`、/usr/bin/git commit、
  git commit; / git commit&&（尾随 shell 操作符）都会命中；
- token 化避免 "git" 出现在长词内（如 gitignore）的误判；
- 带值 flag（-C/-c/-m/--git-dir/--work-tree/--exec-path/--config）吞值；
  `--flag=value` 形式值在 token 内不吞；无值 flag（--no-pager 等）不吞后续子命令，
  因此 git log/diff/show 等只读命令不被误拦；
- 字符串字面量里的 "git commit"（如 --grep "git commit"）会命中（误拦可 SKIP 绕过）。

独立模块（非 heredoc）：可被 pytest 直接测试（tests/test_generic.py 矩阵）。
"""
import json
import re
import sys

# 带值 flag：吞掉下一个 token（--flag=value 形式值在 token 内，不吞）
VALUE_FLAGS = {"-C", "-c", "-m", "--git-dir", "--work-tree", "--exec-path", "--config"}


def norm(t):
    """token 归一化：去引号/反引号/$() 包裹/尾随 shell 操作符。"""
    t = t.strip('"\'`')
    if t.startswith('$('):
        t = t[2:]
    if t.endswith(')'):
        t = t[:-1]
    return t.rstrip(';&|<>')


def is_git(t):
    return t in ("git", "git.exe") or t.endswith(("/git", "\\git"))


def main():
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        ev = json.loads(raw)
    except Exception:
        # 非 PreToolUse JSON：此前 exit 1 被 hook 当"放行"，门禁被静默关闭——
        # 改为 fail-closed（exit 2 → hook 拦截并提示环境问题）
        sys.exit(2)
    tool = (ev.get("tool_use") or {}).get("name") or ev.get("name") or ""
    if tool not in ("Bash", "PowerShell"):
        sys.exit(1)
    cmd = ((ev.get("tool_use") or {}).get("input") or {}).get("command") or ""
    toks = cmd.split()

    # 内联紧急绕过（bash 与 PowerShell 两种拼写）：
    #   CLAUDE_REVIEW_SKIP=1 git ... / $env:CLAUDE_REVIEW_SKIP = 1; git ...
    if re.search(r"CLAUDE_REVIEW_SKIP\s*=\s*1", " ".join(toks[:4])):
        sys.exit(1)

    for i, t in enumerate(toks):
        if not is_git(norm(t)):
            continue
        j, expect_val = i + 1, False
        while j < len(toks):
            w = norm(toks[j])
            if w == "commit":
                sys.exit(0)             # git [flags] commit → 需要门禁检查
            m = re.fullmatch(r"(-[A-Za-z0-9-]+)(?:=(.*))?", w)
            if m:
                flag, inline_val = m.group(1), m.group(2)
                # 带 = 的 flag 值在 token 内；无 = 时仅已知带值 flag 吞下一个 token
                expect_val = flag in VALUE_FLAGS and inline_val is None
            elif not expect_val or re.fullmatch(r"[;&|<>]*", w):
                break                   # 子命令/普通词，或值后的分隔符
            j += 1                      # flag 值（可多 token，含引号空格）
    sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        sys.exit(2)                     # 检测器异常 → fail-closed 拦截
