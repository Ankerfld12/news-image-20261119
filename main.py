#!/usr/bin/env python3
"""news-image-20261119 entrypoint.

Copies the pre-rendered poster in assets/entry.png to the output
directory as entry.png. Standard library only, no network, and the
same bytes are written on every run.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "assets", "entry.png")
    if not os.path.isfile(source):
        print("missing poster: %s" % source, file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))


if __name__ == "__main__":
    main()
