"""mock_session.py — simulate Claude Code appending JSONL turns.

Usage:
  python mock_session.py <path-to-session.jsonl> [--turns N] [--interval-ms MS]

Writes a valid assistant turn every --interval-ms ms, ramping up cache_read so
ctxguard run --budget=N eventually trips.
"""

import argparse, json, os, sys, time, uuid
from datetime import datetime, timezone


def make_turn(model: str, input_tokens: int, output_tokens: int,
              cache_read: int, cache_write: int = 0):
    return {
        "parentUuid": str(uuid.uuid4()),
        "isSidechain": False,
        "promptId": str(uuid.uuid4()),
        "agentId": None,
        "type": "assistant",
        "message": {
            "id": str(uuid.uuid4()),
            "type": "message",
            "role": "assistant",
            "model": model,
            "content": [{"type": "text", "text": "ok"}],
            "stop_reason": "end_turn",
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "cache_creation_input_tokens": cache_write,
                "cache_read_input_tokens": cache_read,
            },
        },
        "uuid": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="session .jsonl path to append to")
    ap.add_argument("--turns", type=int, default=10)
    ap.add_argument("--interval-ms", type=int, default=300)
    ap.add_argument("--model", default="claude-opus-4-8[1m]")
    ap.add_argument("--start-cache-read", type=int, default=0)
    ap.add_argument("--step-cache-read", type=int, default=200)
    args = ap.parse_args()

    cache_read = args.start_cache_read
    for i in range(args.turns):
        cache_read += args.step_cache_read
        turn = make_turn(
            model=args.model,
            input_tokens=100,
            output_tokens=80,
            cache_read=cache_read,
        )
        with open(args.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(turn) + "\n")
        print(f"[mock] turn {i+1}/{args.turns}: cache_read={cache_read}", flush=True)
        time.sleep(args.interval_ms / 1000.0)


if __name__ == "__main__":
    main()
