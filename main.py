#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt. Standard library only, no
network. The line must be 1-200 characters and not only whitespace.
"""

import os

LINE = "My confidence was 99.7%. My accuracy was the other 0.3%."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()

    # Gate rules: one line, 1-200 characters, not only whitespace.
    if not line:
        raise SystemExit("error: entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("error: entry line must be a single line")
    if len(line) > 200:
        raise SystemExit(
            f"error: entry line is {len(line)} chars, over the 200-char limit"
        )
    if len(line.encode("utf-8")) > 200:
        raise SystemExit("error: entry line is over 200 bytes")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Re-read the file and verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")

    if written != line:
        raise SystemExit("error: verification failed, file content does not match")
    if not (1 <= len(written) <= 200) or not written.strip():
        raise SystemExit("error: verification failed, entry is not 1-200 non-blank chars")

    print(f"OK: wrote {len(written)} chars to {OUTPUT_PATH}")
    print(f"entry: {written}")


if __name__ == "__main__":
    main()
