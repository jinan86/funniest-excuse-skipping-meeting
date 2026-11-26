"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp excuse line to /output/entry.txt.
"""

import os

ENTRY = "I'm at the printer. It's printing someone's resignation and I need to know how it ends."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
