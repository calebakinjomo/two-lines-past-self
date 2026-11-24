#!/usr/bin/env python3
"""Two Lines to Your Past Self -- make.fun bounty entry.

Prints two lines addressed to my past self and writes them to
/output/entry.txt for the harness. The two lines total 211 characters,
within the 1-280 character gate for the entry.
"""

import os

LINE_1 = "At 2 a.m. the night before the demo, don't delete the working version to rewrite it the clever way."
LINE_2 = "The clever version froze on stage in front of everyone, and the version you threw away was the one that worked."

ENTRY = LINE_1 + "\n" + LINE_2


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
