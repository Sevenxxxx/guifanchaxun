"""护栏验收:对指定端口跑各类拒绝路径检查(不消耗 LLM)。

用法:
    python webapp\\api_guard_test.py --port 8109 --case badtoken|toolong|rate|capacity|turns|all
- badtoken/toolong:无需特殊配置,`all` 默认只跑这两个。
- rate/capacity/turns:需服务端以对应环境变量单独启动再验证——
    GFC_RATE_SESSION=0(限流) / GFC_MAX_CONCURRENT=0(容量已满) / GFC_MAX_TURNS=0(轮数上限)。
  三者互斥,不能在一次启动里同时验证,故须逐个跑。
"""
from __future__ import annotations

import argparse
import http.client
import json
import sys


def request(port: int, method: str, path: str, body: dict | None, expect: int) -> tuple[int, str]:
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=30)
    payload = json.dumps(body) if body is not None else None
    conn.request(method, path, body=payload, headers={"Content-Type": "application/json"})
    resp = conn.getresponse()
    text = resp.read().decode("utf-8", "replace")
    status = resp.status
    conn.close()
    mark = "PASS" if status == expect else "FAIL"
    print(f"[{mark}] {method} {path} -> {status} (期望 {expect}) | {text[:120]}")
    return status, text


def new_token(port: int) -> str:
    status, text = request(port, "POST", "/api/session", None, 200)
    if status != 200:
        sys.exit(1)
    return json.loads(text)["token"]


def case_badtoken(port: int) -> None:
    request(port, "POST", "/api/chat", {"token": "forged-token-abc", "message": "你好"}, 422)


def case_toolong(port: int) -> None:
    token = new_token(port)
    request(port, "POST", "/api/chat", {"token": token, "message": "长" * 9000}, 400)


def case_rate(port: int) -> None:
    token = new_token(port)
    request(port, "POST", "/api/chat", {"token": token, "message": "你好"}, 429)


def case_turns(port: int) -> None:
    token = new_token(port)
    request(port, "POST", "/api/chat", {"token": token, "message": "你好"}, 429)


def case_capacity(port: int) -> None:
    """需要服务端以 GFC_MAX_CONCURRENT=0 启动:任何请求都应 429(容量已满)。"""
    token = new_token(port)
    request(port, "POST", "/api/chat", {"token": token, "message": "你好"}, 429)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8109)
    ap.add_argument("--case", default="all", choices=["badtoken", "toolong", "rate", "capacity", "turns", "all"])
    args = ap.parse_args()
    if args.case == "all":
        print("注:rate/capacity/turns 需服务端以对应环境变量单独启动验证,故 all 只跑无需特殊配置的 badtoken/toolong。")
        cases = ["badtoken", "toolong"]
    else:
        cases = [args.case]
    for case in cases:
        globals()[f"case_{case}"](args.port)


if __name__ == "__main__":
    main()
