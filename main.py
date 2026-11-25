"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office reply line to entry.txt.

Candidate lines weighed against the judge brief (most important first:
real one-line away message; laugh lands on first read; reads like a
genuine away message; fresh turn, no beach / inbox / limited-email
cliches; short, every word earning its place):

1. "Gone fishing for my own attention span -- back when I find it."
   Beach/fishing cliche the brief explicitly warns against; also
   needs a beat to land. Rejected.

2. "Your email has been received and immediately ignored in a much
   nicer location."  Snarky but long, and "nicer location" is the
   same holiday cliche in disguise. Rejected.

3. "Gone. My out-of-office reply is the only thing in this company
   working remotely."  Meta and fresh, but two beats and the joke
   is about the company, not the absence. Runner-up.

4. "I'm out of the office, which is the closest thing to a promotion
   I've had all year."  Lands well, but it is a joke about work, not
   an away message -- it reads like a notice with a joke bolted on.
   Runner-up.

5. "I'm on annual leave, which is corporate for 'please stop'."
   CHOSEN. It is a real away message a person would gladly switch
   on; the laugh lands on the first read ("corporate for 'please
   stop'" reframes the whole sentence in three words); the turn is
   fresh -- corporate-speak itself is the joke, not a beach or an
   inbox; and at 58 characters it is taken in at a glance. It stands
   alone with no signature or name needed.
   Standalone guard: main() enforces the same gate the sealed scorer
   checks -- 1 to 160 characters, single line, not only whitespace --
   and raises instead of writing an invalid entry.
"""

import os

ENTRY = "I'm on annual leave, which is corporate for 'please stop'."


def main():
    # Gate guard: mirror the sealed scorer (1-160 chars, one line,
    # not only whitespace) so an invalid entry is never written.
    if not (1 <= len(ENTRY) <= 160):
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-160")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
