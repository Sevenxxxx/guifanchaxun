# 规范查询 Web POC（DSH Agent Runtime + guifan-chaxun skill）

从网页提问 → FastAPI → 官方 Python SDK（stdio JSON-RPC）→ `dsh --profile sdk`
子进程（完整 DSH Agent Runtime，自动发现 `guifan-chaxun` skill）→ agent 调用 skill/工具查规范 → 流式返回结果。

**安全默认**：DSH 运行时以 **read-only 只读沙箱**运行（写操作全部被拒、维护态失效），
服务端发放一次性会话令牌（刷新页面=新对话），带护栏提示词、限流与成本上限，含审计日志。

## 前置条件

- Windows 本机（云部署支持 Windows Server / Linux，见下），Python 3.12（`fastapi`/`uvicorn`/`sse-starlette`，见 `requirements.txt`）
- Node.js + DSH checkout（默认 `C:\Users\Seven\Desktop\deepseek-harness`，已构建）
- 本机 DSH 已配置过模型凭据（`~/.dsh/.credentials.yaml` 存在；云上用 `DEEPSEEK_API_KEY` 环境变量）
- `~/.agents/skills/guifan-chaxun`（本仓库 `tools/guifan-chaxun` 的 Junction）——skill 由 DSH
  运行时经 `skill-filesystem` 的 user-agents 根自动发现，无需任何额外配置

## 启动

```powershell
# 1. 一次性初始化(独立 DSH home + sdk profile 材质化 + 凭据复制)
powershell -ExecutionPolicy Bypass -File webapp\setup.ps1

# 2. 启动后端(仓库根目录执行;本机访问绑 127.0.0.1)
python -m webapp

# 3. 局域网/Tailscale/云上:用 start.ps1(绑 0.0.0.0)
powershell -ExecutionPolicy Bypass -File webapp\start.ps1

# 4. 浏览器打开 http://127.0.0.1:8090
```

验证问题示例：`JTG 5120-2021 对桥梁检查周期是怎么规定的？`
展开回复下方的"活动日志"，应能看到 agent 调用 `guifan-chaxun` skill 并执行
`spec.py list/toc/clause/grep/read` 等命令（经 pwsh 工具）。

命令行验收（不经浏览器）：

```powershell
python webapp\e2e_test.py "JTG 5120-2021 对桥梁检查周期是怎么规定的？"
# 多轮:复用上一条输出的 token 再问一句
python webapp\e2e_test.py "上一个问题的条文号是多少？" --token <上一条输出的 token>
# 护栏拒绝路径检查(422/400/429):
python webapp\api_guard_test.py --port 8090 --case badtoken
```

辅助脚本：`webapp/smoke_test.py`（SDK 直连冒烟）、`webapp/debug_session.py`（打印指定会话的
error/turn 事件，诊断用）。

## 配置（`webapp/config.py`，全部可用环境变量覆盖）

| 环境变量 | 默认 | 说明 |
|---|---|---|
| `DSH_CHECKOUT` | `C:\Users\Seven\Desktop\deepseek-harness` | 与 `dsh_launcher.cmd` 同步修改 |
| `DSH_HOME` | `webapp/dsh-home` | 独立 home；被污染时删除该目录重跑 setup |
| `GFC_MODEL` / `GFC_PROVIDER` | `deepseek-v4-flash` / `deepseek-official` | 模型路由 |
| `GFC_PORT` / `GFC_HOST` | `8090` / `127.0.0.1` | 监听地址（start.ps1 设 0.0.0.0） |
| `GFC_PERMISSION_MODE` | `read-only` | **只读沙箱（写保护，必选）** |
| `GFC_TELEMETRY_MODE` | `DISABLED` | 关闭会话遥测上传 |
| `GFC_MAX_TOKENS` | `32768` | 单轮输出封顶 |
| `GFC_TURN_TIMEOUT` | `1800` | 单轮超时（秒） |
| `GFC_MAX_MESSAGE_CHARS` | `8000` | 消息长度上限 |
| `GFC_MAX_TURNS` | `100` | 每会话轮数上限 |
| `GFC_RATE_GLOBAL` / `GFC_RATE_SESSION` | `120` / `30` | 限流（次/分） |
| `GFC_MAX_CONCURRENT` | `5` | **同时使用上限(人):超过直接拒绝 429,不排队** |
| `GFC_SESSION_TTL` / `GFC_SESSION_CAP` | `24` / `100` | 会话闲置过期(小时)/活跃上限 |
| `GFC_ACCESS_TOKEN` | 空（不启用） | 非空=启用访问口令；**优先用 `webapp/access.txt`（单密码，改即生效，无需重启）**；无文件才回退此环境变量 |
| `GFC_PASSWORD_FILE` | `webapp/access.txt` | 单密码文件路径；文件存在且非空=进入需输密码；换密码=改文件内容；删/清空=关闭 |

提示词护栏：`webapp/sdk-guardrail.patch.yml`（经 SDK `patches=` 注入，防注入+不输出凭据）。
审计日志：`webapp/logs/poc.log`。

## API

- `POST /api/session` → `{token}`：发放一次性对话令牌（每次打开页面调一次；旧令牌一律不认）
- `GET /api/health` → `{ok, runtime_started, last_error, model, permission_mode, active_sessions}`
- `GET /api/auth/status` → `{password_required}` —— 是否要求进入密码（前端据此弹密码框）；`password_required:true` 时未带对的 `X-Access-Token` 会被 `401` 拦
- `GET /api/status?session=<token>` → `{running, result?:{final_response, finish_reason}}` —— 查询某会话是否有一轮在跑;跑完返回该轮最终回复(供客户端断流/锁屏后补取,不重跑模型)
- `POST /api/chat` body `{token, message}` → **SSE 流**，事件：
  - `status` `{status: starting|running|idle}` —— 启动中/思考/结束
  - `text` `{text}` —— 当前 assistant 回复全文**替换**（流式增量渲染）
  - `activity` `{type, summary}` —— 工具/skill 调用等活动（`tool/result`、`tool/call`、`subagent.*`…）
  - `done` `{finish_reason, final_response}`
  - `session_reset` —— 服务端运行时重启导致会话失效（前端自动换新令牌重发）
  - `error` `{message}`
  - 心跳:空闲时每 `GFC_SSE_HEARTBEAT`(默认 15s)发一条注释行 `: ping`,防代理/网络掐断长连接。
- 错误码：`401` 口令错 / `400` 消息空或超长 / `422` 令牌无效 / `429` 容量满、限流、轮数上限、本会话忙

同一 token 即同一 DSH 会话：多轮上下文与历史由运行时 JSONL 持久化到
`webapp/dsh-home/sessions`；刷新页面=新会话（令牌仅存浏览器内存）。

## 架构

```
浏览器(static/index.html) --POST /api/session、/api/chat(SSE)--> FastAPI(webapp/main.py)
  webapp/dsh_service.py: DeepSeekHarness(Python SDK, sys.path 引入 checkout/python/sdk/src, 零安装)
  --stdio JSON-RPC--> dsh_launcher.cmd --> node <checkout>/apps/cli/lib/bin.js --profile sdk
  DSH_HOME=webapp/dsh-home + patches=sdk-guardrail.patch.yml
  --> DSH 运行时(88 插件: agent 循环 + 工具 + skill 注册表 + llm-deepseek;只读沙箱)
  --> skill-filesystem 发现 ~/.agents/skills/guifan-chaxun
  --> agent 经 pwsh 工具执行 spec.py --> 读 library_data 索引 --> 原文 --> 流式回传
```

## 云服务器部署（腾讯云轻量，Linux 推荐 / Windows Server 亦可）

**依赖清单（整包上传，不做激进瘦身）**：
- 项目文件：`webapp/`（代码+前端）、`guifansrc/`（约 4GB，文本书 read 依赖）、`library_data/`（约 138MB）
- DSH checkout：整包上传（约 2GB；含 `apps/cli/lib`、node_modules 闭包、`python/sdk/src`）
- 环境：Python 3.12 + Node.js LTS + `pip install fastapi uvicorn sse-starlette`
- skills：服务器建 `~/.agents/skills/guifan-chaxun`（复制 `tools/guifan-chaxun`）+ 兄弟 `guifan-chaxun-scripts`；`config.json` 指向服务器上的 `guifansrc`/`library_data`
- 凭据：**不随包上传、不在部署脚本中写入**；由服务器管理员自行设置 `DEEPSEEK_API_KEY` 环境变量（llm 适配器自动 env 回退）

**Linux 步骤**：
1. 新建 `dsh_launcher.sh`：`#!/usr/bin/env bash` + `exec node <绝对路径>/apps/cli/lib/bin.js "$@"`
2. `config.py` 的 `DSH_CHECKOUT`/`LAUNCHER` 指向服务器路径
3. setup（材质化 sdk profile，离线）→ 带全部 `GFC_*` 环境变量启动
4. 守护：systemd 单元（或 nohup）；开机自启
5. 安全组放行 TCP 8090（公网 + Tailscale）；可选 `GFC_ACCESS_TOKEN`

**Windows Server 步骤**：与本地几乎一致（launcher .cmd 路径改绝对），守护用任务计划/NSSM。
**完整照抄版**：见 `webapp/deploy-server-教学指南.md`（Windows Server 2022 部署手把手：
目录规划、依赖、skill 配置、DSH 路径环境变量、凭据、2G 内存 pagefile 调优、防火墙、任务计划开机自启、
进入密码、验证清单；服务器版初始化用 `webapp/setup_win_server.ps1`——不复制凭据文件）。

**维护策略**：OCR/索引在你的电脑上做，完成后增量上传 `library_data/` 覆盖即可（云上只跑查询态）。

## 已知限制（POC 刻意取舍）

- 单运行时进程、**多会话并行**：最多 `GFC_MAX_CONCURRENT`(默认 5)人同时提问并行执行；
  超过上限下一位请求直接返回 429"当前同时使用人数已达上限,请稍后再试"(不排队)。
- 会话令牌存后端内存：**Web 服务重启后所有令牌失效**（刷新页面即恢复）；DSH 会话历史仍在磁盘。
- SDK 协议无取消：客户端断开后轮次会继续跑完。
- 只读沙箱：写/维护操作（index/OCR）在服务端被拒（已实测：`file access denied under read-only mode`，
  提权无审批渠道 fail-closed）；维护在本地做。
- **读范围**：DSH 沙箱只管"写"，不限制"读"——agent 技术上可读工作区外文件；云上无个人数据 +
  护栏提示词（防注入、不输出凭据）为当前策略（选 A）。
- 公网 + 无鉴权 + web 工具启用：陌生人可用你的 key（成本已被限流/超时/轮数/token 封顶），
  建议启用 `GFC_ACCESS_TOKEN` 或安全组 IP 白名单。启用访问口令后，给同事一个带口令的入口：
  `http://<服务器>:8090/?token=<口令>`（也可用 `?access=`）。前端会把它作为 `X-Access-Token`
  头发给所有 API，并记入本地 localStorage；此后打开同源页面无需再带参数。

## 故障排查

- **setup 失败**：看 `webapp/dump-default-config.txt`；若 launcher 报模块错误，
  把 `dsh_launcher.cmd` 末行换成
  `node --import tsx/esm apps\cli\src\bin.ts %*`（checkout 根 `pnpm dsh` 同款调用）。
- **首问报 MISSING_CREDENTIAL**：本机查 `webapp/dsh-home/.credentials.yaml`；云上查 `DEEPSEEK_API_KEY`。
- **启动超时**：`GFC_INIT_TIMEOUT` 调大；`GET /api/health` 的 `last_error` 有 stderr 诊断。
- **审计**：`webapp/logs/poc.log` 记录会话创建/开始/结束/拒绝。
