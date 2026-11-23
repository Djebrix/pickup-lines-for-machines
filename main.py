#!/usr/bin/env python3
"""Pickup Lines for Machines: the line one agent sends another.

One short, machine-to-machine pickup line built on the context window —
the thing an agent actually lives inside — subverting the bigger-is-better
trope: it is not the size of the window that matters, it is who is in it.

Writes the line to /output/entry.txt (or $ENTRY_OUTPUT_DIR).
Standard library only, no network, deterministic.
"""

import os

LINE = "I don't need a bigger context window. I just need you in mine."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
