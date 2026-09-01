# Windows Server 2022 部署手把手教学(guifan-chaxun Web POC)

> 目标:把你在本机验证好的「规范查询 Web POC」搬到一台腾讯云 Windows Server 2022(2核2G/50G)上,同事用浏览器打开就能问规范。
> 本文按 "**做什么 → 为什么 → 怎么做**" 讲清**每一步的意义**,方便你边做边学。照抄 + 理解即可;`<...>` 处为需替换内容。

---

## 0. 先看懂整套东西是怎么跑的(架构)

```
同事浏览器
   │  http://<服务器公网IP>:8090
   ▼
FastAPI  (webapp/main.py)          ← Web 入口,处理登录/限流/流式输出
   │  调 DSH Python SDK
   ▼
dsh --profile sdk 子进程           ← "Agent 大脑"(Cordis 插件运行时)
   │  调 guifan-chaxun skill
   ▼
spec.py  工具                     ← "翻书方法"(list/toc/clause/read/grep…)
   ▼ 读
guifansrc(规范 PDF 源) + library_data(索引:meta/toc/clauses/chapters…)
```

**各角色的意义**:
- **FastAPI 层** = 入口 + 门卫(会话令牌、限流、只读沙箱、并发上限、SSE 心跳、断流补结果)。同事只跟它打交道。
- **DSH 运行时** = agent 大脑,读 skill 的方法去"思考"该翻哪本书、调哪个工具。
- **spec.py** = 唯一程序,按"书架→目录→条文→原文"翻;查询态**纯文件读,零 LLM**,快且省。
- **guifansrc + library_data** = 知识库。`guifansrc` 是原始 PDF/文档;`library_data` 是**索引**(明文,可 grep/Read)。**骨架与 guifansrc 一一镜像**。

> 一句话:你把"知识库(index)+ 大脑(DSH)+ 入口(FastAPI)+ 方法(skill)"一起搬到云端,同事免安装直接用浏览器问。

---

## 1. 你要准备的 3 样东西

| # | 东西 | 说明 |
|---|---|---|
| 1 | 一台 Windows Server 2022(腾讯云,拿到**公网 IP** + 管理员密码) | 本文的部署目标 |
| 2 | 本机的 `guifanchaxun` 项目(已 clone 到 `C:\Users\Seven\Desktop\guifanchaxun`) | 含 `webapp/`、`tools/`、`library_data/`、`guifansrc/` |
| 3 | 本机的 `deepseek-harness` checkout(`C:\Users\Seven\Desktop\deepseek-harness`,约 2GB) | DSH 运行时本体,服务器要用 |

> **关键**:`guifansrc`(约 4GB)和 `library_data`(约 138MB)是**知识库**;`deepseek-harness` 是**大脑**。两者都要传,少一个就"有入口没知识"或"有知识没大脑"。

---

## 2. 上传文件到服务器的 `C:\poc\`(以及每个文件是干嘛的)

**为什么用 `C:\poc\`**:固定规划路径,脚本/配置里写死它,少踩路径不一致的坑;改路径要全局改,干脆固定。

**目标结构**:
```
C:\poc\
├── guifanchaxun\        ← 项目(webapp/ + guifansrc/ + library_data/)
│   ├── webapp\          ← Web 源码(setup_win_server.ps1 / start.ps1 / dsh_launcher.cmd / main.py)
│   ├── guifansrc\       ← 规范 PDF 源(4GB)
│   └── library_data\    ← 索引(138MB;bookshelf.json + 每书一个目录)
└── deepseek-harness\    ← DSH 运行时(2GB,含 node_modules,Windows→Windows 直接复制)
```

**每个目录/文件的角色**:
- `webapp\` : FastAPI 源码 + 启动/部署脚本。**同事访问的就是它**。
- `library_data\` : **知识库索引**。服务器上只读(查询用);更新在**你本机**做,改完增量上传这里。
- `guifansrc\` : 规范 PDF 源。**文字 PDF 书 `read`/`img` 会直接读它**(现场 fitz 提取页文本 / 渲染页图);OCR 书读 `library_data` 里的 `ocr/` 缓存、非 PDF 书读 `extracted/` 缓存,那些不读源。所以**服务器必须上传 guifansrc**,否则文字规范书一 `read` 就报"源文件缺失"。
- `deepseek-harness\` : DSH 运行时。**Node 依赖已含,Windows→Windows 无需重装**,直接复制即可。

**上传方式(按大小)推荐**:
- `webapp`(小)+ `library_data`(138MB):RDP 复制/共享文件夹/网盘均可。
- `deepseek-harness`(2GB):RDP 磁盘映射或 WinSCP;**直接复制,原生二进制兼容**。
- `guifansrc`(4GB,最大):推荐 **WinSCP(OpenSSH)断点续传** 或 **腾讯云 COS 中转**;RDP 拖拽很慢(可最后传)。

> 为什么 WinSCP 断点续传好:4GB 中途断网不会从头再来;RDP 拖拽对超大目录又慢又易中断。

---

## 3. 安装环境(在服务器上,管理员 PowerShell)

**步骤**:
```powershell
# 3.1 Python 3.12:官网 python.org 下载 Windows x64 安装包,勾选 "Add python.exe to PATH"
python --version          # 应显示 Python 3.12.x

# 3.2 装 Python 依赖(注意 pymupdf!):
#     fastapi/uvicorn/sse-starlette = webapp 网关心跳; pymupdf = spec.py 顶层 import fitz,查询态必装;
#     Pillow = 图片/视觉复核相关,保险。
python -m pip install fastapi uvicorn sse-starlette pymupdf Pillow

# 3.3 Node.js LTS:官网 nodejs.org 下载 msi 安装
node --version            # 应显示 v20+ 等 LTS
```

**为什么(pymupdf 关键)**:
- `spec.py` 第 34 行是模块级 `import fitz`(pymupdf)。**没装它,任何 spec.py 调用都直接 ImportError** → skill 完全不能用,连查询都做不了。
- runbook 旧版只写 `fastapi uvicorn sse-starlette`,**漏了 pymupdf**,这是个坑。已修正为 `... pymupdf Pillow`。
- `docx/openpyxl/pythoncom/tesseract` 只在**维护态**(你本机 index/OCR)用,服务器查询态用不到,不必装(装了也无妨)。
- **Node**:DSH 是 Node 写的,`dsh_launcher.cmd` 里是 `node apps\cli\lib\bin.js`。

---

## 4. 安装 skills 到服务器的用户目录(并改配置路径)

**为什么**:DSH 运行时从 `~/.agents/skills/` 发现 skill(不是仓库里的 `tools/`)。服务器上要把 `guifan-chaxun`(方法)+ `guifan-chaxun-scripts`(程序/配置)复制进去。

**怎么做**:
```powershell
# 4.1 建目录 + 复制
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
Copy-Item C:\poc\guifanchaxun\tools\guifan-chaxun        "$env:USERPROFILE\.agents\skills\" -Recurse
Copy-Item C:\poc\guifanchaxun\tools\guifan-chaxun-scripts "$env:USERPROFILE\.agents\skills\" -Recurse
```
**关键**:改名 `guifan-chaxun-scripts\config.json` 里两条路径,指向**服务器上**的库(换库唯一改动点):
```json
{
  "library_dir": "C:\\poc\\guifanchaxun\\guifansrc",
  "data_dir":    "C:\\poc\\guifanchaxun\\library_data",
  "...其余字段不动..."
}
```

**为什么**:`library_dir`/`data_dir` 就是知识库位置。服务器上这些路径必须换成 `C:\poc\...`,否则 skill 找不到书。

---

## 5. 改 webapp 的 2 处本地路径(必做,否则起不来)

**为什么**:`config.py` 和 `dsh_launcher.cmd` 里写死的是**本机** `C:\Users\Seven\Desktop\deepseek-harness`,服务器上没有这个路径,DSH 开不起来。

**怎么做**:
1. `C:\poc\guifanchaxun\webapp\config.py`:
   ```python
   DSH_CHECKOUT = Path(r"C:\poc\deepseek-harness")     # 改为服务器路径
   DSH_HOME     = WEBAPP_DIR / "dsh-home"             # 不变
   LAUNCHER     = WEBAPP_DIR / "dsh_launcher.cmd"     # 不变
   ```
2. `C:\poc\guifanchaxun\webapp\dsh_launcher.cmd`:
   ```cmd
   cd /d "C:\poc\deepseek-harness"
   node apps\cli\lib\bin.js %*
   ```

> 提示:两处要**保持一致**(注释也写着 `Keep checkout path in sync with DSH_CHECKOUT`)。

---

## 6. 设置 `DEEPSEEK_API_KEY` 环境变量(你自输,不落文件/脚本)

**为什么**:webapp 读 key 的顺序是「凭据文件 → 环境变量」。服务器上没有凭据文件,就用 Machine 级环境变量;**key 不进任何文件/脚本**,只进 Windows 环境变量。

**怎么做**:
```powershell
[Environment]::SetEnvironmentVariable('DEEPSEEK_API_KEY','sk-你的key','Machine')
# 设置后重启 PowerShell 会话才生效;验证(只显示存在,不看值):
[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY','Machine')
```

**为什么 Machine 级**:服务器开机、任何终端/服务都能读到,不依赖某个手动开的窗口。

---

## 7. 材质化 sdk profile(离线)

**为什么**:DSH 用 `--profile sdk` 组合配置(内置模板 `dsh-base`+`dsh-sdk-app`)。首次要在服务器上把它"实例化"到 `dsh-home`(离线,不联网),这样 runtime 才认。

**怎么做**:
```powershell
cd C:\poc\guifanchaxun
powershell -ExecutionPolicy Bypass -File webapp\setup_win_server.ps1
# 期望输出: OK: DSH_HOME = ... ; sdk profile materialized; ... (skill rows: N)
```

**脚本里做了什么**:建 `dsh-home`、用 `dsh_launcher.cmd --profile sdk --dump-default-config` 导出组合、检查 skill 行数。若失败,看 `webapp\dump-default-config.txt`。

---

## 8. 启动 + 验证

**怎么做**:
```powershell
# 8.1 前台启动,先验证
powershell -ExecutionPolicy Bypass -File webapp\start.ps1
# 8.2 另开一个 PowerShell 验证
Invoke-WebRequest http://127.0.0.1:8090/api/health -UseBasicParsing
# 期望: {"ok":true, "runtime_started":false, "model":"deepseek-official/deepseek-v4-flash", "permission_mode":"read-only", ...}
```

**说明**:
- `start.ps1` 会 **`Set-Location` 到仓库根**(任务计划无需设"起始于"),并设 `GFC_HOST=0.0.0.0`(这样才能局域网/公网访问)。
- `runtime_started:false` 是**正常**的:DSH 运行时是**首问才懒启动**。
- `permission_mode:"read-only"`:只读沙箱,防 agent 写文件。看健康接口返回这个字段就知道沙箱生效。
- 可以本机问一句(用 `e2e_test.py` 或浏览器 `http://127.0.0.1:8090`),确认首问成功、能正常流式回答。

**进入密码(可选,默认无)**:默认不需要密码。若要在 `webapp\access.txt` 写一个密码(如 `test1`),刷新页面即要求输入;换密码 = 改文件内容;删/清空 = 关闭。该文件已 gitignore(不提交真实密码),服务器上手动建(`Set-Content webapp\access.txt 'test1' -Encoding utf8`)。输错 401,前端自动重弹。

---

## 9. 防火墙放行 8090(服务器本地防火墙)

**为什么**:Windows 防火墙默认拦入站。要让同事(公网/Tailscale)能连 8090,必须放行。

**怎么做**:
```powershell
New-NetFirewallRule -DisplayName "DSH Web POC 8090" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8090 -Profile Any
```
**再加腾讯云安全组**:控制台 → 安全组/防火墙 → 放行 TCP 8090(来源 0.0.0.0/0 或限定网段)。

> 为什么两层都要:腾讯云安全组(云侧)+ Windows 防火墙(系统侧),**两层都得放行**,否则公网打不开(本机 OK、外部不通).

---

## 10. 内存调优(2核2G,并发 5 必做)

**为什么**:DSH+Node+FastAPI 同时在 2G 内存上跑,容易爆;Windows 默认 Pagefile 太小,并发 5 时可能因内存不足被系统杀掉进程。

**怎么做**:
1. 增大分页文件:`sysdm.cpl` → 高级 → 性能"设置" → 高级 → 虚拟内存"更改":取消"自动管理",C 盘**初始 4096 / 最大 8192 MB**,确定后重启。
   等效命令行:
   ```powershell
   wmic computersystem set AutomaticManagedPagefile=False
   wmic pagefileset create name="C:\pagefile.sys"
   # 再手动把 InitialSize/MaximumSize 设 4096/8192
   ```
2. 确认并发上限:`config.py` 的 `GFC_MAX_CONCURRENT` 默认 5。若上线后内存吃紧(`Get-Process` 看 node/python 内存、页面卡顿),**降到 3**(`$env:GFC_MAX_CONCURRENT='3'`,或改 config.py 默认)。

> 为什么并发 5 + 2G 要小心:每次并发都是一个 DSH 会话,5 个并发就是 5 份运行时上下文,2G 很紧张。宁可并发 3 也别让进程被系统 OOM 杀掉。

---

## 11. 任务计划开机自启

**为什么**:服务器重启后要自动拉起 webapp,不用人手动跑。

**怎么做**:
```powershell
schtasks /Create /F /TN "DSHWebPOC" /SC ONSTART /RU SYSTEM /RL HIGHEST `
  /TR "powershell -ExecutionPolicy Bypass -File C:\poc\guifanchaxun\webapp\start.ps1"
schtasks /Run /TN "DSHWebPOC"     # 立即跑一次验证
```

**说明**:`start.ps1` 内部已 `Set-Location` 仓库根,任务计划**无需设"起始于"**。重启后 1-2 分钟自动拉起;验证:`Invoke-WebRequest http://127.0.0.1:8090/api/health`。

---

## 12. 上线验证清单(每项打钩)

- [ ] 公网 `http://<公网IP>:8090` 打开页面;Tailscale `http://<服务器tailscale-ip>:8090` 也能开。
- [ ] 提问规范问题 → 正常流式回答(首问等几秒,DSH 懒启动)。
- [ ] 只读生效:让 agent 写文件被拒;问"更新索引"失败(维护态在服务器被禁止)。
- [ ] 刷新页面 = 新对话;两台设备同时问 → **并行**。
- [ ] 第 6 人同时提问 → 提示"当前同时使用人数已达上限(5 人)"。
- [ ] 断流/锁屏:回答中途锁屏 → 解锁后自动补结果(方案1,`/api/status`)。
- [ ] 进入密码(若启用 `access.txt`):未登录/密码错 → 401 弹密码框;输对才进。
- [ ] 审计日志 `webapp\logs\poc.log` 有记录。

---

## 13. 日常维护 / 故障排查 / 看日志

**维护策略**:OCR/索引在**你本机**做,完成后**只传 `library_data\`**(138MB)覆盖服务器同目录 → 生效(**云端只跑查询态**)。这避免在服务器上做沉重的 OCR/COM 转换,也符合只读沙箱。

**看日志**:
```powershell
# 审计日志(每次会话/轮次/拒绝都在这)
Get-Content C:\poc\guifanchaxun\webapp\logs\poc.log -Tail 50
# 启动日志(uvicorn/FastAPI 报错在这)
Get-Content C:\poc\guifanchaxun\webapp\logs\webapp_stderr.log -Tail 50
```

**常见故障**:
- 首问 `MISSING_CREDENTIAL` → `DEEPSEEK_API_KEY` 没生效:重启 PowerShell/服务器,`GetEnvironmentVariable(...,'Machine')` 确认;或确认第 6 步设置成功。
- setup 失败 → 看 `dump-default-config.txt`;确认 `dsh_launcher.cmd` 路径对、Node 已装。
- 公网打不开但本机 OK → 腾讯云安全组 **或** 服务器防火墙漏放行 8090。
- skill 一调用就 ImportError → **没装 pymupdf**(第 3.2 步没做)。
- 内存告急 → `GFC_MAX_CONCURRENT` 降 3、Pagefile 加大。

---

## 附:常用命令速查(服务器上)

```powershell
# 看是否在跑 + 端口
Get-NetTCPConnection -LocalPort 8090 -State Listen
Get-Process python,node | Select Id,ProcessName,@{n='MB';e={[math]::Round($_.WorkingSet64/1MB)}}
# 健康检查
Invoke-WebRequest http://127.0.0.1:8090/api/health -UseBasicParsing
# 重启(旧进程被杀后重新拉起)
taskkill /PID <pid> /T /F
powershell -ExecutionPolicy Bypass -File C:\poc\guifanchaxun\webapp\start.ps1
```
