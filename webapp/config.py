"""路径与模型配置 —— 换库/换模型只改这里(或用环境变量覆盖)。"""
from __future__ import annotations

import os
from pathlib import Path

# 仓库根(guifanchaxun)与 DSH checkout
REPO_ROOT = Path(__file__).resolve().parent.parent
WEBAPP_DIR = Path(__file__).resolve().parent
DSH_CHECKOUT = Path(os.environ.get("GFC_DSH_CHECKOUT", r"C:\Users\Seven\Desktop\deepseek-harness"))  # 服务器用 GFC_DSH_CHECKOUT 覆盖,git pull 不影响;与 dsh_launcher.cmd 保持一致
DSH_HOME = WEBAPP_DIR / "dsh-home"  # POC 独立 home:会话/凭据/设置与 GUI 隔离
LAUNCHER = WEBAPP_DIR / "dsh_launcher.cmd"  # dsh CLI 启动包装

# LLM 路由(POC 默认 flash,更快更省;GUI 会话仍用 pro,互不影响)
PROVIDER = os.environ.get("GFC_PROVIDER", "deepseek-official")
MODEL = os.environ.get("GFC_MODEL", "deepseek-v4-flash")
# flash 默认不指定推理强度,保留模型自身默认;pro 可设 GFC_REASONING_EFFORT=max
REASONING_EFFORT = os.environ.get("GFC_REASONING_EFFORT") or None

# Web 服务(避开 GUI 的 3080)
HOST = os.environ.get("GFC_HOST", "127.0.0.1")
PORT = int(os.environ.get("GFC_PORT", "8090"))

# 首次启动运行时(含模型路由握手)的时限
INIT_TIMEOUT_SECONDS = float(os.environ.get("GFC_INIT_TIMEOUT", "60"))

# ===== 安全/成本护栏(云部署+同事使用;全部可用环境变量覆盖) =====
PERMISSION_MODE = os.environ.get("GFC_PERMISSION_MODE", "read-only")   # 只读沙箱(写保护,必选)
TELEMETRY_MODE = os.environ.get("GFC_TELEMETRY_MODE", "DISABLED")      # 关闭会话遥测上传
MAX_TOKENS = int(os.environ.get("GFC_MAX_TOKENS", "32768"))            # 单轮输出封顶(放宽)
TURN_TIMEOUT_SEC = float(os.environ.get("GFC_TURN_TIMEOUT", "1800"))   # 单轮超时(秒,放宽 30 分钟)
MAX_MESSAGE_CHARS = int(os.environ.get("GFC_MAX_MESSAGE_CHARS", "8000"))  # 消息长度上限(放宽)
MAX_TURNS = int(os.environ.get("GFC_MAX_TURNS", "100"))                # 每会话轮数上限(放宽)
RATE_GLOBAL_MIN = int(os.environ.get("GFC_RATE_GLOBAL", "120"))        # 全局限流(次/分)
RATE_SESSION_MIN = int(os.environ.get("GFC_RATE_SESSION", "30"))       # 每会话限流(次/分)
MAX_CONCURRENT = int(os.environ.get("GFC_MAX_CONCURRENT", "5"))        # 同时使用上限(超了直接拒绝,不排队)
SESSION_TTL_HOURS = float(os.environ.get("GFC_SESSION_TTL", "24"))     # 会话闲置过期(小时)
SESSION_CAP = int(os.environ.get("GFC_SESSION_CAP", "100"))            # 活跃会话上限
SSE_HEARTBEAT_SEC = float(os.environ.get("GFC_SSE_HEARTBEAT", "15"))    # SSE 心跳(秒),长回复保活防中断
ACCESS_TOKEN = os.environ.get("GFC_ACCESS_TOKEN", "")                  # 非空=启用访问口令(可选;优先用下方文件)
PASSWORD_FILE = Path(os.environ.get("GFC_PASSWORD_FILE", WEBAPP_DIR / "access.txt"))  # 单密码文件(存在且非空=进入需密码,改文件即生效)
GUARDRAIL_PATCH = WEBAPP_DIR / "sdk-guardrail.patch.yml"               # 提示词护栏 patch
LOG_DIR = WEBAPP_DIR / "logs"                                          # 审计日志目录
