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
# "The Lap" (iteration round 2) — one revision after a criteria
# playtest against the judge's brief. v1's "She does not move." only
# restated the stillness; v2 replaces it with "The tea goes cold. She
# does not mind.": a small sacrifice that SHOWS she chooses to stay
# (criterion 2 — calm from the text, not from instruction), and the
# cold tea is a fresh, concrete detail (criterion 5). "His head is
# heavy in her lap" — "in" not "on": the lap encloses, it holds.
# The holding motif now runs three deep: lap, chair, evening. 277 chars.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "She sets the kettle down and stays.",
        "Rain keeps time on the tin roof.",
        "His head is heavy in her lap,",
        "his breathing slow against her knee.",
        "The tea goes cold. She does not mind.",
        "The chair holds them both.",
        "Outside, the rain goes on,",
        "and the evening holds them",
        "right where they are.",
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
