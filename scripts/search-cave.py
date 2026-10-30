#!/usr/bin/env python3
"""search-cave.py - search the Crystal Cave the way Jim thinks: by story, not filename.

Indexes every Markdown file and every session-record JSON (story layer,
attribution, transcript) and answers queries against all of them.

Usage:
  ./scripts/search-cave.py "suno"                 # full-text across the cave
  ./scripts/search-cave.py "triad" --md-only      # prose only
  ./scripts/search-cave.py "weaver" --sessions-only
  ./scripts/search-cave.py --by-arm gemini        # everything attributed to an arm
  ./scripts/search-cave.py --list-arms            # known arms/attribution names
  ./scripts/search-cave.py "cave" --context 3     # show N lines of context

Exit codes: 0 = matches found, 1 = none, 2 = usage error.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SESSIONS_DIR = REPO_ROOT / "sessions"
ARTIFACTS_DIR = REPO_ROOT / "artifacts"

def flatten_json(obj, out):
    """Recursively flatten any JSON structure into searchable text."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.append(str(k))
            flatten_json(v, out)
    elif isinstance(obj, list):
        for item in obj:
            flatten_json(item, out)
    elif obj is not None:
        out.append(str(obj))


def iter_md_files():
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in path.parts or "obsidian-native-git-bridge" in str(path):
            continue
        yield path


def iter_session_records():
    if not SESSIONS_DIR.is_dir():
        return
    for path in sorted(SESSIONS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        yield path, data


def session_text(path, data):
    """Flatten a session JSON into searchable text, keeping key/provenance labels."""
    parts = []
    flatten_json(data, parts)
    return "\n".join(parts)


def collect_docs():
    docs = []  # (source_label, path, text)
    for path in iter_md_files():
        try:
            docs.append(("md", path, path.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            pass
    for path, data in iter_session_records():
        docs.append(("session", path, session_text(path, data)))
    return docs


def main():
    ap = argparse.ArgumentParser(description="Search the Crystal Cave by story, not filename.")
    ap.add_argument("query", nargs="?", help="Text to search for (case-insensitive).")
    ap.add_argument("--md-only", action="store_true", help="Search Markdown prose only.")
    ap.add_argument("--sessions-only", action="store_true", help="Search session records only.")
    ap.add_argument("--by-arm", metavar="ARM", help="Show docs attributed to this arm (e.g. gemini, gboard, suno).")
    ap.add_argument("--list-arms", action="store_true", help="List attribution names found in session records.")
    ap.add_argument("--context", type=int, default=2, metavar="N", help="Lines of context per hit (default 2).")
    args = ap.parse_args()

    docs = collect_docs()

    if args.list_arms:
        arms = set()
        for path, data in iter_session_records():
            text = session_text(path, data)
            for m in re.finditer(r"(?i)(?:attribut\w*|by|credit\w*)[:\s]+([^\n]{3,120})", text):
                arms.update(a.strip(" .,:;") for a in re.split(r"[,;+/]|\band\b", m.group(1)) if a.strip(" .,:;"))
        for a in sorted(arms, key=str.lower):
            print(a)
        return 0

    if not args.query and not args.by_arm:
        ap.error("provide a query, --by-arm, or --list-arms")

    needle = re.compile(re.escape(args.query), re.IGNORECASE) if args.query else None
    arm_needle = re.compile(re.escape(args.by_arm), re.IGNORECASE) if args.by_arm else None

    hits = 0
    for kind, path, text in docs:
        if args.md_only and kind != "md":
            continue
        if args.sessions_only and kind != "session":
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            line_hit = needle.search(line) if needle else None
            arm_hit = arm_needle.search(line) if arm_needle else None
            if (needle and line_hit) or (arm_needle and arm_hit):
                hits += 1
                rel = path.relative_to(REPO_ROOT)
                lo = max(0, i - args.context)
                hi = min(len(lines), i + args.context + 1)
                print(f"\n== {rel} (line {i + 1}) ==")
                for j in range(lo, hi):
                    marker = ">>" if j == i else "  "
                    print(f"{marker} {lines[j]}")
                break  # one hit block per file is enough; rerun with narrower query for more

    if hits == 0:
        print("No matches.", file=sys.stderr)
        return 1
    print(f"\n{hits} file(s) matched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
