"""FastAPI 应用:极简聊天 API(SSE 流式)+ 静态页面 + 会话令牌/护栏。"""
from __future__ import annotations

import asyncio
import json
import logging
import secrets
import shutil
import time
import uuid
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from webapp import config
from webapp.dsh_service import DshTurnError, service

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="guifan-chaxun Web POC")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# ---- 审计日志 ----
config.LOG_DIR.mkdir(exist_ok=True)
_logger = logging.getLogger("poc")
_logger.setLevel(logging.INFO)
_log_handler = logging.FileHandler(config.LOG_DIR / "poc.log", encoding="utf-8")
_log_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
_logger.addHandler(_log_handler)

# 客户端断开后运行中的轮次继续跑完(协议无取消):保留引用防 GC,结束时丢弃
_background_tasks: set[asyncio.Task] = set()
_SENTINEL = object()

# ---- 会话登记表(token → 会话) ----
@dataclass
class Conv:
    token: str
    dsh_session_id: str
    created: float
    last_used: float
    turns: int = 0

_convos: dict[str, Conv] = {}

# ---- 限流(滑动窗口,事件循环单线程访问,无需锁) ----
_rate_global: deque = deque()
_rate_session: dict[str, deque] = {}

# 排队/运行中的轮次数(含当前正在跑的)
_pending_box = [0]


class ChatRequest(BaseModel):
    token: str
    message: str


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def _check_access_token(request: Request) -> None:
    if not config.ACCESS_TOKEN:
        return
    provided = request.headers.get("X-Access-Token") or request.query_params.get("token")
    if provided != config.ACCESS_TOKEN:
        _logger.warning("auth:reject ip=%s", request.client.host if request.client else "?")
        raise HTTPException(status_code=401, detail="访问口令错误")


def _rate_allow(bucket: deque, limit: int, now: float) -> bool:
    while bucket and now - bucket[0] > 60:
        bucket.popleft()
    if len(bucket) >= limit:
        return False
    bucket.append(now)
    return True


def _purge_dsh_session(session_id: str) -> None:
    """删除 dsh-home 下该会话的持久化目录(运行时 zstd JSONL)。"""
    sessions_root = config.DSH_HOME / "sessions"
    if not sessions_root.exists():
        return
    for path in sessions_root.rglob(session_id):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)


def _evict_oldest_sessions() -> list[str]:
    """超上限时淘汰最旧会话,返回被淘汰会话的 dsh_session_id(调用方按需清理持久化目录)。"""
    evicted = []
    while len(_convos) > config.SESSION_CAP:
        oldest = min(_convos.values(), key=lambda c: c.last_used)
        _convos.pop(oldest.token, None)
        evicted.append(oldest.dsh_session_id)
        _logger.info("session:evicted token=%s", oldest.token[:8])
    return evicted


async def _cleanup_loop() -> None:
    """每分钟:淘汰过期/超上限会话并清理其持久化目录与限流桶。"""
    while True:
        await asyncio.sleep(60)
        now = time.time()
        ttl = config.SESSION_TTL_HOURS * 3600
        for token in list(_convos):
            conv = _convos[token]
            if now - conv.last_used > ttl:
                _convos.pop(token, None)
                await asyncio.to_thread(_purge_dsh_session, conv.dsh_session_id)
                _logger.info("session:expired token=%s dsh=%s", token[:8], conv.dsh_session_id)
        for sid in _evict_oldest_sessions():
            await asyncio.to_thread(_purge_dsh_session, sid)
        for token in list(_rate_session):
            if token not in _convos:
                _rate_session.pop(token, None)


@app.on_event("startup")
async def _startup() -> None:
    task = asyncio.create_task(_cleanup_loop())
    _background_tasks.add(task)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
async def health() -> JSONResponse:
    return JSONResponse(
        {
            "ok": True,
            "runtime_started": service.started,
            "last_error": service.last_error,
            "model": f"{config.PROVIDER}/{config.MODEL}",
            "permission_mode": config.PERMISSION_MODE,
            "active_sessions": len(_convos),
        }
    )


@app.post("/api/session")
async def new_session(request: Request) -> JSONResponse:
    """每次调用发放一个全新对话令牌(旧令牌一律不认)。"""
    _check_access_token(request)
    token = secrets.token_urlsafe(16)
    conv = Conv(
        token=token,
        dsh_session_id=str(uuid.uuid4()),
        created=time.time(),
        last_used=time.time(),
    )
    _convos[token] = conv
    for sid in _evict_oldest_sessions():
        await asyncio.to_thread(_purge_dsh_session, sid)
    ip = request.client.host if request.client else "?"
    _logger.info("session:new token=%s dsh=%s ip=%s", token[:8], conv.dsh_session_id, ip)
    return JSONResponse({"token": token})


@app.post("/api/chat")
async def chat(req: ChatRequest, request: Request) -> StreamingResponse:
    _check_access_token(request)
    ip = request.client.host if request.client else "?"

    if not req.message.strip():
        raise HTTPException(status_code=400, detail="消息不能为空")
    if len(req.message.strip()) > config.MAX_MESSAGE_CHARS:
        raise HTTPException(status_code=400, detail=f"消息过长(上限 {config.MAX_MESSAGE_CHARS} 字)")

    conv = _convos.get(req.token)
    if conv is None:
        _logger.warning("chat:reject-bad-token ip=%s", ip)
        raise HTTPException(status_code=422, detail="会话不存在或已过期,请刷新页面")

    now = time.time()
    if not _rate_allow(_rate_global, config.RATE_GLOBAL_MIN, now):
        _logger.warning("chat:rate-global ip=%s", ip)
        raise HTTPException(status_code=429, detail="请求过于频繁,请稍后再试")
    bucket = _rate_session.setdefault(req.token, deque())
    if not _rate_allow(bucket, config.RATE_SESSION_MIN, now):
        _logger.warning("chat:rate-session ip=%s", ip)
        raise HTTPException(status_code=429, detail="本对话请求过于频繁,请稍后再试")

    if _pending_box[0] >= config.MAX_CONCURRENT:
        _logger.warning("chat:capacity-full ip=%s", ip)
        raise HTTPException(
            status_code=429,
            detail=f"当前同时使用人数已达上限({config.MAX_CONCURRENT} 人),请稍后再试",
        )

    conv.last_used = now
    conv.turns += 1
    if conv.turns > config.MAX_TURNS:
        _logger.warning("chat:turns-limit token=%s", req.token[:8])
        raise HTTPException(status_code=429, detail=f"本对话已达轮数上限({config.MAX_TURNS} 轮),请刷新页面开始新对话")

    _logger.info(
        "chat:start token=%s turn=%d len=%d ip=%s",
        req.token[:8], conv.turns, len(req.message), ip,
    )
    _pending_box[0] += 1

    queue: asyncio.Queue = asyncio.Queue()
    loop = asyncio.get_running_loop()

    def emit(event: dict) -> None:
        # 从 SDK 读取线程回调 -> 投递到事件循环队列,保证 SSE 顺序
        try:
            loop.call_soon_threadsafe(queue.put_nowait, event)
        except RuntimeError:
            pass  # 事件循环已关闭(进程退出):丢弃后续事件,避免杀死 SDK 读取线程

    async def runner():
        try:
            return await asyncio.to_thread(service.run_turn, conv.dsh_session_id, req.message, emit)
        finally:
            try:
                loop.call_soon_threadsafe(queue.put_nowait, _SENTINEL)
            except RuntimeError:
                pass

    initial_status = {"status": "starting"}
    started = time.time()
    task = asyncio.create_task(runner())
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)

    def on_task_done(done_task: asyncio.Task) -> None:
        # 无论客户端是否断开都记录结果(观测缺口修复)
        _pending_box[0] = max(0, _pending_box[0] - 1)
        exc = done_task.exception()
        if exc is not None:
            _logger.info("chat:error token=%s dur=%.1fs err=%s", req.token[:8], time.time() - started, str(exc)[:200])
        else:
            result = done_task.result()
            _logger.info(
                "chat:done token=%s dur=%.1fs finish=%s",
                req.token[:8], time.time() - started, result.finish_reason,
            )

    task.add_done_callback(on_task_done)

    async def gen():
        yield _sse("status", initial_status)
        while True:
            item = await queue.get()
            if item is _SENTINEL:
                break
            event: dict = item
            kind = event.pop("kind", "event")
            yield _sse(kind, event)
        try:
            result = await task
        except Exception as exc:  # noqa: BLE001 —— 把运行时/协议错误透给前端(CancelledError 不在此列,自然传播)
            message = str(exc) or type(exc).__name__
            service.last_error = message
            if isinstance(exc, DshTurnError) and exc.is_collision:
                # 运行时重启后旧会话 id 失效:前端换新令牌自动重发
                yield _sse("session_reset", {"message": message})
            else:
                yield _sse("error", {"message": message})
        else:
            yield _sse(
                "done",
                {
                    "finish_reason": result.finish_reason,
                    "final_response": result.final_response,
                },
            )

    return StreamingResponse(
        gen(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
