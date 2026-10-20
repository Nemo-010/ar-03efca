#!/usr/bin/env python3
"""Print the exact sentence(s) matching a regex, per snapshot file.

Usage: python3 scripts/grab.py <slug> <regex> [max]
Prints "<file>\t<sentence>" so a quote can be copied verbatim into facts.py.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP = os.path.join(ROOT, "data", "snapshots")

slug, pat = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 6
rx = re.compile(pat, re.I)
n = 0
for f in sorted(glob.glob(os.path.join(SNAP, slug, "*.txt"))):
    txt = re.sub(r"\s+", " ", open(f, encoding="utf-8", errors="replace").read())
    for s in re.split(r"(?<=[.!?])\s+", txt):
        if rx.search(s):
            print(f"{os.path.basename(f)[:-4]}\t{s.strip()[:400]}")
            n += 1
            if n >= mx:
                sys.exit()
