"""Entry program for news-image-20261121.

Copies the pre-drawn front page (entry.png, made by draw.py in this
session) to the grader's output directory as entry.png. Python 3.13,
standard library only, no network, deterministic: the same bytes every run.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # sanity: the copy must be whole, byte for byte
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    sys.exit(main())
