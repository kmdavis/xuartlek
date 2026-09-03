#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31"]
# ///
"""
Phase 0 audit: snapshot every Remaster creature from AoN's Elasticsearch index
and measure how much its markdown actually varies.

The statblock mapping was inferred from a single well-behaved creature. Before
writing a mapper for all of them, check that assumption against the whole set:
how many horizontal-rule-delimited blocks each creature has, which section
labels appear, and which constructs (spellcasting, auras, troops, swarms) will
need special handling.

Writes a raw snapshot so generation never depends on a live endpoint.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import requests

from books import ES_KEYS

ES = "https://elasticsearch.aonprd.com/aon/_search"
CORE_BOOKS = ES_KEYS


def fetch_all(category: str, books: list[str], page: int = 250) -> list[dict]:
    """Page with from/size. Every category here is far below the 10k window."""
    out: list[dict] = []
    offset = 0
    while True:
        body = {
            "size": page,
            "from": offset,
            "query": {"bool": {"filter": [
                {"term": {"category": category}},
                {"terms": {"source.keyword": books}},
            ]}},
        }
        r = requests.post(ES, json=body, timeout=60)
        r.raise_for_status()
        payload = r.json()
        hits = payload["hits"]["hits"]
        if not hits:
            break
        out.extend(h["_source"] for h in hits)
        offset += len(hits)
        total = payload["hits"]["total"]["value"]
        print(f"  fetched {len(out)}/{total}", file=sys.stderr)
        if offset >= total:
            break
    return out


# A "**Label**" at the start of a line is how AoN marks statblock fields.
LABEL = re.compile(r"^\*\*([A-Z][A-Za-z /'-]{1,34})\*\*", re.M)


def statblock_region(md: str) -> str:
    """Everything from the Creature-N title onward, i.e. the statblock proper."""
    m = re.search(r'<title level="2"[^>]*right="[^"]*"[^>]*>', md)
    return md[m.end():] if m else md


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path(__file__).parent / ".snapshot")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    raw = args.out / "creatures.json"

    if raw.exists() and not args.refresh:
        creatures = json.loads(raw.read_text())
        print(f"Loaded {len(creatures)} creatures from snapshot")
    else:
        print("Fetching creatures from Elasticsearch...")
        creatures = fetch_all("creature", CORE_BOOKS)
        raw.write_text(json.dumps(creatures, indent=1))
        print(f"Snapshotted {len(creatures)} creatures -> {raw}")

    hr_counts = collections.Counter()
    labels_by_block = collections.defaultdict(collections.Counter)
    all_labels = collections.Counter()
    tags = collections.Counter()
    features = collections.Counter()
    by_book = collections.Counter()
    anomalies: list[tuple[str, str]] = []

    for c in creatures:
        name = c.get("name", "?")
        for s in c.get("source", []):
            by_book[s.strip()] += 1
        md = c.get("markdown", "")
        sb = statblock_region(md)

        for t in re.findall(r"<(\w+)", md):
            tags[t] += 1

        blocks = re.split(r"^---$", sb, flags=re.M)
        hr_counts[len(blocks)] += 1
        if len(blocks) != 3:
            anomalies.append((name, f"{len(blocks)} blocks"))

        for i, b in enumerate(blocks):
            for lab in LABEL.findall(b):
                labels_by_block[i][lab] += 1
                all_labels[lab] += 1

        low = sb.lower()
        if "spells**" in low or "spell dc" in low:
            features["spellcasting"] += 1
        if "**ritual" in low:
            features["rituals"] += 1
        if re.search(r"\*\*[^*]*aura[^*]*\*\*", low):
            features["aura"] += 1
        if "regeneration" in low:
            features["regeneration"] += 1
        if "fast healing" in low:
            features["fast healing"] += 1
        if "troop" in [t.lower() for t in c.get("trait", [])]:
            features["troop trait"] += 1
        if "swarm" in [t.lower() for t in c.get("trait", [])]:
            features["swarm trait"] += 1
        if not c.get("hp"):
            features["NO hp field"] += 1
        if not c.get("ac"):
            features["NO ac field"] += 1
        if "<table" in md:
            features["contains table"] += 1
        if len(c.get("source", [])) > 1:
            features["multiple sources"] += 1

    print(f"\n{'='*66}\nCREATURES: {len(creatures)}\n{'='*66}")
    print("--- by book ---")
    for b, n in by_book.most_common():
        print(f"  {n:5d}  {b}")

    print("\n--- statblock blocks split on '---' (expected 3) ---")
    for n, count in sorted(hr_counts.items()):
        flag = "  <-- expected" if n == 3 else "  <-- DEVIATION"
        print(f"  {n} blocks: {count:5d} creatures{flag}")

    print("\n--- field labels per block ---")
    for i in sorted(labels_by_block):
        top = labels_by_block[i].most_common(14)
        print(f"  BLOCK {i}: " + ", ".join(f"{k}({v})" for k, v in top))

    print("\n--- labels appearing in more than one block (ambiguous) ---")
    for lab, total in all_labels.most_common():
        blocks_seen = [i for i in labels_by_block if lab in labels_by_block[i]]
        if len(blocks_seen) > 1 and total > 5:
            dist = ", ".join(f"b{i}={labels_by_block[i][lab]}" for i in blocks_seen)
            print(f"  {lab:26} {total:5d}  ({dist})")

    print("\n--- constructs needing special handling ---")
    for k, n in features.most_common():
        print(f"  {n:5d}  {k}")

    print("\n--- AoN markup tags ---")
    print("  " + ", ".join(f"{k}({v})" for k, v in tags.most_common(12)))

    if anomalies:
        print(f"\n--- {len(anomalies)} creatures deviating from the 3-block shape (first 15) ---")
        for name, why in anomalies[:15]:
            print(f"  {why:12} {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
