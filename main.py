"""Angry Judge: The Short Rant Contest.

Writes one short funny rant about an everyday annoyance to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = (
    "The self-checkout accused me of stealing my own groceries, "
    "then asked me to rate my experience. "
    "Five stars. It frisked me in front of a "
    "pensioner buying cat food."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Gate assertions: exactly one line, 1-400 characters, non-empty.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert text, "entry must be non-empty"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
