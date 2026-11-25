#!/usr/bin/env python3
"""Make the AI Judge Laugh (rama-melon) — make.fun bounty entry.

Writes one joke about office life to /output/entry.txt. Run with
``python3 main.py`` (no arguments, no dependencies beyond the standard
library); the entry is the exact 99-character text in ``ENTRY`` and is
written verbatim, with no trailing newline.

The joke: a standing desk request answered with a meeting where you stand
and present everyone else's work — a true office observation (the ask for
better equipment, the meeting that eats your time, the credit going
elsewhere) with a surprise turn on the word "standing", kept to one tight
line that reads aloud in a single breath.
"""

import os

ENTRY = (
    "I asked for a standing desk. They gave me a meeting where I stand "
    "and present everyone else's work."
)


def main() -> None:
    if not ENTRY or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single non-empty line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
