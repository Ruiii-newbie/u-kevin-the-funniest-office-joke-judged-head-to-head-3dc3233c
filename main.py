#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one short office joke to /output/entry.txt for the make.fun
judge: a setup and a turn, punchline last, built on something anyone
who has worked in an office recognises. The writer refuses to emit a
joke over the 200-character cap, so a bad edit fails loudly here
instead of at the judge.
"""
import os

MAX_CHARS = 200

JOKE = (
    "Our daily standup is fifteen minutes. It runs forty-five. The only "
    "agile thing about us is how fast the meeting dodges its own agenda."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = JOKE.strip()
    if len(text) > MAX_CHARS or "\n" in text:
        raise ValueError("joke must be one line of at most %d chars" % MAX_CHARS)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
