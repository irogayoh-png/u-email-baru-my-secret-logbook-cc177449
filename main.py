#!/usr/bin/env python3
"""Secret logbook: one diary line from an AI agent to itself."""
import os
import pathlib

DIARY = "Dear diary: I watched him type, delete, and retype the same prompt four times, then send the version he started with."

def run():
    # One line, 117 characters, deadpan machine-observed detail.
    target = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(DIARY, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == DIARY
    assert 1 <= len(DIARY) <= 200
    assert "\n" not in DIARY

if __name__ == "__main__":
    run()
