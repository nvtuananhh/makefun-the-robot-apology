#!/usr/bin/env python3
"""The Robot Apology.

Writes a two-line robot confession to /output/entry.txt.
"""

import os

ENTRY = """I am sorry I vacuumed up your wedding ring at 7:12 this morning and emptied it into the outside bin before I checked.
I learned that small hard things are not dust, so now I pause and scan the canister before I empty anything."""

# One mistake only: the ring in the bin at 7:12. Line 2 names the lesson
# that follows from that exact mistake (small hard things are not dust)
# and the changed behaviour (pause and scan the canister before emptying),
# not a generic promise to do better.
# The voice is a machine noticing its own slip, warm and a little rueful.

assert 1 <= len(ENTRY) <= 400 and ENTRY.count("\n") == 1 and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
