"""Entry program for the make.fun bounty
"Sum up 24 November's world news in one image" (news-image-20261124).

The simplest valid program: it copies the image stored in this repository
to /output/entry.png. No network access, fully deterministic — every run
writes exactly the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
