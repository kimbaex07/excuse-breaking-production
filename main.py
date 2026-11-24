#!/usr/bin/env python3
"""Write the one-line AI excuse to the output directory.

Reads entry.txt next to this script, validates the competition gate
(1-180 characters, not only whitespace), and writes the exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: output/). Pure Python stdlib.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY_FILE = HERE / "entry.txt"


def main() -> int:
    raw = ENTRY_FILE.read_bytes()
    try:
        line = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("entry.txt is not valid UTF-8", file=sys.stderr)
        return 1

    if not line.strip():
        print("entry.txt is empty or only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 180:
        print(f"entry.txt is {len(line)} characters (gate: 1-180)", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry.txt must be a single line", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(raw)
    os.chmod(out_path, 0o644)
    print(f"wrote {len(raw)} bytes ({len(line)} characters) to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
