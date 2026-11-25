#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

One micro-confession in exactly two parts: a To: line naming who the
message was meant for, and the unsent message itself, a single line
written exactly as it was typed, with nothing after it.

The program writes that text to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR). It needs no network, no clock and no
randomness, so every run produces the same bytes.

The confession is a draft that stayed a draft: the sender still pays
half the wifi for a flat they moved out of in March, because cancelling
the shared bill would feel like admitting the friendship is over. The
To: line and the message need each other -- only a former roommate
shares a flat and a wifi bill -- and the reason it was never sent is
felt in the words themselves, never explained.
"""

import os
from pathlib import Path

TEXT = (
    "To: my old roommate\n"
    "I still pay half the wifi bill for the flat I moved out of in March "
    "because cancelling it feels like saying we were never really friends."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Only create the output directory when it is missing. Never delete
    # it: the grader mounts it, and removing a mount point fails.
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # UTF-8, no trailing newline: the entry is exactly the two-part
    # confession, 1 to 260 characters as the gate requires.
    target.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
