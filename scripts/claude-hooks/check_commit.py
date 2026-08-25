"""提交前审查检测器（PreToolUse 钩子调用）：判定事件是否为 git commit。

协议：exit 0 = 命中 git commit（需要门禁检查）；exit 1 = 放行。
判定为 token 序列级：git [flags] commit（flag 可带含空格的多 token 值）。

与旧 grep 子串匹配一致地覆盖"命令任意位置"——sudo/env 赋值前缀/wrapper
词（cmd/bash -c/$(...)）/字符串字面量里的 git commit 都会命中：门禁宁可
误拦（可用 CLAUDE_REVIEW_SKIP 绕过），不可漏拦；token 化避免 "git" 出现
在长词内（如 gitignore）的误判。子命令形态（git log --grep "git commit"）
因 log 不是 flag 而正确放行。

独立模块（非 heredoc）：可被 pytest 直接测试（tests/test_generic.py 矩阵）。
"""
import json
import re
import sys

raw = sys.argv[1] if len(sys.argv) > 1 else ""
try:
    ev = json.loads(raw)
except Exception:
    sys.exit(1)                     # 非 PreToolUse JSON：放行（不阻断）
tool = (ev.get("tool_use") or {}).get("name") or ev.get("name") or ""
if tool not in ("Bash", "PowerShell"):
    sys.exit(1)
cmd = ((ev.get("tool_use") or {}).get("input") or {}).get("command") or ""
toks = cmd.split()


def strip_q(t: str) -> str:
    return t.strip('"\'')


# 内联紧急绕过：命令前缀 CLAUDE_REVIEW_SKIP=1 git ...（token 级锚定首个
# token；提交信息/文档里出现该字样不在命令位置，不会被误判为绕过）
if toks:
    first = toks[0]
    if re.fullmatch(r"CLAUDE_REVIEW_SKIP=1;?", first) or \
       re.fullmatch(r"\$env:CLAUDE_REVIEW_SKIP\s*=\s*['\"]?1['\"]?;?", first):
        sys.exit(1)

for i, t in enumerate(toks):
    # 引号开头的 token 是字符串字面量（如 --grep "git commit"、printf 内容）：
    # 字面量里的 git 不是命令，跳过（无引号字面量如 echo 运行 git commit 教程
    # 仍命中——宁可误拦可绕过，不可漏拦）
    if t.startswith(('"', "'")):
        continue
    if strip_q(t) not in ("git", "git.exe"):
        continue
    j, expect_val = i + 1, False
    while j < len(toks):
        w = strip_q(toks[j])
        if w == "commit":
            sys.exit(0)             # git [flags] commit → 需要门禁检查
        if re.fullmatch(r"-[A-Za-z0-9-]+", w):
            expect_val = True       # flag（如 -m、-C、--no-pager）
        elif not expect_val or re.fullmatch(r"[;&|<>]*", w):
            break                   # 子命令/普通词，或值后的分隔符
        j += 1                      # flag 值（可多 token，含引号空格）
sys.exit(1)
