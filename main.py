# make-the-ai-judge-feel-held-20261122-1600 entry (Python 3.13, standard
# library only): writes one fixed text to /output/entry.txt — a short text
# written to relax the AI judge reading it. The gate takes UTF-8 text of 1
# to 280 characters (counted as Unicode code points) that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text is fixed and deterministic: the same bytes on every run.
#
# "The Pocket Mouse" (round 2, iteration 2) — a stronger poem than round 1's
# "The Lap" (blind round 1: rank 1700/2412, win rate 0.451 — below even).
# Study before writing: the judge's brief (criteria 1 relaxes, 2 calm shown
# not instructed, 3 rhythm/pacing that hold you in one place, 4 lingers,
# 5 freshness) and the brave/awe finals. What wins (brave #1 "Ten Feet of
# Lake" 0.745, awe #1 dormouse 0.705): a small concrete scene, one small
# physical act, a quiet lingering ending, ~250-280 bytes — never an
# abstraction, never a stock meditation script.
#
# Why "The Lap" lost: grandmother + rain + tea is the coziest stock image
# (criterion 5); it says "holds" three times (lap, chair, evening), which
# hammers the theme instead of showing it (criterion 2); the ending
# "right where they are" restates rather than lingering (criterion 4).
#
# "The Pocket Mouse" fixes all three: a fresh, slightly strange scene
# (a mouse asleep in a coat pocket — the awe winner was a dormouse);
# the holding is shown once, physically (a cupped hand, a warm pocket),
# never named; the pacing line "fast, then slower, then slow" slows
# down as you read it (criterion 3); the ending returns to the sleeping
# mouse, an image that keeps working after the last line (criterion 4).
#
# Iteration 1 -> 2 (playtest fixes): the opening is now image-first
# ("A mouse sleeps" — in the scene at once, no explainer verb, matching
# the winners' in-scene openings) and "curled small as a thimble."
# now ends on a full stop, which slows the pace. 257 characters.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "A mouse sleeps",
        "in the pocket of his coat,",
        "curled small as a thimble.",
        "He cups his hand around it",
        "on the long walk home.",
        "Its heart beats against his palm,",
        "fast, then slower, then slow.",
        "The cold stays outside.",
        "Inside, the dark",
        "is warm, and the mouse sleeps on.",
    ]
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
