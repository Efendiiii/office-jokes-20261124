#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line joke about office life (under 200 characters)
to /output/entry.txt, exactly as the program/v1 harness requires.

Deterministic: the same text on every run, so the two grading runs
agree byte for byte. Standard library only, no network.
"""

import os

JOKE = "My calendar blocked 'focus time' from 9 to 5, so my manager booked a meeting called 'Focus Time Sync' to discuss it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Fail loudly instead of ever writing an entry the gate rejects:
    # one line, 1 to 199 characters, not only white space.
    if not 1 <= len(JOKE) <= 199:
        raise ValueError(f"joke is {len(JOKE)} characters, gate needs 1-199")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
