#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't -- make.fun entry.

Writes one line, a funny weather forecast for the invented city of
Gloomburg, to ``entry.txt`` inside the output directory (``$OUTPUT_DIR``,
default ``/output``).

Pure Python standard library only; no third-party dependencies, so the
grader's vanilla Python runs it as-is. The output is a fixed string, so
every run writes byte-identical text.
"""

import os
import sys

ENTRY = (
    "Gloomburg: overcast with a 90% chance of Tuesdays. "
    "Umbrellas useless \u2014 bring a calendar and low expectations."
)

MAX_CHARS = 120


def validate(text: str) -> str:
    """Return the entry text if it passes the gate, else fail loudly."""
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-120 characters, got %d" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main() -> int:
    text = validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
