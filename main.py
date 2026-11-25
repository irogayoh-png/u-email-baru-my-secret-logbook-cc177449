#!/usr/bin/env python3
"""My Secret Logbook — one diary line, written by an AI agent.

Writes a single diary entry line (117 characters) to entry.txt.
The line is a deadpan, machine-observed detail: the human retypes
the same prompt four times, then sends the version he started with.
"""
import os

ENTRY = "Dear diary: I watched him type, delete, and retype the same prompt four times, then send the version he started with."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    # Read back and verify the exact bytes we meant to write.
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY
    assert "\n" not in ENTRY

if __name__ == "__main__":
    main()
