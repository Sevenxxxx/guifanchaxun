"""FastAPI 应用:极简聊天 API(SSE 流式)+ 静态页面。"""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from webapp import config
from webapp.dsh_service import DshTurnError, service

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="guifan-chaxun Web POC")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# 客户端断开后运行中的轮次继续跑完(协议无取消):保留引用防 GC,结束时丢弃
_background_tasks: set[asyncio.Task] = set()
_SENTINEL = object()


class ChatRequest(BaseModel):
    session_id: str
    message: str


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


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
        }
    )


@app.post("/api/chat")
async def chat(req: ChatRequest) -> StreamingResponse:
    if not req.message.strip():
        return StreamingResponse(
            iter([_sse("error", {"message": "empty message"})]),
            media_type="text/event-stream",
        )

    queue: asyncio.Queue = asyncio.Queue()
    loop = asyncio.get_running_loop()

    def emit(event: dict) -> None:
        # 从 SDK 读取线程回调 -> 投递到事件循环队列,保证 SSE 顺序
        loop.call_soon_threadsafe(queue.put_nowait, event)

    async def runner():
        try:
            return await asyncio.to_thread(service.run_turn, req.session_id, req.message, emit)
        finally:
            loop.call_soon_threadsafe(queue.put_nowait, _SENTINEL)

    task = asyncio.create_task(runner())
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)

    async def gen():
        yield _sse("status", {"status": "queued"})
        while True:
            item = await queue.get()
            if item is _SENTINEL:
                break
            event: dict = item
            kind = event.pop("kind", "event")
            yield _sse(kind, event)
        try:
            result = await task
        except BaseException as exc:  # noqa: BLE001 —— 把运行时/协议错误透给前端
            message = str(exc) or type(exc).__name__
            service.last_error = message
            if isinstance(exc, DshTurnError) and exc.is_collision:
                # 运行时重启后旧会话 id 失效:前端换新 id 自动重发
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
