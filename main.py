"""One-Line Laugh-Off entry.

Writes a single funny line to /output/entry.txt, exactly as the
competition harness expects. No network, no secrets, no input files.

The line is checked against the competition gate before it is written:
UTF-8 text, 1 to 200 characters, not only white space. If it ever
failed that check the program would refuse to write anything, so a
bad entry can never be submitted silently.
"""

import os
from pathlib import Path

JOKE = "My Roomba left me for the vacuum cleaner. Its note said: 'He sucks, but at least he means it.'"

OUTPUT = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} characters, gate needs 1-200")
    if not line.strip():
        raise SystemExit("entry is only white space")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
