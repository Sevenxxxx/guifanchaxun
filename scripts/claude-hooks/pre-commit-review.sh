#!/usr/bin/env bash
# 提交前审查钩子(方案 B):拦截 Claude Code 会话内(Bash/PowerShell 工具)发起的
# git commit,强制先完成 /code-review --fix 并刷新审查标记 .claude/review-stamp。
#
# 两种模式:
#   --stamp  /code-review --fix 完成后刷新标记。标记内容 = 当前工作区状态哈希
#            (全部非忽略文件的工作区内容哈希 + 路径清单),与文件 mtime 无关——
#            Windows mtime 秒级粒度不可靠;哈希对 git add 也不敏感(staging 不改变
#            工作区内容,标记与提交时保持一致)
#   默认     钩子模式:stdin 为 PreToolUse 事件 JSON,仅拦截 git commit 命令
#
# 放行条件(任一满足即 exit 0):
#   1. 命令不是 git commit(token 级判定:git [flags] commit,flags 可带含空格的值)
#   2. CLAUDE_REVIEW_SKIP=1(紧急绕过:会话环境变量或命令内联前缀)
#   3. 工作区完全干净:无未跟踪非忽略文件、git diff 与暂存区均无改动
#      (如 --allow-empty 提交;注意未跟踪文件会让"git add -A && git commit"
#      这类复合命令落入标记检查,防绕过)
#   4. .claude/review-stamp 存在且内容 = 当前工作区哈希(审查后未再改动)
# 其余情况 exit 2 拦截,stderr 提示反馈给 Claude(防死循环的关键:标记文件即断环)
set -u

STAMP=".claude/review-stamp"

# 工作区状态哈希:文件集 = 索引 ∪ 未跟踪非忽略文件(staging 不变集),
# 内容 = 各文件工作区字节哈希 + 路径清单(同名换路径/删除也能检出)。
# 文件清单必须排序(LC_ALL=C 字节序)——ls-files 对未跟踪文件按文件系统序、
# 对已暂存文件按索引序列出,同一文件集在 add 前后行序不同,会破坏 staging 不变性。
# 哈希单次批量:hash-object --stdin-paths 的 autocrlf 过滤与逐文件 --path 一致
# (实测 CRLF 文件三值相同:批量/--path/索引哈希),避免每文件一个子进程
worktree_hash() {
  tmp_list="$(mktemp 2>/dev/null || echo /tmp/wt-hash.$$)"
  git ls-files --cached --others --exclude-standard -z 2>/dev/null | LC_ALL=C sort -z > "$tmp_list"
  {
    # 存在的文件:批量内容哈希(每行一个路径,含空格安全;autocrlf 过滤生效)。
    # 删除 → 哈希行少一行 → 摘要必变,无需显式 deleted 标记
    tr '\0' '\n' < "$tmp_list" \
      | while IFS= read -r f; do [ -f "$f" ] && printf '%s\n' "$f"; done \
      | git hash-object --stdin-paths 2>/dev/null
    # 原始路径流(NUL 字节进摘要;改名/增删路径 → 摘要必变)
    cat "$tmp_list"
  } | git hash-object --stdin
  rm -f "$tmp_list"
}

# ---- --stamp 模式:审查完成后刷新标记 ----
if [ "${1:-}" = "--stamp" ]; then
  root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "不在 git 仓库内,无法刷新审查标记" >&2
    exit 1
  }
  cd "$root" || { echo "无法进入仓库根目录 $root" >&2; exit 1; }
  mkdir -p "$root/.claude"
  h="$(worktree_hash)"
  printf '%s\n' "$h" > "$root/$STAMP"
  echo "审查标记已刷新(工作区哈希 ${h:0:8}…):$root/$STAMP" >&2
  exit 0
fi

# ---- 钩子模式:stdin 为 PreToolUse 事件 JSON ----
payload="$(cat)"

# 非 git 相关命令快速放行(python 启动 ~300ms 只在疑似 git 时付)。
# 小写化后匹配:PowerShell 命令大小写不敏感,GIT COMMIT 同样命中
pl="${payload,,}"
case "$pl" in
  *'git'*) ;;
  *) exit 0 ;;
esac
# 二级预过滤: 提交类命令必然含子命令名——git status/diff/log/add/push
# 等只读命令不再付 python 启动('am' 用词边界,防 JSON 字段名 "command" 误命中)。
# 注意: 子命令词表必须与 check_commit.py 的 COMMIT_SUBS 同步
if [[ "$pl" =~ (^|[^[:alpha:]])commit([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])merge([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])pull([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])cherry([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])revert([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])rebase([^[:alpha:]]|$) ]] \
   || [[ "$pl" =~ (^|[^[:alpha:]])am([^[:alpha:]]|$) ]]; then
  :
else
  exit 0
fi

# 紧急绕过:会话环境变量(内联前缀 CLAUDE_REVIEW_SKIP=1 git 由
# check_commit.py token 级识别——锚定命令首段,防提交信息误判)
if [ "${CLAUDE_REVIEW_SKIP:-}" = "1" ]; then
  exit 0
fi

# git commit 检测(独立模块,pytest 覆盖;协议:0=命中提交,1=明确非提交,
# 2=检测器异常)。附加检查只拦不放:异常也放行,但打印警告(门禁失效可见,
# 不能因检测器问题阻断会话内其他命令)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
printf '%s' "$payload" | python "$SCRIPT_DIR/check_commit.py" -
rc=$?
if [ "$rc" -eq 1 ]; then
  exit 0
fi
if [ "$rc" -ne 0 ]; then
  echo "⚠️ 提交审查检测器异常(rc=$rc),本次放行。请检查 check_commit.py/python 环境。" >&2
  exit 0
fi

# —— 已确认 git commit:干净工作区/审查标记检查 ——
root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "git rev-parse 失败,放行" >&2
  exit 0
}
cd "$root" || exit 0

# 工作区完全干净(含 --allow-empty 提交)→ 放行
if git diff --quiet 2>/dev/null && git diff --cached --quiet 2>/dev/null \
   && [ -z "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
  exit 0
fi

# 审查标记与当前工作区一致 → 已审查放行
if [ -f "$STAMP" ] && [ "$(cat "$STAMP")" = "$(worktree_hash)" ]; then
  exit 0
fi

cat >&2 <<'EOF'
⚠️ git commit 被提交前审查钩子拦截:当前改动尚未通过 /code-review --fix。
   请先运行 /code-review --fix,完成后刷新审查标记再提交:
     bash scripts/claude-hooks/pre-commit-review.sh --stamp
   紧急绕过(慎用):
     CLAUDE_REVIEW_SKIP=1 git commit ...
EOF
exit 2
