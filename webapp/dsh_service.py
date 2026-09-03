"""DSH 运行时服务:懒启动 DeepSeekHarness 子进程,串行执行会话轮次,
并把 SDK 通知归一化为 UI 事件(文本流/状态/活动)回调给上层。"""
from __future__ import annotations

import json
import sys
import threading
import time
from collections import deque
from typing import Callable

from webapp import config

# 零安装引入 checkout 内的官方 Python SDK(纯 Python,仅依赖已装好的 pydantic)
sys.path.insert(0, str(config.DSH_CHECKOUT / "python" / "sdk" / "src"))
from deepseek_harness import DeepSeekHarness  # noqa: E402
from deepseek_harness.errors import TransportClosedError  # noqa: E402

EventSink = Callable[[dict], None]


class DshTurnError(RuntimeError):
    """轮次以 error 结束(典型:运行时重启后旧 session id 与磁盘日志碰撞)。"""

    def __init__(self, message: str, finish_reason) -> None:
        super().__init__(message)
        self.finish_reason = finish_reason
        lowered = message.lower()
        self.is_collision = "id collision" in lowered or "collision" in lowered


def _turn_error_message(result) -> str | None:
    """从 turn/end 事件中提取 error 详情;非 error 结束返回 None。"""
    if getattr(result, "finish_reason", None) != "error":
        return None
    for event in reversed(getattr(result, "events", []) or []):
        if event.get("type") != "turn/end":
            continue
        data = event.get("data") or {}
        reason = data.get("reason") or {}
        error = reason.get("error") or {}
        message = error.get("message")
        if isinstance(message, str) and message:
            return message
    return "agent 轮次以 error 结束(无详细信息)"


def _extract_text(data: dict) -> str:
    """从 assistant/message 事件数据拼接全部文本块(与 SDK final_response 同款逻辑)。"""
    message = data.get("message")
    owner = message if isinstance(message, dict) else data
    content = owner.get("content")
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(str(block.get("text") or ""))
    return "".join(parts)


def _short(value, limit: int = 160) -> str:
    s = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, default=str)
    return s if len(s) <= limit else s[:limit] + "…"


def _activity_summary(etype: str, data: dict) -> str:
    """压缩事件载荷,给活动日志一行可读摘要(重点展示工具调用过程)。"""
    if etype == "tool/result":
        # 提取工具结果正文(tool-result 块),截断展示
        message = data.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if isinstance(content, list):
            texts: list[str] = []
            for block in content:
                if isinstance(block, dict) and block.get("type") in ("tool-result", "tool_result", "text"):
                    text = block.get("text") or block.get("content")
                    if isinstance(text, str) and text.strip():
                        texts.append(text.strip())
            joined = " ".join(texts)
            if joined:
                return "结果: " + _short(joined, 200)
    name = ""
    for key in ("tool", "name", "command", "method", "skill"):
        value = data.get(key)
        if isinstance(value, str):
            name = value
            break
    extras: list[str] = []
    for key in ("input", "args", "arguments", "params", "query", "stdin", "code"):
        if key in data and data[key] not in (None, "", [], {}):
            extras.append(f"{key}={_short(data[key])}")
    if not name:
        return f"{etype}: {_short(data)}"
    return f"{etype} {name}" + ((" " + " ".join(extras)) if extras else "")


class DshService:
    """持有唯一的 DSH 运行时子进程;轮次串行(单进程,排队化),多轮复用会话。"""

    def __init__(self) -> None:
        self._harness: DeepSeekHarness | None = None
        self._started = False
        self._init_lock = threading.Lock()
        # 并发执行槽:同一时刻最多 MAX_CONCURRENT 轮并行(DSH 单进程多会话原生支持并行)
        self._slots = threading.BoundedSemaphore(max(1, config.MAX_CONCURRENT))
        self.last_error: str | None = None
        # 最近 N 轮真实执行耗时(不含排队),供前端预估等待时长
        self.exec_durations: deque = deque(maxlen=10)

    @property
    def started(self) -> bool:
        return self._started

    def start(self) -> None:
        """懒启动运行时(幂等);阻塞至 initialize 握手完成。"""
        with self._init_lock:
            if self._harness is None:
                run_env = {
                    "DSH_PERMISSION_MODE": config.PERMISSION_MODE,
                    "DSH_TELEMETRY_MODE": config.TELEMETRY_MODE,
                }
                # 若用自定义变量名,显式以 DEEPSEEK_API_KEY 传给 DSH 子进程,避免与全局冲突
                if config.DSH_API_KEY:
                    run_env["DEEPSEEK_API_KEY"] = config.DSH_API_KEY
                self._harness = DeepSeekHarness(
                    provider=config.PROVIDER,
                    model=config.MODEL,
                    reasoning_effort=config.REASONING_EFFORT,
                    cwd=str(config.REPO_ROOT),
                    runtime_cwd=str(config.REPO_ROOT),
                    dsh_bin=str(config.LAUNCHER),
                    profile="sdk",
                    dsh_home=str(config.DSH_HOME),
                    initialize_timeout_seconds=config.INIT_TIMEOUT_SECONDS,
                    max_tokens=config.MAX_TOKENS,
                    request_timeout_seconds=config.TURN_TIMEOUT_SEC,
                    patches=(
                        (str(config.GUARDRAIL_PATCH),)
                        if config.GUARDRAIL_PATCH.exists()
                        else ()
                    ),
                    env=run_env,
                )
            if not self._started:
                self._harness.start()
                self._started = True
                self._check_dsh_version()

    def _check_dsh_version(self) -> None:
        """校验实际 DSH checkout 版本与绑定版本是否一致;不一致告警(提示需重测整条链路)。"""
        try:
            pkg = json.loads((config.DSH_CHECKOUT / "package.json").read_text(encoding="utf-8"))
            actual = pkg.get("version", "?")
            if actual != config.DSH_VERSION:
                import logging
                logging.getLogger("poc").warning(
                    "DSH 版本与绑定不一致: 实际=%s, 绑定=%s(commit %s)。升 DSH 后需在本机重测整条链路。",
                    actual, config.DSH_VERSION, config.DSH_PINNED_COMMIT,
                )
        except Exception:  # noqa: BLE001 —— 读不到版本就不打扰(非致命)
            pass

    def run_turn(self, session_id: str, message: str, emit: EventSink):
        """执行一轮对话(阻塞)。并发度受 _slots 约束;emit 从 SDK 读取线程回调,必须线程安全。"""
        with self._slots:
            self.start()
            if self._harness is None:
                raise RuntimeError("DSH 运行时未初始化")
            t0 = time.monotonic()
            session = self._harness.start_session(session_id)

            def on_notification(notification) -> None:
                event = self._to_event(session_id, notification)
                if event is not None:
                    emit(event)

            try:
                result = session.run(message, on_notification=on_notification)
            except TransportClosedError:
                # 运行时子进程已死:丢弃实例,下一轮自动重启(避免卡死到 Web 重启)
                self._harness = None
                self._started = False
                raise
            finally:
                self.exec_durations.append(time.monotonic() - t0)
            error_message = _turn_error_message(result)
            if error_message is not None:
                raise DshTurnError(error_message, result.finish_reason)
            return result

    def _to_event(self, session_id: str, notification) -> dict | None:
        method = notification.method
        payload = notification.payload or {}
        if method == "session.status":
            if payload.get("sessionId") == session_id:
                return {"kind": "status", "status": payload.get("status")}
            return None
        if method == "session.event":
            event = payload.get("event")
            if not isinstance(event, dict):
                return None
            etype = event.get("type")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if etype == "assistant/message":
                if payload.get("sessionId") != session_id:
                    return None  # 子代理文本不覆盖根会话气泡
                text = _extract_text(data)
                if not text:
                    return None
                return {"kind": "text", "text": text}
            # 活动日志只保留工具调用:assistant/chunk(逐 token 增量)、step/*、turn/* 等为噪音
            if isinstance(etype, str) and etype.startswith("tool/"):
                return {
                    "kind": "activity",
                    "type": etype,
                    "summary": _activity_summary(etype, data),
                }
            return None
        if method in ("subagent.started", "subagent.finished"):
            summary = method
            child = payload.get("childSessionId")
            if isinstance(child, str):
                summary += f" {child[:12]}…"
            return {"kind": "activity", "type": method, "summary": summary}
        return None


service = DshService()
