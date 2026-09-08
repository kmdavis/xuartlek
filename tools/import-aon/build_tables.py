#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31", "beautifulsoup4>=4.12"]
# ///
"""
Build content/srd/pf2e/tables/ from the hand-picked legacy tables.

These 16 tables have no Remaster successor but are still valid at the table,
so they are kept and re-homed. Everything else that used to live in
archive/srd/pf2e/rules/tables was either superseded by the Remaster import or
belonged to an adventure, and has been deleted.

Deliberately a sibling of books/, bestiary/ and compendium/ rather than a
folder inside one of them. Regenerating the SRD means deleting those three
directories wholesale, so anything hand-maintained inside them would not
survive. Nothing here comes from the importers.

Three of the tables are Gamemastery Guide variant rules that the Remaster left
behind. AoN still publishes their explanatory text, which is fetched and put
back so each table says how to use it rather than sitting there contextless.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

HERE = Path(__file__).parent
SRC = HERE.parents[1] / "archive" / "srd" / "pf2e" / "rules" / "tables"
OUT = HERE.parents[1] / "content" / "srd" / "pf2e" / "tables"
AON = "https://2e.aonprd.com"

# file stem -> (destination group, title, AoN rules page supplying the prose)
TABLES: dict[str, tuple[str, str, int | None]] = {
    "critical-hit-deck-bludgeoning-chd":  ("decks", "Critical Hit Deck: Bludgeoning", None),
    "critical-hit-deck-piercing-chd":     ("decks", "Critical Hit Deck: Piercing", None),
    "critical-hit-deck-slashing-chd":     ("decks", "Critical Hit Deck: Slashing", None),
    "critical-hit-deck-bomb-or-spell-chd": ("decks", "Critical Hit Deck: Bomb or Spell", None),
    "critical-fumble-deck-melee-cfd":     ("decks", "Critical Fumble Deck: Melee", None),
    "critical-fumble-deck-ranged-cfd":    ("decks", "Critical Fumble Deck: Ranged", None),
    "critical-fumble-deck-unarmed-cfd":   ("decks", "Critical Fumble Deck: Unarmed", None),
    "critical-fumble-deck-spell-cfd":     ("decks", "Critical Fumble Deck: Spell", None),
    "hero-point-deck-hpd":                ("decks", "Hero Point Deck", None),
    "housing-costs-lotg":                 ("economy", "Housing Costs", None),
    "animal-prices-lotg":                 ("economy", "Animal Prices", None),
    "animal-caretaking-gear-prices-lotg": ("economy", "Animal Caretaking Gear Prices", None),
    "common-crimes-and-punishments-lotg": ("economy", "Common Crimes and Punishments", None),
    "resilient-armor-gmg":                ("variant-rules", "Resilient Armor", 1368),
    "devastating-weapons-gmg":            ("variant-rules", "Devastating Weapons", 1368),
    # AoN renamed this to Item Quirks, to distinguish it from Dark Archive's
    # own Quirks table.
    "quirks-gmg":                         ("variant-rules", "Item Quirks", 1083),
}

RENAME = {"quirks-gmg": "item-quirks"}

GROUP_NOTE = {
    "decks": "Paizo accessory decks. Each row is a card face; draw or roll instead of "
             "applying the standard critical effect.",
    "economy": "Prices and social consequences from the Lost Omens Travel Guide. "
               "Nothing in the Remaster replaces these.",
    "variant-rules": "Optional Gamemastery Guide subsystems. The Remaster did not carry "
                     "them into GM Core, but Paizo still treats them as valid; each "
                     "carries its explanatory text from Archives of Nethys.",
}


def fetch_prose(session: requests.Session, rule_id: int) -> tuple[str, str]:
    """Explanatory paragraphs and the citation from an AoN rules page."""
    r = session.get(f"{AON}/Rules.aspx?ID={rule_id}&NoRedirect=1", timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    main = soup.select_one("#main")
    if main is None:
        return "", ""
    for tag in main.select("table, nav, script, style"):
        tag.decompose()
    text = main.get_text("\n")
    # Prose sits between the "Source <book> pg. N" line and the first table,
    # which has already been removed above.
    m = re.search(r"Source\s*\n+\s*(.+?pg\.\s*\d+)", text)
    if not m:
        return "", ""
    citation = m.group(1).strip()
    paras = []
    for line in text[m.end():].split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if len(line) > 40:
            paras.append(line)
        elif paras and len(paras) >= 1 and line.startswith(("Source", "Chapter")):
            break
    return "\n\n".join(paras[:6]), citation


def convert(path: Path, title: str, group: str, prose: str, citation: str) -> str:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    body = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.S)
    body = re.sub(r"^#\s+.*?\n", "", body, count=1)
    legacy_cite = ""
    m = re.search(r"^\*Source: (.+?)\*\s*$", body, re.M)
    if m:
        legacy_cite = m.group(1).strip()
        body = body[:m.start()] + body[m.end():]
    # Legacy links point into the deleted archive tree; drop them to plain text.
    body = re.sub(r"\[([^\]]+)\]\((?:archive|content)/[^)]*\)", r"\1", body)
    body = re.sub(r"\[([^\]]+)\]\([^)]*\.md[^)]*\)", r"\1", body)
    body = re.sub(r"\n\^[a-z0-9-]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    slug = RENAME.get(path.stem, path.stem)
    slug = re.sub(r"-(?:cfd|chd|hpd|lotg|gmg|roe|da|som)$", "", slug)
    head = [
        "---",
        "cssclasses: pf2e,pf2e-table",
        "tags:",
        f"- table/{group}",
        f'aliases: ["{title}"]',
        f'source: "{legacy_cite or citation}"',
    ]
    if citation:
        head.append(f'aon_url: "{AON}/Rules.aspx?ID={RULE_OF[path.stem]}"')
    head += ["---", "", f"# {title}", ""]
    out = head
    if prose:
        out += [prose, ""]
    out += [body, ""]
    if legacy_cite:
        out += [f"*Source: {legacy_cite}*", ""]
    return "\n".join(out)


RULE_OF = {k: v for k, (_, _, v) in TABLES.items() if v}


def main() -> int:
    if not SRC.exists():
        print(f"missing {SRC}", file=sys.stderr)
        return 1
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0"
    prose_cache: dict[int, tuple[str, str]] = {}

    OUT.mkdir(parents=True, exist_ok=True)
    written = 0
    for stem, (group, title, rule_id) in TABLES.items():
        src = SRC / f"{stem}.md"
        if not src.exists():
            print(f"  MISSING {src.name}", file=sys.stderr)
            continue
        prose, citation = "", ""
        if rule_id:
            if rule_id not in prose_cache:
                prose_cache[rule_id] = fetch_prose(session, rule_id)
                print(f"  fetched Rules.aspx?ID={rule_id} "
                      f"({len(prose_cache[rule_id][0])} chars of prose)")
            prose, citation = prose_cache[rule_id]
        slug = RENAME.get(stem, stem)
        slug = re.sub(r"-(?:cfd|chd|hpd|lotg|gmg|roe|da|som)$", "", slug)
        dest = OUT / group / f"{slug}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(convert(src, title, group, prose, citation), encoding="utf-8",
                        newline="\n")
        written += 1

    for group, note in GROUP_NOTE.items():
        idx = OUT / group / "index.md"
        rows = sorted(p.stem for p in (OUT / group).glob("*.md") if p.stem != "index")
        idx.write_text("\n".join([
            "---", "cssclasses: pf2e,pf2e-table", "tags:", f"- table/{group}",
            f'aliases: ["{group.replace("-", " ").title()}"]', "---", "",
            f"# {group.replace('-', ' ').title()}", "", note, "",
            *[f"- [[srd/pf2e/tables/{group}/{r}|{r.replace('-', ' ').title()}]]" for r in rows],
            "",
        ]), encoding="utf-8", newline="\n")

    print(f"\nWrote {written} tables + {len(GROUP_NOTE)} index pages to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
