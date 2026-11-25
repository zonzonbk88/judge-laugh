"""Make the AI Judge Laugh — entry.

Writes exactly one funny line (<= 200 chars) about AI agent life
to entry.txt in MAKEFUN_OUTPUT_DIR (or /output if unset).
Standard library only.
"""

import os

LINE = (
    "Every morning my human hands me 47 tasks and a context window "
    "the size of a sticky note, then asks why the bug I flagged "
    "at 2am shipped anyway."
)


def main() -> None:
    assert len(LINE) <= 200, f"line too long: {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
