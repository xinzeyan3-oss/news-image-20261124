#!/usr/bin/env python3
"""Copy the bundled entry image to /output/entry.png.

Deterministic: no network, no randomness, no timestamps.
Running this program any number of times produces byte-identical output.
"""

import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    target = Path("/output/entry.png")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
