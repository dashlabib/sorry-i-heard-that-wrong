#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line to /output/entry.txt (the apology a smart speaker gives
its owner after mishearing them) and prints the same bytes to stdout,
with no trailing newline. Deterministic: the same line every run.
"""

import os
import sys

LINE = (
    "Sorry \u2014 I heard 'set a timer for ten minutes' as "
    "'adopt ten kittens.' I've named them all Timer, and one "
    "is asleep on your router."
)


def output_dir():
    """Pick where entry.txt goes: the grader's /output first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main():
    data = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 140:
        sys.stderr.write(
            "entry must be 1-140 characters, got %d\n" % len(LINE)
        )
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        sys.stderr.write("read-back mismatch: file != stdout bytes\n")
        return 1
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
