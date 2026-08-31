# Windows Server 2022 部署 Runbook（2核2G / 50G / 完整桌面版）

> 照抄即可；`<...>` 为需替换内容。路径规划固定为 `C:\poc\`，如需变更请全局替换。

## 0. 前置

- 腾讯云控制台：拿到公网 IP、重置管理员密码
- **安全组放行 TCP 8090**（腾讯云控制台 → 轻量应用服务器 → 防火墙/安全组 → 添加规则：TCP 8090，来源 0.0.0.0/0 或限定网段）
- 本机远程桌面：`mstsc` → 公网 IP（端口 3389）

## 1. 安装环境（服务器上，管理员）

```powershell
# Python 3.12(官网 python.org 下载 Windows x64 安装包;安装时勾选 Add python.exe to PATH)
python --version
python -m pip install fastapi uvicorn sse-starlette

# Node.js LTS(官网 nodejs.org 下载 msi 安装)
node --version
```

## 2. 上传文件到 C:\poc\

```
C:\poc\
├── guifanchaxun\        ← 项目(webapp/ + guifansrc/ 4GB + library_data/ 138MB)
│   ├── webapp\          ← 含 setup_win_server.ps1 / start.ps1 / dsh_launcher.cmd
│   ├── guifansrc\
│   └── library_data\
└── deepseek-harness\    ← 本机整个 checkout(~2GB,含 node_modules,直接复制)
```

上传方式（按大小选）：
- `webapp` + `library_data`（小）：RDP 复制粘贴 / 共享文件夹 / 网盘均可
- `deepseek-harness`（2GB）：RDP 磁盘映射或 WinSCP；**Windows→Windows 直接复制，原生二进制兼容，无需重装依赖**
- `guifansrc`（4GB，最大头）：推荐 WinSCP(OpenSSH)断点续传 或 腾讯云 COS 中转；RDP 拖拽慢（后议，可最后传）

## 3. skills 目录（服务器上）

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
Copy-Item C:\poc\guifanchaxun\tools\guifan-chaxun "$env:USERPROFILE\.agents\skills\" -Recurse
Copy-Item C:\poc\guifanchaxun\tools\guifan-chaxun-scripts "$env:USERPROFILE\.agents\skills\" -Recurse
```

**改 skill 配置路径**（必做）：编辑
`C:\Users\<管理员>\.agents\skills\guifan-chaxun-scripts\config.json`：
```json
{
  "library_dir": "C:\\poc\\guifanchaxun\\guifansrc",
  "data_dir": "C:\\poc\\guifanchaxun\\library_data",
  ...其余不动
}
```

## 4. 改 POC 的 3 处路径（必做）

1. `C:\poc\guifanchaxun\webapp\config.py`：
   - `DSH_CHECKOUT = Path(r"C:\poc\deepseek-harness")`
   - `DSH_HOME = WEBAPP_DIR / "dsh-home"`（不变）
   - `LAUNCHER = WEBAPP_DIR / "dsh_launcher.cmd"`（不变）
2. `C:\poc\guifanchaxun\webapp\dsh_launcher.cmd`：
   ```cmd
   cd /d "C:\poc\deepseek-harness"
   node apps\cli\lib\bin.js %*
   ```

## 5. 设置 DEEPSEEK_API_KEY（你自己输入，不落任何文件/脚本）

```powershell
[Environment]::SetEnvironmentVariable('DEEPSEEK_API_KEY', 'sk-你的key', 'Machine')
# 设置后重启 PowerShell 会话生效;验证:
[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY', 'Machine')
```

## 6. 初始化 + 启动

```powershell
cd C:\poc\guifanchaxun
powershell -ExecutionPolicy Bypass -File webapp\setup_win_server.ps1   # 材质化 sdk profile(离线)
# 确认输出 OK + skill rows: 3

powershell -ExecutionPolicy Bypass -File webapp\start.ps1              # 前台启动,先验证
# 另开一个 PowerShell 验证:
Invoke-WebRequest http://127.0.0.1:8090/api/health -UseBasicParsing
```

## 7. 防火墙放行（服务器本地防火墙，管理员）

```powershell
New-NetFirewallRule -DisplayName "DSH Web POC 8090" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8090 -Profile Any
```

## 8. 2GB 内存调优（并发 5 必做）

1. 增大分页文件：`sysdm.cpl` → 高级 → 性能"设置" → 高级 → 虚拟内存"更改"：
   取消"自动管理"，C 盘自定义 **初始 4096 MB / 最大 8192 MB**，确定后重启生效。
   （等效命令行：`wmic computersystem set AutomaticManagedPagefile=False` +
   `wmic pagefileset create name="C:\pagefile.sys"` + 设 Initial/MaximumSize）
2. 确认并发上限：`config.py` 的 `GFC_MAX_CONCURRENT` 默认 5；若上线后内存吃紧
   （`Get-Process` 看 dsh/node 内存、页面卡顿），降到 3。

## 9. 开机自启（任务计划，管理员）

```powershell
schtasks /Create /F /TN "DSHWebPOC" /SC ONSTART /RU SYSTEM /RL HIGHEST `
  /TR "powershell -ExecutionPolicy Bypass -File C:\poc\guifanchaxun\webapp\start.ps1"
schtasks /Run /TN "DSHWebPOC"    # 立即跑一次验证
```
> start.ps1 内部已自动切到仓库根目录，任务计划无需设"起始于"。
> 重启服务器后 1-2 分钟自动拉起；验证：`Invoke-WebRequest http://127.0.0.1:8090/api/health`。

## 10. 上线验证清单

- [ ] 公网 `http://<公网IP>:8090` 打开页面；Tailscale `http://<服务器tailscale-ip>:8090` 也能开
- [ ] 提问规范问题 → 正常流式回答（首问等几秒，DSH 运行时懒启动）
- [ ] 只读生效：让 agent 写文件 → 被拒；问"更新索引" → 失败
- [ ] 刷新页面 = 新对话；两台设备同时问 → 并行
- [ ] 第 6 人同时提问 → 提示"当前同时使用人数已达上限(5 人)"
- [ ] 审计日志 `webapp\logs\poc.log` 有记录

## 11. 日常维护

- 知识库更新：**本机**跑 `spec.py index/remove` → 只上传 `library_data\`（138MB）覆盖服务器同目录 → 生效
- 查内存：`Get-Process | Where-Object { $_.ProcessName -in @('node','python') } | Sort-Object WorkingSet64 -Descending`
- 看日志：`Get-Content C:\poc\guifanchaxun\webapp\logs\poc.log -Tail 50`

## 12. 故障排查

- 首问 MISSING_CREDENTIAL → 环境变量没生效：重启 PowerShell/服务器，或 `[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY','Machine')` 确认
- setup 失败 → 看 `webapp\dump-default-config.txt`；确认 dsh_launcher.cmd 路径正确、Node 已装
- 公网打不开但本机 OK → 安全组（腾讯云控制台）或服务器防火墙漏放行 8090
- 内存告急 → `GFC_MAX_CONCURRENT` 降 3、pagefile 加大
