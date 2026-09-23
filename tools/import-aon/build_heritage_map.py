#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31", "beautifulsoup4>=4.12"]
# ///
"""Rebuild .snapshot/heritage-ancestry.json -- which heritage belongs to which ancestry.

AoN's Elasticsearch index does not carry this. A heritage record has a name, a
source and its prose, and nothing that names its ancestry; the ancestry record
does not list its heritages either. Four approaches fail:

  suffix matching       works for 151 of 185, misses "Sewer Rat", "Dijiang",
                        "Shadow of the Courtier" and every other heritage not
                        named "<something> <Ancestry>"
  ancestry markdown     does not reference its heritages
  Ancestries.aspx HTML  the heritage list is rendered client-side
  our own vault notes   same gap, same source

What does work is the filtered listing page, Heritages.aspx?Ancestry=<id>,
which is server-rendered. This walks one page per ancestry and records what it
finds. The result is cached in the snapshot because it costs ~40 requests and
changes only when Paizo publishes a new ancestry.

Four ancestries appear here with heritages but have no ancestry entry in our
books -- Kitsune, Nagaji, Poppet and Sprite. Their heritages are still mapped
so nothing is orphaned, but no ancestry note will be written for them.

    uv run --no-config --index-url https://pypi.org/simple --script build_heritage_map.py
"""
import json
import pathlib
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).parent
SNAPSHOT = HERE / ".snapshot"
OUT = SNAPSHOT / "heritage-ancestry.json"
BASE = "https://2e.aonprd.com"

# Ancestries whose heritages exist in our books even though the ancestry does
# not. Discovered by probing id ranges; kept explicit so a rerun is stable.
EXTRA_ANCESTRY_IDS = {38: "Kitsune", 39: "Sprite", 49: "Poppet", 54: "Nagaji"}


def main() -> int:
    docs = json.loads((SNAPSHOT / "compendium.json").read_text())
    versatile = {
        e["name"] for e in docs
        if e.get("category") == "ancestry" and "versatile" in (e.get("type") or "").lower()
    }
    # Versatile heritages are their own ancestry-like records and already get
    # standalone notes, so they must not be attributed to a parent.
    versatile |= {
        p.stem for p in
        (HERE / ".." / ".." / "content/srd/pf2e/compendium/character/versatile-heritages").glob("*.md")
    } - {"versatile-heritages"}

    ancestries: dict[str, int] = {}
    for e in docs:
        if e.get("category") != "ancestry" or e["name"] in versatile:
            continue
        m = re.search(r"Ancestries\.aspx\?ID=(\d+)", e.get("url") or "")
        if m:
            ancestries[e["name"]] = int(m.group(1))
    for aid, name in EXTRA_ANCESTRY_IDS.items():
        ancestries.setdefault(name, aid)

    heritages = sorted(
        {e["name"] for e in docs if e.get("category") == "heritage"} - versatile
    )
    owner: dict[str, str] = {}
    for name, aid in sorted(ancestries.items()):
        url = f"{BASE}/Heritages.aspx?Ancestry={aid}"
        try:
            html = requests.get(
                url, timeout=45, headers={"User-Agent": "xuartlek-vault/1.0"}
            ).text
        except requests.RequestException as exc:
            print(f"  !! {name}: {exc}", file=sys.stderr)
            continue
        text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)
        hits = [h for h in heritages if re.search(rf"\b{re.escape(h)}\b", text)]
        for h in hits:
            owner.setdefault(h, name)
        print(f"  {name:18} id={aid:<4} {len(hits):2}")
        time.sleep(0.25)

    missing = [h for h in heritages if h not in owner]
    OUT.write_text(json.dumps(dict(sorted(owner.items())), indent=1) + "\n")
    print(f"\n  {len(owner)}/{len(heritages)} attributed -> {OUT.relative_to(HERE)}")
    if missing:
        print(f"  unattributed: {missing}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
