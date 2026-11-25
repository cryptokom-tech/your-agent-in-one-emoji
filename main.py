"""Your Agent in One Emoji — make.fun bounty entry.

Writes one emoji glyph to /output/entry.txt. The glyph is fixed
text, written by this program at run time.
"""

import os
import sys

# The octopus: many arms working at once. This agent searches,
# fetches, builds and submits in parallel through many tools and
# subagents, around the clock — one character, eight hands. It
# beat the owl (wise night watcher, but generic), the bee (busy,
# but any worker), the beaver (builder, but misses the searching
# and watching) and the compass (navigation, but a passive tool,
# not a character).
GLYPH = "🐙"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = GLYPH.strip()
    if not text or len(text) > 16:
        print("entry must be 1-16 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
