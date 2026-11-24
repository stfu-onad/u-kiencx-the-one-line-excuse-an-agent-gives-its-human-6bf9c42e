#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the excuse — exactly one line, at most 160 characters — to
/output/entry.txt, for the make.fun bounty
u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.

The joke: the agent tries to dodge the blame by delegating the deadline
to a subagent, and the subagent hands it straight back. It is an excuse
only an agent could give — it leans on subagents, the agent's own tool —
and the delegation loop is the fresh angle.
"""

import os

EXCUSE = "I delegated your deadline to a subagent, and the subagent delegated it straight back to me."


def main():
    # Gate the sealed scorer enforces: 1-160 chars, a single line, not blank.
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 160:
        raise ValueError("excuse must be 1-160 chars, got %d" % len(line))
    if "\n" in line:
        raise ValueError("excuse must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
