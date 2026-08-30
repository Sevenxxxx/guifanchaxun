"""路径与模型配置 —— 换库/换模型只改这里(或用环境变量覆盖)。"""
from __future__ import annotations

import os
from pathlib import Path

# 仓库根(guifanchaxun)与 DSH checkout
REPO_ROOT = Path(__file__).resolve().parent.parent
WEBAPP_DIR = Path(__file__).resolve().parent
DSH_CHECKOUT = Path(r"C:\Users\Seven\Desktop\deepseek-harness")  # 与 dsh_launcher.cmd 保持一致
DSH_HOME = WEBAPP_DIR / "dsh-home"  # POC 独立 home:会话/凭据/设置与 GUI 隔离
LAUNCHER = WEBAPP_DIR / "dsh_launcher.cmd"  # dsh CLI 启动包装

# LLM 路由(默认与当前 GUI 会话一致)
PROVIDER = os.environ.get("GFC_PROVIDER", "deepseek-official")
MODEL = os.environ.get("GFC_MODEL", "deepseek-v4-pro")
REASONING_EFFORT = os.environ.get("GFC_REASONING_EFFORT", "max")

# Web 服务(避开 GUI 的 3080)
HOST = os.environ.get("GFC_HOST", "127.0.0.1")
PORT = int(os.environ.get("GFC_PORT", "8090"))

# 首次启动运行时(含模型路由握手)的时限;轮次本身不设超时(规范查询可能多步工具调用)
INIT_TIMEOUT_SECONDS = float(os.environ.get("GFC_INIT_TIMEOUT", "60"))
