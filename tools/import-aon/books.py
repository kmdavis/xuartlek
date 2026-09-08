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

  Lost Omens         Setting line, not rules -- with one deliberate exception,
                     Divine Mysteries (see below).

  Divine Mysteries   INCLUDED despite AoN shelving it under Lost Omens. It is
  Web Supplement     the Remaster replacement for Gods & Magic, and a large
                     amount of PF2e mechanics is gated on a specific deity:
                     Fleet Step, for instance, is only available to certain
                     worshippers. Excluding it would leave 5,071 unresolvable
                     deity references and orphan the 108 spells and 91 feats
                     that depend on them. Only the core book is taken; the Web
                     Supplement's 80 extra niche gods, and the long tail in
                     Draconic Codex / Gods & Magic / adventures / blog posts,
                     are all left out.

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
    "Divine Mysteries": "DM",
}

# Books that are not in AoN's "Rulebooks" shelf but are imported anyway.
# Kept separate so the Rulebooks-derived provenance above stays honest.
NON_RULEBOOKS = frozenset({"Divine Mysteries"})

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
