#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes one line, the Moon's reply at last to the wishes, howls and
late-night promises of everyone staring up at it, to
/output/entry.txt (1-240 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The line is built from three fragments: the opening (four billion
years of night shifts), the charge (billing overtime), and the
complaint (the howling is a noise complaint). ``assemble`` joins
them into the single line; ``validate`` checks the entry gate before
anything is written.
"""

from pathlib import Path

OPENING = "After four billion years of night shifts,"
CHARGE = "I'm billing overtime"
COMPLAINT = "and the howling is a noise complaint."
SEPARATOR = " \u2014 "  # em dash, spaced, joins charge to complaint

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(opening: str, charge: str, complaint: str, separator: str) -> str:
    """Join the three fragments into one comeback line."""
    parts = [opening, charge]
    return " ".join(parts) + separator + complaint


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-240 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 240:
        raise ValueError(f"line must be 1-240 characters, got {len(line)}")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("line must not contain control characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(OPENING, CHARGE, COMPLAINT, SEPARATOR))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
