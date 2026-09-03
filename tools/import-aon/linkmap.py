"""Shared resolver turning AoN references into vault wikilinks.

Every AoN page carries links like ``[Agile](/Traits.aspx?ID=6)``. Until now the
importers dropped these to plain text because the target pages did not exist
yet. They do now, so the map below converts them.

Two shapes come out:

    [[traits/player-core/agile|Agile]]        a page of its own
    [[rules-elements/conditions#Off-Guard|off-guard]]   a consolidated section

Build order matters. The map has to be complete before any file is written,
so every importer registers its outputs first and resolves afterwards.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

# AoN database -> the ES category it corresponds to. Anything absent stays
# plain text, which is correct for Sources (rendered as citations already) and
# for databases we do not import.
DB_CATEGORY = {
    "Traits": "trait",
    "Conditions": "condition",
    "Spells": "spell",
    "Feats": "feat",
    "Equipment": "equipment",
    "Actions": "action",
    "Skills": "skill",
    "Weapons": "weapon",
    "Armor": "armor",
    "Shields": "shield",
    "Deities": "deity",
    "Languages": "language",
    "MonsterFamilies": "creature-family",
    "Ancestries": "ancestry",
    "Classes": "class",
    "Backgrounds": "background",
    "Heritages": "heritage",
    "Archetypes": "archetype",
    "Rituals": "ritual",
    "Hazards": "hazard",
    "Domains": "domain",
    "Planes": "plane",
    "Relics": "relic",
    "Curses": "curse",
    "Diseases": "disease",
    "AnimalCompanions": "animal-companion",
    "Familiars": "familiar-ability",
    "Monsters": "__creature__",
    "NPCs": "__creature__",
    "Rules": "__rules__",
}

LINK_RE = re.compile(r"\[([^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*)\]\(/(\w+)\.aspx\?ID=(\d+)[^)]*\)")


class LinkMap:
    """AoN (database, id) -> vault target."""

    # Categories whose names are unique, so a reference can be matched by label
    # when its id misses. AoN keeps a separate record for the pre-Remaster
    # version of a trait or condition, and body text often still cites that
    # older id even in a Remaster book.
    NAME_FALLBACK = {
        "trait", "condition", "skill", "language", "weapon-group", "armor-group",
        "domain", "plane", "deity", "class", "ancestry", "archetype",
    }

    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self._by_key: dict[tuple[str, int], str] = {}
        self._by_name: dict[tuple[str, str], str] = {}

    # -- registration ----------------------------------------------------

    def _target(self, path: Path, anchor: str | None) -> str:
        rel = path.relative_to(self.vault_root).with_suffix("")
        target = str(rel)
        if anchor:
            # Trailing escapes leak in from AoN labels such as "Kholo\\".
            anchor = anchor.rstrip("\\ \t")
            return f"{target}#{anchor}"
        return target

    def add(self, category: str, aon_id: str | int, path: Path,
            anchor: str | None = None, name: str | None = None) -> None:
        num = _num(aon_id)
        target = self._target(path, anchor)
        if num is not None:
            self._by_key[(category, num)] = target
        if name and category in self.NAME_FALLBACK:
            self._by_name.setdefault((category, _norm(name)), target)

    def add_creature(self, aon_id: str | int, path: Path) -> None:
        self.add("__creature__", aon_id, path)

    def add_rule(self, aon_id: str | int, path: Path, anchor: str | None = None) -> None:
        self.add("__rules__", aon_id, path, anchor)

    # -- resolution ------------------------------------------------------

    def lookup(self, db: str, aon_id: int, label: str | None = None) -> str | None:
        cat = DB_CATEGORY.get(db)
        if not cat:
            return None
        hit = self._by_key.get((cat, aon_id))
        if hit or not label:
            return hit
        return self._by_name.get((cat, _norm(label)))

    def rewrite(self, text: str, current: Path | None = None) -> tuple[str, int, int]:
        """Convert AoN links to wikilinks. Returns (text, resolved, dropped)."""
        stats = [0, 0]

        def repl(m: re.Match) -> str:
            label, db, raw_id = m.group(1), m.group(2), int(m.group(3))
            label = LINK_RE.sub(lambda i: i.group(1), label).strip().rstrip("\\")
            target = self.lookup(db, raw_id, label)
            if not target:
                stats[1] += 1
                return label
            if current is not None:
                here = self._target(current, None)
                if target == here:
                    stats[0] += 1
                    return label
                if target.startswith(here + "#"):
                    stats[0] += 1
                    return f"[[{target[len(here):]}|{label}]]"
            stats[0] += 1
            return f"[[{target}|{label}]]"

        out = LINK_RE.sub(repl, text)
        # AoN sometimes wraps a link in literal brackets, which would leave
        # "[[[target|label]]" once the inner link is converted.
        out = re.sub(r"\[(\[\[[^\]]+\]\])\]", r"\1", out)
        return out, stats[0], stats[1]

    # -- persistence -----------------------------------------------------

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({
            "by_id": {f"{c}:{i}": t for (c, i), t in sorted(self._by_key.items())},
            "by_name": {f"{c}:{n}": t for (c, n), t in sorted(self._by_name.items())},
        }, indent=0), encoding="utf-8")

    def load(self, path: Path) -> int:
        if not path.exists():
            return 0
        data = json.loads(path.read_text())
        for k, v in data.get("by_id", {}).items():
            cat, _, num = k.rpartition(":")
            self._by_key[(cat, int(num))] = v
        for k, v in data.get("by_name", {}).items():
            cat, _, nm = k.partition(":")
            self._by_name[(cat, nm)] = v
        return len(self._by_key)

    def __len__(self) -> int:
        return len(self._by_key)


def _num(aon_id: str | int) -> int | None:
    m = re.search(r"(\d+)", str(aon_id))
    return int(m.group(1)) if m else None


def _norm(name: str) -> str:
    """Exact-match key. Deliberately strict: a decorated label such as
    "reach 10 feet" must not match the "Reach" trait."""
    return re.sub(r"\s+", " ", name.strip().lower())
