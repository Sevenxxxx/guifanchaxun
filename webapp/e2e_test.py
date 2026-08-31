"""端到端验收脚本:POST /api/session 取令牌 → POST /api/chat 流式打印 SSE。

用法(先启动后端 python -m webapp):
    python webapp\\e2e_test.py "JTG 5120-2021 对桥梁检查周期是怎么规定的?"
    python webapp\\e2e_test.py "上一个问题的条文号是多少?" --token <上一条输出的 token>
"""
from __future__ import annotations

import argparse
import http.client
import json
import sys


def main() -> None:
    ap = argparse.ArgumentParser(description="guifan-chaxun Web POC 验收客户端")
    ap.add_argument("message")
    ap.add_argument("--token", default=None, help="复用已有令牌即多轮;缺省新建会话")
    ap.add_argument("--port", type=int, default=8090)
    ap.add_argument("--timeout", type=float, default=1800.0)
    args = ap.parse_args()

    conn = http.client.HTTPConnection("127.0.0.1", args.port, timeout=args.timeout)

    token = args.token
    if token is None:
        conn.request("POST", "/api/session", headers={"Content-Type": "application/json"})
        resp = conn.getresponse()
        if resp.status != 200:
            print(f"[失败] 创建会话 HTTP {resp.status}: {resp.read().decode('utf-8', 'replace')}")
            sys.exit(1)
        token = json.loads(resp.read().decode("utf-8"))["token"]
        print(f"[新会话] token={token}")

    body = json.dumps({"token": token, "message": args.message})
    conn.request("POST", "/api/chat", body=body, headers={"Content-Type": "application/json"})
    resp = conn.getresponse()
    if resp.status != 200:
        print(f"[失败] HTTP {resp.status}: {resp.read().decode('utf-8', 'replace')}")
        sys.exit(1)

    buffer = ""
    activities = 0
    last_text = ""
    final = ""
    while True:
        chunk = resp.read(65536)
        if not chunk:
            break
        buffer += chunk.decode("utf-8", "replace")
        while "\n\n" in buffer:
            frame, buffer = buffer.split("\n\n", 1)
            event, data = "message", ""
            for line in frame.split("\n"):
                if line.startswith("event:"):
                    event = line[6:].strip()
                elif line.startswith("data:"):
                    data += line[5:].strip()
            if not data:
                continue
            payload = json.loads(data)
            if event == "text":
                last_text = payload.get("text") or ""
                print(f"\r[文本流] {len(last_text)} 字", end="")
            elif event == "activity":
                activities += 1
                print(f"\n[活动] {payload.get('type')}: {(payload.get('summary') or '')[:150]}")
            elif event == "status":
                extra = ""
                if payload.get("status") == "queued" and "position" in payload:
                    extra = f"(前有 {payload.get('position')} 个,预计 {payload.get('eta_seconds')}s)"
                print(f"\n[状态] {payload.get('status')}{extra}")
            elif event == "done":
                final = payload.get("final_response") or ""
                print(f"\n[完成] finish_reason={payload.get('finish_reason')}")
            elif event == "error":
                print(f"\n[错误] {payload.get('message')}")
            elif event == "session_reset":
                print(f"\n[会话重置] {payload.get('message')}")

    print("\n\n========== 最终回复 ==========")
    print(final or last_text or "(空)")
    print(f"\n活动事件 {activities} 条;多轮请复用: --token {token}")


if __name__ == "__main__":
    main()
