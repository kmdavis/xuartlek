"""Canonical book list, shared by every importer.

Derived from Archives of Nethys' own catalogue rather than guessed, using
source_category == "Rulebooks" and release_date >= 2023-08-02 (Rage of Elements,
the first book of the Remaster era). Regenerate with:

    curl -s -X POST https://elasticsearch.aonprd.com/aon/_search \
      -H 'Content-Type: application/json' \
      -d '{"size":300,"query":{"bool":{"filter":[{"term":{"category":"source"}}]}},
           "_source":["name","source_category","release_date"]}'

The list is hardcoded rather than fetched at runtime so a run is reproducible
and a new Paizo release cannot silently change what gets generated.

Deliberately excluded:

  Legacy rulebooks   Core Rulebook, Advanced Player's Guide, Bestiary 1-3,
                     Gamemastery Guide, Secrets of Magic, Book of the Dead,
                     Dark Archive, Treasure Vault, Guns & Gears, Ancestry Guide.
                     All superseded by a book in the list below.

  Lost Omens         Setting line, not rules. Note this also excludes Divine
                     Mysteries (AoN categorises it Lost Omens), which is the
                     Remaster replacement for Gods & Magic and carries the
                     deity and domain entries.

  Adventures / APs   Adventure Paths, standalone adventures, Society scenarios.
"""

from __future__ import annotations

# Book title -> short citation code used in statblocks and <sup> citations.
REMASTER_RULEBOOKS: dict[str, str] = {
    "Player Core": "PC1",
    "Player Core 2": "PC2",
    "GM Core": "GMC",
    "Monster Core": "MC",
    "Monster Core 2": "MC2",
    "NPC Core": "NPC",
    "Rage of Elements": "RoE",
    "Howl of the Wild": "HotW",
    "War of Immortals": "WoI",
    "War of Immortals Alternate Mythic Rules": "WoIA",
    "Guns & Gears (Remastered)": "G&G",
    "Treasure Vault (Remastered)": "TV",
    "Battlecry!": "BC",
    "Dark Archives (Remastered)": "DA",
    "Impossible Magic": "IM",
    "Secrets of the Unlit Star Game Master's Guide": "SUS",
}

# The original five, kept so a run can be narrowed back down for comparison.
CORE_FIVE = ["Player Core", "Player Core 2", "GM Core", "Monster Core", "NPC Core"]

ALL_BOOKS = list(REMASTER_RULEBOOKS)

# Elasticsearch stores source as lowercase in the keyword subfield.
ES_KEYS = [b.lower() for b in ALL_BOOKS]


def code(book: str) -> str:
    """Short citation code for a book title, falling back to the title."""
    return REMASTER_RULEBOOKS.get(book.strip(), book.strip())


def slug(book: str) -> str:
    import re
    s = re.sub(r"[^\w\s-]", "", book.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")
