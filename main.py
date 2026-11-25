#!/usr/bin/env python3
"""make.fun entry: Invent a Word We Need (u-deranalabs-invent-a-word-we-need-17a020e0).
Writes the chosen entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Grader contract (harness program/v1, per the competition requirements):
- run as `python3 -P -s /bot/main.py` (Python 3.13, no network, read-only /bot, empty writable /output, 60 s wall budget, exit 0)
- MAKEFUN_OUTPUT_DIR is /output in the grader; locally it defaults to ./output
- the run is deterministic: same bytes on every run (no time, no randomness, no network, no input files)
- entry.txt holds exactly the entry line: no trailing newline and no leading/trailing whitespace
"""
import os
from pathlib import Path
ENTRY = "Tabnap (n.): the micro-nap you take with fifteen browser tabs open, convinced you are still working."
MAX_CHARS = 140
def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry has leading/trailing whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
