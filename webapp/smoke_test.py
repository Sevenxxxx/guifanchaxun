"""SDK 直连冒烟(绕过 Web):验证运行时启动、通知流、final_response。

用法: python webapp\\smoke_test.py ["提示词"] [--session-id xxx]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent
sys.path.insert(0, str(WEBAPP.parent))
from webapp import config  # noqa: E402

sys.path.insert(0, str(config.DSH_CHECKOUT / "python" / "sdk" / "src"))
from deepseek_harness import DeepSeekHarness  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", nargs="?", default="你好,请只回复两个字:收到")
    ap.add_argument("--session-id", default="smoke-001")
    args = ap.parse_args()

    counts: dict[str, int] = {}
    text_lens: list[int] = []

    def on_notification(n) -> None:
        counts[n.method] = counts.get(n.method, 0) + 1
        if n.method == "session.event":
            ev = n.payload.get("event") if isinstance(n.payload, dict) else None
            if isinstance(ev, dict) and ev.get("type") == "assistant/message":
                data = ev.get("data") if isinstance(ev.get("data"), dict) else {}
                msg = data.get("message")
                owner = msg if isinstance(msg, dict) else data
                content = owner.get("content")
                if isinstance(content, list):
                    text = "".join(
                        str(b.get("text") or "")
                        for b in content
                        if isinstance(b, dict) and b.get("type") == "text"
                    )
                    text_lens.append(len(text))

    print(f"[smoke] 启动运行时 profile=sdk home={config.DSH_HOME} ...", flush=True)
    with DeepSeekHarness(
        provider=config.PROVIDER,
        model=config.MODEL,
        reasoning_effort=config.REASONING_EFFORT,
        cwd=str(config.REPO_ROOT),
        runtime_cwd=str(config.REPO_ROOT),
        dsh_bin=str(config.LAUNCHER),
        profile="sdk",
        dsh_home=str(config.DSH_HOME),
        initialize_timeout_seconds=config.INIT_TIMEOUT_SECONDS,
    ) as harness:
        print("[smoke] 运行时已启动,发送提示词 ...", flush=True)
        result = harness.run(args.prompt, session_id=args.session_id, on_notification=on_notification)
        print(f"[smoke] finish_reason = {result.finish_reason}", flush=True)
        print(f"[smoke] 通知统计 = {counts}", flush=True)
        print(f"[smoke] assistant 文本流长度序列 = {text_lens}", flush=True)
        print("[smoke] final_response =", flush=True)
        print(result.final_response, flush=True)

    print("[smoke] OK", flush=True)


if __name__ == "__main__":
    main()
