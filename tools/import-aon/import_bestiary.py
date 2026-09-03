#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31"]
# ///
"""
Build bestiary notes in Fantasy Statblocks format from the AoN snapshot.

Reads .snapshot/creatures.json (written by audit_creatures.py) so generation
never depends on a live endpoint. The audit established that all 718 creatures
split into exactly three '---' blocks with no label appearing in more than one,
so block position determines slot deterministically:

    block 0 -> abilities_top   (Perception, Languages, Skills, mods, Items)
    block 1 -> abilities_mid   (AC, saves, HP, immunities, resistances)
    block 2 -> abilities_bot   (Speed, Strikes, spellcasting, offense)

Numeric and categorical values come from the structured ES fields, not from
parsing prose. Only the prose slots are parsed out of markdown.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Fantasy Statblocks PF2e action glyphs.
ACTION_GLYPH = {
    "single action": "⬻",
    "one action": "⬻",
    "two actions": "⬺",
    "three actions": "⬽",
    "reaction": "⬲",
    "free action": "⭓",
}

from books import REMASTER_RULEBOOKS

BOOK_ABBR = {b.lower(): c for b, c in REMASTER_RULEBOOKS.items()}

# Labels that become dedicated statblock keys rather than free-form abilities.
BLOCK0_RESERVED = {"Source", "Perception", "Languages", "Skills",
                   "Str", "Dex", "Con", "Int", "Wis", "Cha"}
BLOCK1_RESERVED = {"AC", "Fort", "Ref", "Will", "HP"}
BLOCK2_RESERVED = {"Speed", "Melee", "Ranged", "Damage"}

SPELL_BLOCK = re.compile(r"^(.*(?:Innate|Spontaneous|Prepared|Focus) Spells|Rituals)$")


# --------------------------------------------------------------------------
# Markup cleanup
# --------------------------------------------------------------------------


# The label may itself contain brackets: AoN embeds literal action tokens
# such as "[free-action]" inside link labels.
LINK = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\([^)]*\)")


def unlink(text: str) -> str:
    """Markdown link -> its label, including nested links.

    AoN nests links inside link labels. A single pass leaves a stranded
    "](/Url.aspx?ID=86)" behind, because re.sub does not rescan what it just
    substituted, so repeat until the text stops changing.
    """
    for _ in range(10):
        new = LINK.sub(r"\1", text)
        if new == text:
            return new
        text = new
    return text


def strip_markup(text: str) -> str:
    """AoN markup -> plain text. Links become their label; no external URLs."""
    text = re.sub(
        r'<actions[^>]*string="([^"]+)"[^>]*/?>',
        lambda m: ACTION_GLYPH.get(m.group(1).strip().lower(), "") + " ",
        text,
    )
    text = re.sub(r"<trait[^>]*label=\"([^\"]+)\"[^>]*/?>", r"\1", text)
    text = re.sub(r"</?(?:row|column|traits|title|document|aside|br|hr)[^>]*/?>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unlink(text)
    # The plugin renders __x__ as bold inside desc strings.
    text = re.sub(r"\*\*([^*]+)\*\*", r"__\1__", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    return text.strip(" ;,")


def statblock_region(md: str) -> str:
    m = re.search(r'<title level="2"[^>]*>', md)
    return md[m.end():] if m else md


def split_blocks(md: str) -> list[str]:
    return re.split(r"^---$", statblock_region(md), flags=re.M)


def parse_labels(block: str) -> list[tuple[str, str]]:
    """Split a block into (label, body) pairs on leading **Label** markers.

    Links are resolved first. AoN writes some field labels as links, in both
    orders -- "[**Troop Defenses**](/MonsterAbilities.aspx?ID=86)" and
    "**[Troop Defenses](/MonsterAbilities.aspx?ID=86)**". Splitting before
    resolving them either severs the link, leaving a stranded "](/Url)" at the
    head of the value, or hides the label so its text is swallowed by the
    preceding field.
    """
    block = unlink(block)
    positions = [(m.start(), m.end(), m.group(1))
                 for m in re.finditer(r"\*\*([A-Z][A-Za-z0-9 /'-]{0,40})\*\*", block)]
    out: list[tuple[str, str]] = []
    for i, (start, end, label) in enumerate(positions):
        stop = positions[i + 1][0] if i + 1 < len(positions) else len(block)
        out.append((label.strip(), block[end:stop]))
    return out


# --------------------------------------------------------------------------
# YAML emission
# --------------------------------------------------------------------------


def y(value) -> str:
    """JSON strings are valid YAML, which sidesteps quoting and colon issues."""
    return json.dumps(value, ensure_ascii=False)


def name_desc_list(key: str, items: list[tuple[str, str]], indent: str = "  ") -> list[str]:
    if not items:
        return []
    lines = [f"{key}:"]
    for n, d in items:
        lines.append(f"{indent}- name: {y(n)}")
        lines.append(f"{indent}  desc: {y(d)}")
    return lines


def normalise_newlines(text: str) -> str:
    """CRLF and lone CR -> LF. AoN's data is CRLF and the repo is eol=lf."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-") or "creature"


# --------------------------------------------------------------------------
# Conversion
# --------------------------------------------------------------------------


def dedupe(creatures: list[dict]) -> tuple[list[dict], list[tuple[dict, dict]]]:
    """Collapse creatures that AoN indexes twice.

    A creature reprinted in a Remaster book keeps its old adventure entry as a
    separate record, and the two can disagree on real numbers -- Calikang is AC
    31 in Monster Core 2 and AC 35 in the adventure; Rusalka is HP 230 vs 180.
    Taking whichever happened to be last would silently publish legacy stats.

    The Remaster printing always lists its Remaster book first in `source`,
    whereas the legacy record lists the adventure first. Record IDs are not a
    reliable signal: for Boggard Scout the Remaster record has the lower ID.
    """
    groups: dict[tuple[str, str], list[dict]] = {}
    for c in creatures:
        groups.setdefault((book_slug(c), slugify(c["name"])), []).append(c)

    def remaster_first(c: dict) -> int:
        srcs = [s.strip().lower() for s in (c.get("source", []) or [])]
        return 1 if srcs and srcs[0] in BOOK_ABBR else 0

    def numeric_id(c: dict) -> int:
        m = re.search(r"(\d+)", str(c.get("id", "")))
        return int(m.group(1)) if m else 0

    kept: list[dict] = []
    dropped: list[tuple[dict, dict]] = []
    for _, group in groups.items():
        if len(group) == 1:
            kept.append(group[0])
            continue
        ranked = sorted(group, key=lambda c: (remaster_first(c), numeric_id(c)), reverse=True)
        kept.append(ranked[0])
        dropped.extend((d, ranked[0]) for d in ranked[1:])
    return kept, dropped


def book_slug(c: dict) -> str:
    """Directory for a creature: its Remaster book, mirroring the legacy layout."""
    sources = [s.strip() for s in (c.get("source", []) or [])]
    primary = next((s for s in sources if s.lower() in BOOK_ABBR), sources[0] if sources else "misc")
    return slugify(primary)


def convert(c: dict) -> tuple[str, dict]:
    """Return (markdown, diagnostics)."""
    diag: dict = {"name": c.get("name"), "warnings": []}
    md = c.get("markdown", "")
    blocks = split_blocks(md)
    if len(blocks) != 3:
        diag["warnings"].append(f"expected 3 blocks, got {len(blocks)}")
        blocks = (blocks + ["", "", ""])[:3]

    b0, b1, b2 = (parse_labels(b) for b in blocks)
    d0 = {k: v for k, v in b0}
    d1 = {k: v for k, v in b1}

    name = c.get("name", "Unknown")
    level = c.get("level")
    traits = c.get("trait", []) or []

    # ES returns size as a list; the statblock wants one value.
    raw_size = c.get("size") or ""
    sizes = raw_size if isinstance(raw_size, list) else [raw_size]
    size = sizes[0] if sizes else ""

    sources = [s.strip() for s in (c.get("source", []) or [])]
    src_raw = c.get("source_raw", []) or []

    # A creature reprinted in a Core book lists several sources in arbitrary
    # order. Prefer the Core book so provenance is not an adventure module.
    primary = next((s for s in sources if s.lower() in BOOK_ABBR), sources[0] if sources else "")

    # -- header fields ---------------------------------------------------
    out: list[str] = [
        "```statblock",
        "columns: 2",
        "forcecolumns: true",
        "layout: Basic Pathfinder 2e Layout",
    ]
    out.append(f"source: {y(BOOK_ABBR.get(primary.lower(), primary))}")
    out.append(f"name: {y(name)}")
    out.append(f"level: {y(f'Creature {level}')}")
    # Remaster removed alignment, so no alignment key is emitted.
    if size:
        out.append(f"size: {y(size)}")
    # Size also appears in the trait list; it already has its own key.
    lowered = {s.lower() for s in sizes}
    for i, t in enumerate([t for t in traits if t.lower() not in lowered], start=1):
        out.append(f"trait_{i:02d}: {y(t)}")

    if c.get("perception") is not None:
        out.append(f"modifier: {c['perception']}")

    # -- block 0: perception / languages / skills / mods / top abilities --
    perc_body = strip_markup(d0.get("Perception", ""))
    if perc_body:
        out += name_desc_list("perception", [("Perception", f"Perception {perc_body}")])

    langs = strip_markup(d0.get("Languages", ""))
    if langs:
        out.append(f"languages: {y(langs)}")

    skills = strip_markup(d0.get("Skills", ""))
    if skills:
        out += name_desc_list("skills", [("Skills", skills)])

    mods = [c.get(k) for k in ("strength", "dexterity", "constitution",
                               "intelligence", "wisdom", "charisma")]
    if all(m is not None for m in mods):
        out.append(f"abilityMods: {json.dumps(mods)}")
    else:
        diag["warnings"].append("missing one or more ability modifiers")

    top = [(k, strip_markup(v)) for k, v in b0 if k not in BLOCK0_RESERVED]
    out += name_desc_list("abilities_top", top)

    # -- block 1: defenses ------------------------------------------------
    ac = c.get("ac")
    if ac is not None:
        out.append(f"ac: {ac}")
    saves = "; ".join(
        f"__{lab}__: {strip_markup(d1[lab])}" for lab in ("Fort", "Ref", "Will") if lab in d1
    )
    ac_desc = f"{ac if ac is not None else strip_markup(d1.get('AC',''))}"
    if saves:
        ac_desc += f"; {saves}"
    out += name_desc_list("armorclass", [("AC", ac_desc)])

    hp = c.get("hp")
    if hp is not None:
        out.append(f"hp: {hp}")
    hp_desc = strip_markup(d1.get("HP", "")) or str(hp or "")
    for extra in ("Immunities", "Resistances", "Weaknesses", "Hardness"):
        if extra in d1:
            hp_desc += f"; __{extra}__ {strip_markup(d1[extra])}"
    out += name_desc_list("health", [("HP", hp_desc)])

    mid = [(k, strip_markup(v)) for k, v in b1
           if k not in BLOCK1_RESERVED | {"Immunities", "Resistances", "Weaknesses", "Hardness"}]
    out += name_desc_list("abilities_mid", mid)

    # -- block 2: speed, strikes, spells, offense -------------------------
    speed = c.get("speed_raw") or strip_markup(dict(b2).get("Speed", ""))
    if speed:
        out.append(f"speed: {y(strip_markup(str(speed)))}")

    attacks: list[tuple[str, str]] = []
    spells: list[tuple[str, str]] = []
    bot: list[tuple[str, str]] = []

    i = 0
    while i < len(b2):
        label, body = b2[i]
        if label in ("Melee", "Ranged"):
            desc = strip_markup(body)
            # A Damage label immediately follows its Strike.
            if i + 1 < len(b2) and b2[i + 1][0] == "Damage":
                desc += f" __Damage__ {strip_markup(b2[i + 1][1])}"
                i += 1
            attacks.append((label, desc))
        elif SPELL_BLOCK.match(label):
            spells.append((label, strip_markup(body)))
        elif label not in BLOCK2_RESERVED:
            bot.append((label, strip_markup(body)))
        i += 1

    out += name_desc_list("attacks", attacks)
    out += name_desc_list("abilities_bot", bot)
    out += name_desc_list("spellcasting", spells)

    if src_raw:
        # Match the citation to the book chosen above, not just the last entry.
        book = next((s for s in src_raw if s.lower().startswith(primary.lower())), src_raw[-1])
        m = re.match(r"(.*?)\s*pg\.\s*(\d+)", book)
        out.append(f"sourcebook: {y(f'_{m.group(1).strip()}_, page {m.group(2)}.' if m else book)}")
    out.append("```")

    diag["attacks"] = len(attacks)
    diag["spell_blocks"] = len(spells)
    diag["abilities"] = len(top) + len(mid) + len(bot)
    if not attacks and not spells:
        diag["warnings"].append("no attacks and no spellcasting")

    # -- note wrapper -----------------------------------------------------
    tag_traits = "\n".join(f"  - pf2e/creature/trait/{slugify(t)}" for t in traits)
    fm = [
        "---",
        "obsidianUIMode: preview",
        "noteType: pf2eMonster",
        f"aliases: {y(name)}",
        "tags:",
        f"  - pf2e/creature/level/{level}",
    ]
    if tag_traits:
        fm.append(tag_traits)
    fm += [
        "statblock: inline",
        f"name: {y(name)}",
        f"level: {level}",
        f"source: {y(primary)}",
        *([f"other_sources: {y('; '.join(s for s in sources if s != primary))}"]
          if len(sources) > 1 else []),
        f"aon_id: {y(c.get('id',''))}",
        f"aon_url: {y('https://2e.aonprd.com' + c.get('url','')) if c.get('url') else y('')}",
        "---",
        "",
    ]

    encounter = ["", "```encounter-table", f"name: {name}", "creatures:", f"  - 1: {name}", "```"]
    return "\n".join(fm + out + encounter) + "\n", diag


# --------------------------------------------------------------------------
# QA sample selection
# --------------------------------------------------------------------------


def pick_sample(creatures: list[dict]) -> list[tuple[str, dict]]:
    """A QA matrix, not a greatest-hits list: each entry probes a failure mode."""
    by_name = {c["name"]: c for c in creatures}
    picked: list[tuple[str, dict]] = []
    used: set[str] = set()

    def take(reason: str, pred, limit: int = 1):
        n = 0
        for c in creatures:
            if n >= limit or c["name"] in used:
                continue
            try:
                ok = pred(c)
            except Exception:
                ok = False
            if ok:
                picked.append((reason, c))
                used.add(c["name"])
                n += 1

    md = lambda c: c.get("markdown", "")
    traits = lambda c: [t.lower() for t in c.get("trait", [])]

    take("lowest level", lambda c: c.get("level") == min(x.get("level", 99) for x in creatures))
    take("highest level", lambda c: c.get("level") == max(x.get("level", -99) for x in creatures))
    take("plain melee only", lambda c: "**Melee**" in md(c) and "**Ranged**" not in md(c)
         and "Spells**" not in md(c) and c.get("level", 0) <= 3)
    take("melee + ranged", lambda c: "**Melee**" in md(c) and "**Ranged**" in md(c))
    take("innate spellcaster", lambda c: "Innate Spells**" in md(c))
    take("prepared spellcaster", lambda c: "Prepared Spells**" in md(c))
    take("spontaneous spellcaster", lambda c: "Spontaneous Spells**" in md(c))
    take("multi-block spellcaster", lambda c: len(re.findall(r"Spells\*\*", md(c))) >= 2)
    take("has rituals", lambda c: "**Rituals**" in md(c))
    take("swarm", lambda c: "swarm" in traits(c))
    take("troop", lambda c: "troop" in traits(c))
    take("regeneration", lambda c: "regeneration" in md(c).lower())
    take("fast healing", lambda c: "fast healing" in md(c).lower())
    take("aura", lambda c: re.search(r"\*\*[^*]*[Aa]ura[^*]*\*\*", md(c)) is not None)
    take("immunities+resist+weak", lambda c: all(k in md(c) for k in
         ("**Immunities**", "**Resistances**", "**Weaknesses**")))
    take("contains table", lambda c: "<table" in md(c))
    take("multiple sources", lambda c: len(c.get("source", [])) > 1)
    take("NPC Core w/ gear", lambda c: any("npc core" in s.lower() for s in c.get("source", []))
         and "**Items**" in md(c))
    take("rare or unique", lambda c: c.get("rarity") in ("rare", "unique"))
    take("no Strike at all", lambda c: "**Melee**" not in md(c) and "**Ranged**" not in md(c))
    take("many movement modes", lambda c: str(c.get("speed_raw", "")).count(",") >= 2)
    return picked


def main() -> int:
    ap = argparse.ArgumentParser()
    here = Path(__file__).parent
    ap.add_argument("--snapshot", type=Path, default=here / ".snapshot" / "creatures.json")
    # Not dot-prefixed: Obsidian hides dotfolders, and this needs reviewing.
    ap.add_argument("--out", type=Path, help="output root (default: staging for sample, vault for --all)")
    ap.add_argument("--all", action="store_true", help="convert every creature, not the QA sample")
    args = ap.parse_args()

    if args.out is None:
        args.out = (
            here.parents[1] / "content" / "srd" / "pf2e-remaster" / "bestiary"
            if args.all
            else here / "staging" / "bestiary"
        )

    creatures = json.loads(args.snapshot.read_text())
    print(f"Loaded {len(creatures)} creatures")

    creatures, dropped = dedupe(creatures)
    if dropped:
        print(f"Deduplicated {len(dropped)} duplicate records (kept the Remaster printing):")
        for d, k in dropped:
            diffs = [f"{f} {d.get(f)}->{k.get(f)}" for f in ("ac", "hp", "level")
                     if d.get(f) != k.get(f)]
            note = f"  [stats differ: {', '.join(diffs)}]" if diffs else ""
            print(f"  {d['name']:26} dropped {d['id']:16} kept {k['id']}{note}")
        print()

    if args.all:
        selection = [("", c) for c in creatures]
    else:
        selection = pick_sample(creatures)
        print(f"QA sample: {len(selection)} creatures\n")

    args.out.mkdir(parents=True, exist_ok=True)
    diags = []
    per_book: dict[str, int] = {}
    seen: dict[Path, str] = {}
    for reason, c in selection:
        text, diag = convert(c)
        diag["reason"] = reason

        bslug = book_slug(c)
        dest = args.out / bslug
        dest.mkdir(parents=True, exist_ok=True)
        path = dest / f"{slugify(c['name'])}.md"
        if path in seen:
            diag["warnings"].append(f"path collides with {seen[path]}")
        seen[path] = c["name"]
        diag["path"] = str(path.relative_to(args.out))
        diags.append(diag)

        path.write_text(normalise_newlines(text), encoding="utf-8")
        per_book[bslug] = per_book.get(bslug, 0) + 1
        if reason:
            warn = ("  !! " + "; ".join(diag["warnings"])) if diag["warnings"] else ""
            print(f"  {reason:26} {c['name']:34} "
                  f"atk={diag['attacks']} spells={diag['spell_blocks']} abil={diag['abilities']}{warn}")

    (args.out / "_diagnostics.json").write_text(json.dumps(diags, indent=1), encoding="utf-8")
    bad = [d for d in diags if d["warnings"]]
    print(f"\nWrote {len(selection)} files to {args.out}")
    for b, n in sorted(per_book.items(), key=lambda x: -x[1]):
        print(f"  {n:5d}  {b}")
    print(f"\nCreatures with warnings: {len(bad)}")
    if bad:
        kinds: dict[str, int] = {}
        for d in bad:
            for w in d["warnings"]:
                key = re.sub(r"\d+", "N", w)
                kinds[key] = kinds.get(key, 0) + 1
        for k, n in sorted(kinds.items(), key=lambda x: -x[1]):
            print(f"  {n:5d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
