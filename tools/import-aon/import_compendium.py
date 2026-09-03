#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.31"]
# ///
"""
Import the PF2e Remaster compendium (everything that is neither a rule nor a
creature) from AoN's Elasticsearch index.

Output mirrors the pre-Remaster SRD's compendium layout and per-entry format:
YAML frontmatter, an H1 with the level suffix, a trait line, the body prose,
and an italic Source line carrying the page number.

Two classes of entry are deliberately dropped:

  * anything whose markdown says "There is a more recent version of this"
  * anything carrying a remaster_id, which points forward to its replacement

Both are pre-Remaster records that only matched the book filter because a
Remaster book reprinted them and is therefore listed among their sources.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

from books import ES_KEYS, REMASTER_RULEBOOKS

ES = "https://elasticsearch.aonprd.com/aon/_search"
BOOK_ABBR = {b.lower(): c for b, c in REMASTER_RULEBOOKS.items()}

# Categories handled elsewhere or not worth a note of their own.
SKIP_CATEGORIES = {"creature", "rules", "source", "category-page"}

# Category -> folder, mirroring content/srd/pf2e/compendium.
FOLDERS: dict[str, str] = {
    **{c: "feats" for c in ["feat"]},
    **{c: "spells" for c in ["spell", "ritual"]},
    **{c: "equipment" for c in
       ["equipment", "weapon", "armor", "shield", "siege-weapon", "vehicle", "relic"]},
    **{c: "character" for c in
       ["ancestry", "heritage", "background", "class", "class-feature", "class-sample",
        "class-kit", "archetype", "bloodline", "lesson", "mystery", "patron", "eidolon",
        "arcane-school", "implement", "apparition", "mythic-calling", "epithet", "ikon",
        "tactic", "runesmith-rune", "familiar-ability", "familiar-specific",
        "animal-companion", "domain", "deity", "deity-category", "instinct", "muse",
        "hunters-edge", "doctrine", "methodology", "racket", "conscious-mind",
        "subconscious-mind", "research-field", "innovation", "way", "cause", "curriculum",
        "warfare-tactic", "draconic-exemplar", "element"]},
    **{c: "gm" for c in
       ["hazard", "curse", "disease", "creature-adjustment", "creature-ability",
        "creature-family", "monster-template", "kingdom-structure", "kingdom-event",
        "campsite-meal", "plane", "relic-gift"]},
}
DEFAULT_FOLDER = "rules-elements"  # action, condition, trait, skill, language, sidebar...

# The vault's CSS keys off both the #Actions target and the link title text, so
# these strings are load-bearing and must match exactly.
ACTION_TARGET = "rules/player-core/chapter-8-playing-the-game/actions#Actions"
ACTION_ICON: dict[str, tuple[str, str]] = {
    "single action": (">", "Single Action"),
    "one action": (">", "Single Action"),
    "two actions": (">>", "Two-Action"),
    "three actions": (">>>", "Three-Action"),
    "reaction": ("<", "Reaction"),
    "free action": (" ", "Free Action"),
}


def action_icon(raw: str) -> str:
    """Render AoN's action cost as the icon link the vault CSS expects.

    AoN emits an empty string for anything with no action cost, and compound
    values such as "Single Action to Three Actions" for variable ones.
    """
    key = raw.strip().lower()
    if not key:
        return ""
    if key in ACTION_ICON:
        glyph, title = ACTION_ICON[key]
    elif re.search(r"\b(round|minute|hour|day|week)s?\b", key):
        glyph, title = "??", "Duration or Frequency"
    else:
        glyph, title = "?", "Varies"
    return f'[{glyph}]({ACTION_TARGET} "{title}")'


# --------------------------------------------------------------------------


def normalise_newlines(text: str) -> str:
    """CRLF and lone CR -> LF. AoN's data is CRLF and the repo is eol=lf."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-") or "entry"


def numeric_id(d: dict) -> str:
    m = re.search(r"(\d+)", str(d.get("id", "")))
    return m.group(1) if m else ""


def build_class_index(docs: list[dict]) -> dict[str, str]:
    """Map a Classes.aspx ID to its class name.

    Class features are not uniquely named -- every class has "Initial
    Proficiencies", "Skill Feats" and so on -- but each carries the URL of its
    parent class, so they can be filed under it.
    """
    index: dict[str, str] = {}
    for d in docs:
        if d.get("category") != "class":
            continue
        m = re.search(r"Classes\.aspx\?ID=(\d+)", d.get("url") or "")
        if m:
            index[m.group(1)] = d.get("name", "")
    return index


def destination(d: dict, root: Path, class_index: dict[str, str]) -> Path:
    """Folder and filename for an entry, before uniqueness is enforced."""
    cat = d.get("category", "")
    folder = FOLDERS.get(cat, DEFAULT_FOLDER)
    parts = [folder]
    if cat == "class-feature":
        m = re.search(r"Classes\.aspx\?ID=(\d+)", d.get("url") or "")
        owner = class_index.get(m.group(1), "") if m else ""
        parts += ["class-features", slugify(owner) if owner else "general"]
    return root.joinpath(*parts) / f"{slugify(d.get('name', ''))}.md"


def fetch(category: str | None, books: list[str], page: int = 250) -> list[dict]:
    out: list[dict] = []
    offset = 0
    flt: list[dict] = [{"terms": {"source.keyword": books}}]
    must_not: list[dict] = [{"terms": {"category": sorted(SKIP_CATEGORIES)}}]
    if category:
        flt = [{"term": {"category": category}}, {"terms": {"source.keyword": books}}]
        must_not = []
    while True:
        body = {
            "size": page,
            "from": offset,
            "track_total_hits": True,
            "query": {"bool": {"filter": flt, "must_not": must_not}},
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
        print(f"  {len(out)}/{total}", file=sys.stderr)
        if offset >= total or offset >= 10000:
            break
        time.sleep(0.2)
    return out


def superseded(d: dict) -> bool:
    if d.get("remaster_id"):
        return True
    return "There is a more recent version" in (d.get("markdown") or "")


# --------------------------------------------------------------------------
# Markdown conversion
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


def strip_markup(text: str, keep_bold: bool = True, already_linked: bool = False) -> str:
    # An appended <title level="2">...</title> becomes a real subheading. These
    # mark shared blurbs such as "Critical Specialization Effects".
    def _subheading(m: re.Match) -> str:
        level = min(int(m.group(1)) + 1, 6)
        label = unlink(m.group(2)).strip()
        return f"\n\n{'#' * level} {label}\n\n"

    text = re.sub(r'<title[^>]*level="(\d)"[^>]*>(.*?)</title>', _subheading, text, flags=re.S)

    # Resolve AoN's links *before* building action icons. Doing it after would
    # strip the icon links this function just created back down to a bare ">".
    if not already_linked:
        text = unlink(text)
    # "Click here to view" / "Click here for the full rules" only made sense as a
    # hyperlink; once the link is gone the sentence says nothing.
    text = re.sub(r"[^.\n]*\bClick here\b[^.\n]*\.?", "", text, flags=re.I)

    text = re.sub(
        r'<actions[^>]*string="([^"]*)"[^>]*/?>',
        lambda m: action_icon(m.group(1)),
        text,
    )
    text = re.sub(r"<trait[^>]*label=\"([^\"]+)\"[^>]*/?>", r"\1", text)
    text = re.sub(r"</?(?:row|column|traits|spoilers|document|aside|br|hr|title)[^>]*/?>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    # Appended sections carry their own Source line, often citing a legacy book.
    # The note already has one citation; a second is misleading.
    text = re.sub(r"^\*\*Source\*\*.*$", "", text, flags=re.M)
    # A few AoN entries are malformed at source, opening a <title> inside a
    # markdown link label so the link cannot be matched as a unit, e.g.
    # "[resistances</title> and immunities](/Rules.aspx?ID=2893)". Drop the
    # orphaned tail. Action icons are unaffected: their target is a relative
    # vault path with no leading slash and no .aspx.
    text = re.sub(r"\]\(/[^)]*\.aspx[^)]*\)", "", text)
    if not keep_bold:
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.replace("&amp;", "&").replace("&nbsp;", " ").replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


STAT_TITLE = re.compile(r'<title[^>]*level="(\d)"[^>]*>(.*?)</title>', re.S)


def tabulate_stat_blocks(prose: str) -> str:
    """Turn runs of label/value subheadings into a table.

    Ancestries express their statistics as a level-3 title per field followed by
    a bare value, which renders as a ladder of headings with one word under
    each. A table reads far better. Definition lists would be the natural fit
    but neither Obsidian core nor Quartz supports them, so they would appear
    verbatim. Only short single-paragraph values qualify, which leaves genuine
    prose sections such as "Critical Specialization Effects" as headings.
    """
    hits = list(STAT_TITLE.finditer(prose))
    if not hits:
        return prose

    spans = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(prose)
        spans.append((m, prose[m.end():end]))

    out: list[str] = []
    cursor = 0
    run: list[tuple[str, str]] = []

    def flush() -> None:
        if not run:
            return
        rows = "\n".join(f"| **{lab}** | {val} |" for lab, val in run)
        out.append(f"\n\n|  |  |\n| --- | --- |\n{rows}\n\n")
        run.clear()

    for m, raw in spans:
        level = int(m.group(1))
        label = unlink(m.group(2)).strip()
        value = unlink(re.sub(r"<[^>]+>", " ", raw))
        value = re.sub(r"\s+", " ", value).strip()

        out.append(prose[cursor:m.start()])
        cursor = m.start() + len(m.group(0)) + len(raw)

        is_stat = level >= 3 and 0 < len(value) <= 160 and "\n\n" not in raw.strip()
        if is_stat:
            run.append((label, value.replace("|", "\\|")))
        else:
            flush()
            out.append(f"\n\n{'#' * min(level + 1, 6)} {label}\n\n{raw}")

    flush()
    out.append(prose[cursor:])
    return "".join(out)


def split_head_and_prose(body: str) -> tuple[str, str]:
    """Separate the metadata header from the descriptive text.

    Only some categories use a horizontal rule to divide the two. Feats, spells
    and equipment do; conditions, traits, backgrounds, domains and others run
    the prose straight on from the metadata. For those, the metadata is either
    wrapped in a <column> containing the Source line, or is a bare Source line
    directly under the title.
    """
    parts = re.split(r"^---$", body, maxsplit=1, flags=re.M)
    if len(parts) == 2:
        return parts[0], parts[1]

    head_chunks: list[str] = []

    def take_column(m: re.Match) -> str:
        # Only metadata columns are removed; a column of prose is left alone.
        if "**Source**" in m.group(0):
            head_chunks.append(m.group(0))
            return "\n"
        return m.group(0)

    rest = re.sub(r"<column[^>]*>.*?</column>", take_column, body, flags=re.S)

    if not head_chunks:
        # Bare "**Source** ..." line with no wrapper, e.g. conditions and traits.
        sm = re.search(r"^\*\*Source\*\*.*$", rest, flags=re.M)
        if sm:
            head_chunks.append(sm.group(0))
            rest = rest[: sm.start()] + rest[sm.end():]

    return "\n".join(head_chunks), rest


def parse_entry(d: dict) -> tuple[str, dict]:
    diag: dict = {"name": d.get("name"), "category": d.get("category"), "warnings": []}
    md = d.get("markdown") or ""
    name = d.get("name", "Unknown")

    m = re.search(r'<title[^>]*?right="([^"]*)"', md, re.S)
    right = (m.group(1).strip() if m else "")

    # The action cost sits inside the <title> block, which is otherwise dropped.
    tb = re.search(r"<title.*?</title>", md, re.S)
    am = re.search(r'<actions[^>]*string="([^"]*)"', tb.group(0)) if tb else None
    title_action = action_icon(am.group(1)) if am else ""

    body = md
    tm = re.search(r"</title>", md)
    if tm:
        body = md[tm.end():]
    body = re.sub(r"<traits>.*?</traits>", "", body, flags=re.S)
    body = re.sub(r"<spoilers>.*?</spoilers>", "", body, flags=re.S)

    head, prose = split_head_and_prose(body)
    # Resolve links across the whole body before anything slices it up, so no
    # later pass can cut one in half and strand a "](/Url)" fragment.
    prose = unlink(prose)
    prose = tabulate_stat_blocks(prose)
    if not prose.strip():
        diag["warnings"].append("no body prose")

    traits = d.get("trait") or []

    # Resolve links first: a label can sit inside one, as in
    # "_[**PFS Note**](/pathfinder-society) text_", which otherwise leaves the
    # closing bracket and URL stranded in the value.
    head_flat = unlink(head)
    head_flat = re.sub(r'<actions[^>]*string="([^"]*)"[^>]*/?>',
                       lambda mm: action_icon(mm.group(1)), head_flat)
    meta: list[tuple[str, str]] = []
    for mm in re.finditer(r"\*\*([A-Z][A-Za-z0-9 /'()-]{0,32})\*\*(.*?)(?=\*\*[A-Z]|\Z)",
                          head_flat, re.S):
        label = mm.group(1).strip()
        val = strip_markup(mm.group(2), keep_bold=False, already_linked=True).strip(" _;,")
        val = re.sub(r"\s*\n\s*", " ", val)
        if label == "Source" or not val:
            continue
        meta.append((label, val))

    # Citation: prefer the Remaster book over an adventure reprint.
    sources = [s.strip() for s in (d.get("source") or [])]
    raws = d.get("source_raw") or []
    primary = next((s for s in sources if s.lower() in BOOK_ABBR), sources[0] if sources else "")
    cite = next((r for r in raws if r.lower().startswith(primary.lower())), raws[-1] if raws else "")
    page = None
    cm = re.match(r"(.*?)\s*pg\.\s*(\d+)", cite)
    if cm:
        page = cm.group(2)
    else:
        diag["warnings"].append("no page number")

    cat = d.get("category", "misc")
    tags = [f"compendium/src/pf2e-remaster/{slugify(primary)}"]
    tags += [f"trait/{slugify(t)}" for t in traits]
    if d.get("level") is not None:
        tags.append(f"{cat}/level/{d['level']}")

    fm = [
        "---",
        "obsidianUIMode: preview",
        f"cssclasses: pf2e,pf2e-{cat}",
        "tags:",
        *[f"- {t}" for t in tags],
        f"aliases: [{json.dumps(name, ensure_ascii=False)}]",
        f"aon_id: {json.dumps(d.get('id',''))}",
        f"source: {json.dumps(primary)}",
        "---",
        "",
    ]

    out = list(fm)
    heading = f"# {name}"
    if right:
        heading += f"  *{right}*"
    if title_action:
        heading += f"  {title_action}"
    out.append(heading)
    out.append("")
    if traits:
        out.append("  ".join(f"`{t}`" for t in traits))
        out.append("")
    for label, val in meta:
        out.append(f"- **{label}**: {val}")
    if meta:
        out.append("")
    out.append(strip_markup(prose))
    out.append("")
    if cite:
        src_txt = f"*Source: {primary} p. {page}*" if page else f"*Source: {strip_markup(cite)}*"
        out.append(src_txt)

    diag["traits"] = len(traits)
    diag["meta"] = len(meta)
    diag["body_chars"] = len(strip_markup(prose))
    return "\n".join(out) + "\n", diag


# --------------------------------------------------------------------------


SAMPLE_CATEGORIES = [
    "feat", "spell", "equipment", "weapon", "armor", "action", "trait", "condition",
    "class-feature", "background", "heritage", "ancestry", "archetype", "hazard",
    "ritual", "domain", "animal-companion", "relic", "vehicle", "curse",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    here = Path(__file__).parent
    ap.add_argument("--snapshot", type=Path, default=here / ".snapshot" / "compendium.json")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    if args.out is None:
        args.out = (
            here.parents[1] / "content" / "srd" / "pf2e-remaster" / "compendium"
            if args.all else here / "staging" / "compendium"
        )

    if args.snapshot.exists() and not args.refresh:
        docs = json.loads(args.snapshot.read_text())
        print(f"Loaded {len(docs)} docs from snapshot")
    else:
        print("Fetching compendium from Elasticsearch (per category, to beat the 10k window)...")
        docs, seen = [], set()
        cats = json.loads((here / ".snapshot" / "categories.json").read_text())
        for cat in cats:
            got = fetch(cat, ES_KEYS)
            for g in got:
                if g.get("id") not in seen:
                    seen.add(g.get("id"))
                    docs.append(g)
            print(f"  {cat}: {len(got)}")
        args.snapshot.parent.mkdir(parents=True, exist_ok=True)
        args.snapshot.write_text(json.dumps(docs))
        print(f"Snapshotted {len(docs)} docs")

    live = [d for d in docs if not superseded(d)]
    print(f"Excluded {len(docs) - len(live)} superseded (pre-Remaster) entries")

    if args.all:
        selection = live
    else:
        by_cat: dict[str, dict] = {}
        for d in live:
            c = d.get("category")
            if c in SAMPLE_CATEGORIES and c not in by_cat:
                by_cat[c] = d
        selection = [by_cat[c] for c in SAMPLE_CATEGORIES if c in by_cat]
        print(f"QA sample: {len(selection)} entries, one per category\n")

    class_index = build_class_index(docs)
    diags, per_folder, seen_paths = [], {}, {}
    disambiguated = 0
    for d in selection:
        text, diag = parse_entry(d)
        path = destination(d, args.out, class_index)
        if path in seen_paths:
            # Names are not unique across the compendium: hundreds of
            # item-granted actions are called "Cast a Spell" or just
            # "(concentrate)". Suffix with the AoN id rather than overwrite.
            # The full id is needed, not just its digits, because ids are only
            # unique per category -- equipment-2306 and weapon-2306 coexist.
            base = path.stem
            suffix = slugify(str(d.get("id", ""))) or "dup"
            path = path.with_name(f"{base}-{suffix}.md")
            guard = 2
            while path in seen_paths:
                path = path.with_name(f"{base}-{suffix}-{guard}.md")
                guard += 1
            disambiguated += 1
        seen_paths[path] = d["name"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(normalise_newlines(text), encoding="utf-8")
        folder = path.parent.relative_to(args.out).parts[0]
        per_folder[folder] = per_folder.get(folder, 0) + 1
        diag["path"] = str(path.relative_to(args.out))
        diags.append(diag)
        if not args.all:
            w = ("  !! " + "; ".join(diag["warnings"])) if diag["warnings"] else ""
            print(f"  {diag['category']:18} {d['name'][:30]:32} "
                  f"traits={diag['traits']:2d} meta={diag['meta']:2d} body={diag['body_chars']:5d}{w}")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "_diagnostics.json").write_text(json.dumps(diags, indent=1), encoding="utf-8")
    print(f"\nWrote {len(selection)} files to {args.out}")
    for f, n in sorted(per_folder.items(), key=lambda x: -x[1]):
        print(f"  {n:6d}  {f}")
    if disambiguated:
        print(f"Disambiguated {disambiguated} duplicate names with their AoN id")
    bad = [d for d in diags if d["warnings"]]
    print(f"Entries with warnings: {len(bad)}")
    kinds: dict[str, int] = {}
    for d in bad:
        for w in d["warnings"]:
            kinds[re.sub(r"\d+", "N", w)] = kinds.get(re.sub(r"\d+", "N", w), 0) + 1
    for k, n in sorted(kinds.items(), key=lambda x: -x[1])[:10]:
        print(f"  {n:6d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
