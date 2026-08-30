"""诊断:直连 SDK 打开指定会话,打印 error 相关事件与 turn/end 详情。"""
from __future__ import annotations

import json
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent
sys.path.insert(0, str(WEBAPP.parent))
from webapp import config  # noqa: E402

sys.path.insert(0, str(config.DSH_CHECKOUT / "python" / "sdk" / "src"))
from deepseek_harness import DeepSeekHarness  # noqa: E402

session_id = sys.argv[1] if len(sys.argv) > 1 else "e2e-1788079786"
prompt = sys.argv[2] if len(sys.argv) > 2 else "你好,请只回复:在的"

with DeepSeekHarness(
    provider=config.PROVIDER,
    model=config.MODEL,
    reasoning_effort=config.REASONING_EFFORT,
    cwd=str(config.REPO_ROOT),
    runtime_cwd=str(config.REPO_ROOT),
    dsh_bin=str(config.LAUNCHER),
    profile="sdk",
    dsh_home=str(config.DSH_HOME),
) as harness:
    result = harness.run(prompt, session_id=session_id)
    print(f"finish_reason = {result.finish_reason}")
    print(f"final_response = {result.final_response[:300]!r}")
    types = {}
    for ev in result.events:
        t = str(ev.get("type"))
        types[t] = types.get(t, 0) + 1
        if "error" in t.lower() or t == "turn/end":
            print(json.dumps(ev, ensure_ascii=False)[:1200])
    print(f"event types = {types}")
