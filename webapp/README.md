# 规范查询 Web POC（DSH Agent Runtime + guifan-chaxun skill）

最小可运行验证：从网页提问 → FastAPI → 官方 Python SDK（stdio JSON-RPC）→ `dsh --profile sdk`
子进程（完整 DSH Agent Runtime，自动发现 `guifan-chaxun` skill）→ agent 调用 skill/工具查规范 → 流式返回结果。

## 前置条件

- Windows 本机，Python 3.12（已装 `fastapi`/`uvicorn`/`sse-starlette`，见 `requirements.txt`）
- Node.js + DSH checkout（默认 `C:\Users\Seven\Desktop\deepseek-harness`，已构建）
- 本机 DSH 已配置过模型凭据（`~/.dsh/.credentials.yaml` 存在）
- `~/.agents/skills/guifan-chaxun`（本仓库 `tools/guifan-chaxun` 的 Junction）——skill 由 DSH
  运行时经 `skill-filesystem` 的 user-agents 根自动发现，无需任何额外配置

## 启动

```powershell
# 1. 一次性初始化(独立 DSH home + sdk profile 材质化 + 凭据复制)
powershell -ExecutionPolicy Bypass -File webapp\setup.ps1

# 2. 启动后端(仓库根目录执行)
python -m webapp

# 3. 浏览器打开
#    http://127.0.0.1:8090
```

## 局域网 / Tailscale 访问（让其他电脑用浏览器打开）

默认只绑本机 `127.0.0.1`。局域网或 Tailscale（tailnet）里的其他电脑要访问，两步：

1. **放行防火墙**（管理员 PowerShell 执行；只对 tailnet 与局域网 192.168.1.0/24 放行 8090）：
   ```powershell
   New-NetFirewallRule -DisplayName "DSH Web POC 8090" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8090 -Profile Any -RemoteAddress 100.64.0.0/10,192.168.1.0/24
   ```
2. **用 `webapp/start.ps1` 启动**（绑定 0.0.0.0）：
   ```powershell
   powershell -ExecutionPolicy Bypass -File webapp\start.ps1
   ```

其他电脑浏览器访问：
- Tailscale：`http://100.85.0.30:8090`
- 局域网：`http://192.168.1.9:8090`

安全提示：POC 无鉴权。`0.0.0.0` 绑定 = 任何能到达该端口的网络都能用；想收窄可用
`GFC_HOST` 只绑具体 IP（如 `100.85.0.30`），或把上面的 `RemoteAddress` 改小。

验证问题示例：`JTG 5120-2021 对桥梁检查周期是怎么规定的？`
展开回复下方的“活动日志”，应能看到 agent 调用 `guifan-chaxun` skill 并执行
`spec.py list/toc/clause/grep/read` 等命令（经 pwsh 工具）。

命令行验收（不经浏览器）：

```powershell
python webapp\e2e_test.py "JTG 5120-2021 对桥梁检查周期是怎么规定的？"
# 多轮:复用上一条输出的 session id 再问一句
python webapp\e2e_test.py "上一个问题的条文号是多少？" --session-id <id>
```

辅助脚本：`webapp/smoke_test.py`（SDK 直连冒烟）、`webapp/debug_session.py`（打印指定会话的
error/turn 事件，诊断用）。

## 配置（`webapp/config.py`）

| 项 | 默认 | 说明 |
|---|---|---|
| `DSH_CHECKOUT` | `C:\Users\Seven\Desktop\deepseek-harness` | 与 `dsh_launcher.cmd` 同步修改 |
| `DSH_HOME` | `webapp/dsh-home` | 独立 home；被污染时删除该目录重跑 setup |
| `GFC_MODEL` | `deepseek-v4-pro` | 环境变量可覆盖（provider/reasoning_effort 同理） |
| `GFC_PORT` | `8090` | 避开 DSH GUI 的 3080 |

## API

- `GET /api/health` → `{ok, runtime_started, last_error, model}`
- `POST /api/chat` body `{session_id, message}` → **SSE 流**，事件：
  - `status` `{status: queued|running|idle}` —— 排队/思考/结束
  - `text` `{text}` —— 当前 assistant 回复全文**替换**（流式增量渲染）
  - `activity` `{type, summary}` —— 工具/skill 调用等活动（`tool/result`、`tool/executing`、`subagent.*`…）
  - `done` `{finish_reason, final_response}`
  - `error` `{message}`（含 SDK 捕获的运行时 stderr 诊断）

同一 `session_id` 即同一 DSH 会话：多轮上下文与历史由运行时 JSONL 持久化到
`webapp/dsh-home/sessions`。

## 架构

```
浏览器(static/index.html) --POST /api/chat (SSE)--> FastAPI(webapp/main.py)
  webapp/dsh_service.py: DeepSeekHarness(Python SDK, sys.path 引入 checkout/python/sdk/src, 零安装)
  --stdio JSON-RPC--> dsh_launcher.cmd --> node <checkout>/apps/cli/lib/bin.js --profile sdk
  DSH_HOME=webapp/dsh-home --> DSH 运行时(dsh-base: 工具 + skill 注册表 + llm-deepseek)
  --> skill-filesystem 发现 ~/.agents/skills/guifan-chaxun
  --> agent 经 pwsh 工具执行 spec.py --> 读 library_data 索引 --> 原文 --> 流式回传
```

## 已知限制（POC 刻意取舍）

- 单运行时进程，轮次串行（第二问排队，页面显示“排队中”）；单用户、仅 localhost、无鉴权。
- **多轮会话在服务进程存活期内有效**：同一 `session_id` 的上下文与历史持久化到
  `webapp/dsh-home/sessions`（zstd JSONL）。后端重启后 DSH 运行时拒绝旧 id（磁盘日志碰撞，
  SDK 协议无冷恢复端点），页面会自动开新会话重发当前消息并提示；旧历史仍在磁盘上可查。
- SDK 协议无取消：客户端断开后轮次会继续跑完。
- 只做查询态；维护态（OCR/COM 转换）耗时且需写权限，不在 POC 验证范围。
- headless 下审批无交互通道；默认权限策略下读操作免审批。若遇审批卡住，
  在 `webapp/dsh-home/profiles/sdk/cordis.patch.yml` 固定 permission preset。

## 故障排查

- **setup 失败**：看 `webapp/dump-default-config.txt`；若 launcher 报模块错误，
  把 `dsh_launcher.cmd` 末行换成
  `node --import tsx/esm apps\cli\src\bin.ts %*`（checkout 根 `pnpm dsh` 同款调用）。
- **首问报 MISSING_CREDENTIAL**：`webapp/dsh-home/.credentials.yaml` 是否复制成功。
- **启动超时**：`GFC_INIT_TIMEOUT` 调大；`GET /api/health` 的 `last_error` 有 stderr 诊断。
