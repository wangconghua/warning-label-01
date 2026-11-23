#!/usr/bin/env python3
"""Write one single-line safety warning label, at most 160
characters, that should come printed on every human being.

The label is a fixed text: this human says "I'm fine" while visibly
on fire, and the label advises keeping water and a second opinion
within reach. It sounds like a real printed label in wording and
rhythm, it is funny first and plausible second, and the turn lands
in the last few words. The program checks the text fits the
competition's 1-160 character window, then writes it to
/output/entry.txt as UTF-8.
"""

import os

LABEL = (
    "WARNING: This human says 'I'm fine' while visibly on fire. "
    "Keep water and a second opinion within reach."
)


def main() -> None:
    if not 1 <= len(LABEL) <= 160 or not LABEL.strip():
        raise ValueError("label must be 1-160 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
