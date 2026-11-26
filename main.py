"""Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes a single razor-sharp excuse line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

EXCUSE = (
    "I'm at the printer. "
    "It's printing someone's resignation "
    "and I need to know how it ends."
)


def build_entry() -> str:
    """Return the excuse as one single line.

    The joke: a resignation printing at the office printer is treated
    like a TV finale — you cannot walk away before finding out how it ends.
    """
    return EXCUSE


def validate(entry: str) -> None:
    """Gate check: one line, 1-200 chars, not only whitespace."""
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} chars, over the 200 limit")


def main() -> None:
    entry = build_entry()
    validate(entry)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")
    print(entry)


if __name__ == "__main__":
    main()
