#!/usr/bin/env python3
"""drive-index.py - build a searchable manifest of the Crystal Cave material in Google Drive.

Uses the google_drive_mcp connector tools when run inside a Vibe session
(via the agent), or reads a previously exported manifest JSON. Locally it
can also ingest an exported Takeout folder (Keep notes land there as
Takeout/Keep/*.html + *.json).

Usage:
  python3 scripts/drive-index.py --from-manifest drive-manifest.json --query suno
  python3 scripts/drive-index.py --from-takeout /path/to/Takeout --query gardener
  python3 scripts/drive-index.py --write-manifest cave-drive-index.json   # run by agent with Drive tools
"""
import argparse, json, re, sys
from pathlib import Path

def load_manifest(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("files", [])

def load_takeout(path):
    root = Path(path)
    docs = []
    for f in root.rglob("*"):
        if f.suffix.lower() in (".html", ".json", ".md", ".txt"):
            try:
                docs.append({"title": str(f.relative_to(root)), "source": "takeout", "content": f.read_text(encoding="utf-8", errors="replace")})
            except OSError:
                pass
    return docs

def search(docs, needle, needle_re=None):
    pat = re.compile(needle_re or re.escape(needle), re.IGNORECASE)
    hits = 0
    for d in docs:
        blob = d.get("title", "") + "\n" + (d.get("content") or d.get("fullText", ""))
        if pat.search(blob):
            hits += 1
            print(f"\n== {d.get('title')} ==")
            m = pat.search(blob)
            start = max(0, m.start() - 120)
            print(blob[start:m.end() + 120].replace("\n", " | "))
    print(f"\n{hits} item(s) matched.")
    return 0 if hits else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-manifest")
    ap.add_argument("--from-takeout")
    ap.add_argument("--query")
    args = ap.parse_args()
    if args.from_manifest:
        docs = load_manifest(args.from_manifest)
    elif args.from_takeout:
        docs = load_takeout(args.from_takeout)
    else:
        ap.error("provide --from-manifest or --from-takeout")
    if not args.query:
        ap.error("provide --query")
    return search(docs, args.query)

if __name__ == "__main__":
    sys.exit(main())
