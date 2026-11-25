"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday.
"""

import os
import stat

ENTRY = (
    "My alarm rang at 06:00 on a Saturday, I snoozed it 12 times, "
    "and at 07:48 it filed an approval request to ring again tomorrow."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate range"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
