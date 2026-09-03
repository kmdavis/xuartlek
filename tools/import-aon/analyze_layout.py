#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Count compendium entries along the axes we might split folders on.

Read-only. Produces the numbers needed to decide where a folder is worth
breaking up, and where a split would just create a pile of near-empty
directories.

Type comes from cssclasses (the "pf2e-<category>" entry), not from tags: a
trait/* tag is present both on trait entries and on every entry that merely
references that trait, so tags cannot identify what a note *is*.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

from books import CORE_FIVE

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> dict:
    """Minimal reader for the flat frontmatter this importer emits."""
    m = FM.match(text)
    if not m:
        return {}
    out: dict = {}
    key = None
    for line in m.group(1).split("\n"):
        if line.startswith("- ") and key:
            out.setdefault(key, []).append(line[2:].strip())
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            key = k.strip()
            v = v.strip()
            if v:
                out[key] = v.strip('"')
    return out


def load(folder: Path) -> list[dict]:
    rows = []
    for f in sorted(folder.rglob("*.md")):
        if f.name.startswith("_"):
            continue
        fm = parse_frontmatter(f.read_text(encoding="utf-8"))
        css = [c for c in fm.get("cssclasses", "").split(",") if c and c != "pf2e"]
        tags = fm.get("tags", [])
        rows.append({
            "path": f,
            "rel": f.relative_to(folder),
            "type": css[0] if css else "(none)",
            "source": fm.get("source", "(unknown)"),
            "traits": [t.split("/", 1)[1] for t in tags if t.startswith("trait/")],
            "level": next((t.rsplit("/", 1)[1] for t in tags if "/level/" in t), None),
        })
    return rows


def bar(n: int, total: int, width: int = 22) -> str:
    filled = round(width * n / total) if total else 0
    return "#" * filled


def table(title: str, counter: collections.Counter, total: int, limit: int = 30) -> None:
    print(f"\n  {title}  ({len(counter)} distinct)")
    for k, n in counter.most_common(limit):
        print(f"    {n:6d}  {100*n/total:5.1f}%  {bar(n,total):22}  {k}")
    if len(counter) > limit:
        rest = sum(n for _, n in counter.most_common()[limit:])
        print(f"    {rest:6d}  {100*rest/total:5.1f}%  {'':22}  ... {len(counter)-limit} more")


def crosstab(rows: list[dict], total: int, min_rows: int = 1) -> None:
    """Type x core/non-core, with the non-core books broken out."""
    core = {b.lower() for b in CORE_FIVE}
    by_type: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for r in rows:
        by_type[r["type"]][r["source"]] += 1
    print(f"\n  TYPE x SOURCE  (core = {', '.join(CORE_FIVE)})")
    for t, srcs in sorted(by_type.items(), key=lambda x: -sum(x[1].values())):
        tot = sum(srcs.values())
        if tot < min_rows:
            continue
        c = sum(n for s, n in srcs.items() if s.lower() in core)
        print(f"    {tot:6d}  {t:20}  core={c:<6} non-core={tot-c}")
        for s, n in srcs.most_common():
            if s.lower() not in core:
                print(f"            {n:6d}  ^ {s}")


def analyse(name: str, folder: Path, extras: list[str]) -> None:
    rows = load(folder)
    total = len(rows)
    print("\n" + "=" * 78)
    print(f"{name.upper()}   {total} entries   {folder}")
    print("=" * 78)
    if not total:
        return

    table("BY TYPE (cssclass)", collections.Counter(r["type"] for r in rows), total)
    table("BY SOURCEBOOK", collections.Counter(r["source"] for r in rows), total)
    crosstab(rows, total)

    if "level" in extras:
        lv = collections.Counter(r["level"] or "(none)" for r in rows)
        ordered = collections.Counter()
        for k in sorted(lv, key=lambda x: (x == "(none)", int(x) if x.isdigit() else 999)):
            ordered[k] = lv[k]
        print(f"\n  BY LEVEL  ({len(ordered)} distinct)")
        for k, n in ordered.items():
            print(f"    {n:6d}  {100*n/total:5.1f}%  {bar(n,total):22}  level {k}")

    if "consumable" in extras:
        con = collections.Counter(
            "consumable" if "consumable" in r["traits"] else "not consumable" for r in rows
        )
        table("BY CONSUMABLE TRAIT", con, total)

    if "traits" in extras:
        tr = collections.Counter(t for r in rows for t in r["traits"])
        table("BY TRAIT (most common)", tr, total, limit=25)
        notrait = sum(1 for r in rows if not r["traits"])
        print(f"    {notrait:6d}  {100*notrait/total:5.1f}%  {'':22}  (entries with no trait tag)")

    deep = collections.Counter(str(r["rel"].parent) for r in rows)
    if len(deep) > 1:
        table("EXISTING SUBFOLDERS", deep, total, limit=12)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    default = Path(__file__).resolve().parents[2] / "content" / "srd" / "pf2e-remaster" / "compendium"
    ap.add_argument("--root", type=Path, default=default)
    ap.add_argument("--only", nargs="+", help="limit to these folders")
    args = ap.parse_args()

    plan = {
        "rules-elements": [],
        "gm": [],
        "character": [],
        "feats": ["level", "traits"],
        "equipment": ["level", "consumable"],
        "spells": ["level"],
    }
    for name, extras in plan.items():
        if args.only and name not in args.only:
            continue
        folder = args.root / name
        if folder.exists():
            analyse(name, folder, extras)
        else:
            print(f"  missing: {folder}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
