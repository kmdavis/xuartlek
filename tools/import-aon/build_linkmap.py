#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31", "beautifulsoup4>=4.12"]
# ///
"""
Precompute where every entry will land, so links can be resolved on the first
generation pass.

Destinations are pure functions of the snapshot, so they can be worked out
without writing anything. That avoids a chicken-and-egg problem: a note cannot
link to a page whose path is only decided while writing that page.

Run this before the importers. It writes .snapshot/linkmap.json.
"""

from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import import_bestiary as bes
import import_compendium as comp
from books import ALL_BOOKS
from linkmap import LinkMap

HERE = Path(__file__).parent
VAULT = HERE.parents[1] / "content"
ROOT = VAULT / "srd" / "pf2e"


def main() -> int:
    lm = LinkMap(VAULT)
    snap = HERE / ".snapshot"

    # -- compendium ------------------------------------------------------
    docs = json.loads((snap / "compendium.json").read_text())
    live = [d for d in docs if not comp.superseded(d)]
    class_index = comp.build_class_index(docs)
    counts = collections.Counter(d.get("category", "") for d in live)
    for d in live:
        srcs = [s.strip() for s in (d.get("source") or [])]
        d["__source__"] = next((s for s in srcs if s.lower() in comp.BOOK_ABBR),
                               srcs[0] if srcs else "")

    # Consolidated entries are gathered first: a page is only split once the
    # size of the whole group is known, and the split has to match what the
    # importer will do.
    grouped: dict[Path, list[dict]] = {}
    standalone: list[tuple[dict, Path]] = []
    seen: set[Path] = set()
    for d in live:
        path, page_cat = comp.destination(d, ROOT / "compendium", class_index, counts)
        d["__name__"] = comp.detemplate(d.get("name", ""))
        if page_cat:
            grouped.setdefault(path, []).append(d)
        else:
            if path in seen:
                suffix = comp.slugify(str(d.get("id", ""))) or "dup"
                path = path.with_name(f"{path.stem}-{suffix}.md")
            seen.add(path)
            standalone.append((d, path))

    for d, path in standalone:
        lm.add(d.get("category", ""), d.get("id", ""), path, name=d["__name__"])

    shards = 0
    for path, entries in grouped.items():
        mapping = comp.shard_paths(path, [e["__name__"] for e in entries])
        shards += len(set(mapping.values()))
        for d in entries:
            final = mapping[d["__name__"]]
            lm.add(d.get("category", ""), d.get("id", ""), final,
                   anchor=d["__name__"], name=d["__name__"])
    print(f"  compendium: {len(live)} entries "
          f"({len(standalone)} notes, {sum(len(v) for v in grouped.values())} "
          f"sections across {shards} pages)")

    # -- bestiary --------------------------------------------------------
    creatures, _dropped = bes.dedupe(json.loads((snap / "creatures.json").read_text()))
    for c in creatures:
        path = (ROOT / "bestiary" / bes.book_slug(c) / bes.creature_type(c)
                / f"{bes.slugify(c['name'])}.md")
        lm.add_creature(c.get("id", ""), path)
    print(f"  bestiary:   {len(creatures)} creatures")

    # -- rules -----------------------------------------------------------
    # Reuse the importer's own index parse and path assignment.
    import import_aon as rules
    fetcher = rules.Fetcher(HERE / ".cache", delay=0.0, refresh=False)
    index_html = fetcher.get(rules.INDEX_URL, "index")
    entries = rules.parse_index(index_html, ALL_BOOKS)
    rules.assign_paths(entries, ROOT / "books")
    own = {e.aon_id for e in entries}
    for e in entries:
        lm.add_rule(e.aon_id, e.path)
    # Subsections resolve to an anchor on their parent page.
    subs = 0
    for e in entries:
        try:
            page = fetcher.get(f"{rules.BASE}/Rules.aspx?ID={e.aon_id}&NoRedirect=1", str(e.aon_id))
        except Exception:
            continue
        rule = rules.rule_body(page)
        if rule is None:
            continue
        heads: dict[int, str] = {}
        rules.collect_headings(rule, heads, own)
        for hid, text in heads.items():
            if hid not in own:
                lm.add_rule(hid, e.path, anchor=text)
                subs += 1
    print(f"  rules:      {len(entries)} sections + {subs} subsections")

    out = snap / "linkmap.json"
    lm.save(out)
    print(f"\nWrote {len(lm)} link targets -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
