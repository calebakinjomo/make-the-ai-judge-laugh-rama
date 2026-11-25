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


MAX_ENTRY_CHARS = 280


def main() -> None:
    if not ENTRY or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single non-empty line")
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError("ENTRY exceeds the %d-character limit" % MAX_ENTRY_CHARS)
    if ENTRY != ENTRY.strip():
        raise ValueError("ENTRY must not have leading or trailing whitespace")
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
