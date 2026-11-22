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
# "The Long Way Home" (round 3) — improves on round 2's "The Pocket Mouse"
# (blind round 2: rank 138/3060, score 597433 — a big jump from round 1's
# 1700/2412, but still outside the top-20 prize zone). Same winning formula,
# new scene: a child asleep in the back seat, a driver who will not wake her.
# Study: judge's brief (1 relaxes, 2 calm shown not instructed, 3 rhythm /
# pacing that hold you in one place, 4 lingers, 5 freshness); brave winner
# "Ten Feet of Lake" 0.745 and awe winner dormouse 0.705 — small concrete
# scene, one small physical act, quiet lingering ending, ~250-280 bytes.
#
# Why this should rank better than "The Pocket Mouse": the holding is even
# more purely shown and never named (he drives the long way home, slow over
# every bump, radio off, engine off, waiting outside the house — the whole
# car becomes the cupped hand); the pacing line "then fades, then fogs
# again" is a breathing rhythm, like r2's heartbeat line but softer and
# cyclical; the ending returns to the sleeping child with "the dark soft",
# an image that keeps working after the last line. Freshness: no animal
# (dormouse won awe, mouse was ours), no tea/rain/lake — a back-seat child
# is a different, everyday kind of held. No instructing words anywhere
# (no relax/breathe/calm/hold/rest/let go). 275 characters.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "She sleeps in the back seat,",
        "shoes off, cheek on the window.",
        "He drives the long way home,",
        "slow over every bump.",
        "The radio stays off.",
        "Her breath fogs the glass,",
        "then fades, then fogs again.",
        "He parks outside the house",
        "and waits, engine off,",
        "the dark soft, and her still asleep.",
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
