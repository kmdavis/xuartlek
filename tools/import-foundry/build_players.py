#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""
Write a player note per Foundry actor export.

Layout of each note:

    frontmatter          quick fields for dataview and the campaign index
    ```statblock```      Fantasy Statblocks, matching the existing Flick page
    Feats                grouped by category, with rules text
    Inventory            worn / held / carried / consumable, outside the statblock

Only equipped weapons, worn armour and invested items reach the statblock; the
rest is inventory prose, because a statblock listing ten torches helps nobody.

Derived numbers come from foundry_pc, which is checked against Flick by
check_flick.py. Run that first.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import foundry_pc as F

HERE = Path(__file__).parent
VAULT = HERE.parents[1]
OUT = VAULT / "content" / "campaigns" / "votgz" / "players"
TRAITS = "srd/pf2e/compendium/rules-elements/traits"
LANGS = "srd/pf2e/compendium/rules-elements/languages"

# actor file stem -> (note name, player, companion-of)
ROSTER = {
    "flick-(wes)": ("Flick", "Wes Baker", None),
    "belegost-(elias)": ("Belegost", "Elias", None),
    "gripp-(levi)": ("Gripp", "Levi", None),
    "vaelendil-(tanusri)": ("Vaelendil", "Tanusri", None),
    "espera-(ellen)": ("Espera", "Ellen", None),
    "gteek-(calvin)": ("Gteek", "Calvin", None),
    "sir-pickles-(gripp's-companion)": ("Sir Pickles", "Levi", "Gripp"),
    "drak-(ellen's-companion)": ("Drak", "Ellen", "Espera"),
}

ACTION_GLYPH = {1: "⬻", 2: "⬺", 3: "⬹", "reaction": "⬲", "free": "⭓"}


def slug(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def _index(root: Path, sub: str) -> dict[str, str]:
    base = root / "content" / "srd" / "pf2e" / "compendium" / "rules-elements" / sub
    return {p.stem: str(p.relative_to(root / "content").with_suffix(""))
            for p in base.rglob("*.md") if p.stem != "index"}


def _headings(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(re.findall(r"^##\s+(.+?)\s*$", path.read_text(encoding="utf-8"), re.M))


TRAIT_INDEX = _index(VAULT, "traits")
LANG_HEADINGS = _headings(VAULT / "content" / "srd" / "pf2e" / "compendium"
                          / "rules-elements" / "languages.md")


def trait_link(t: str) -> str:
    """Link a trait to wherever it actually lives.

    Traits are filed per sourcebook, so the folder cannot be assumed. Traits
    carrying a value -- thrown-10, versatile-s, scatter-5 -- have no page of
    their own and resolve to the base trait. Anything unknown degrades to
    readable text rather than a broken link.
    """
    label = t.replace("-", " ").title()
    s = slug(t)
    target = TRAIT_INDEX.get(s)
    if target is None:
        stem = re.sub(r"-(?:\d+|[a-z])$", "", s)
        target = TRAIT_INDEX.get(stem)
    return f"[[{target}|{label}]]" if target else label


def language_link(name: str) -> str:
    label = name.title()
    return f"[[{LANGS}#{label}|{label}]]" if label in LANG_HEADINGS else label


def weapon_line(actor: dict, w: dict, mods: dict) -> str | None:
    s = w["system"]
    eq = s.get("equipped") or {}
    if eq.get("carryType") not in ("held", "worn"):
        return None
    bonus, _ab = F.attack_bonus(actor, w, mods)
    dmg = s.get("damage") or {}
    dice = f"{dmg.get('dice', 1)}{dmg.get('die', 'd4')}"
    ranged = bool(s.get("range"))
    traits = [t for t in (s.get("traits", {}).get("value") or [])]
    # Strength adds to melee damage; ranged only with propulsive or thrown.
    bump = 0 if ranged else mods.get("str", 0)
    # Precise Strike applies to melee agile or finesse weapons only.
    if not ranged and ({"agile", "finesse"} & set(traits)):
        bump += F.precision_damage(actor)
    dmg_str = f"{dice}{f'+{bump}' if bump > 0 else (str(bump) if bump else '')}"
    tr = ", ".join(trait_link(t) for t in sorted(traits)) if traits else ""
    rng = ""
    if ranged:
        rng = f" __Range__ {s['range']} ft.;"
        if s.get("reload", {}).get("value") not in (None, "", "0"):
            rng += f" __Reload__ {s['reload']['value']};"
    kind = "Ranged" if ranged else "Melee"
    return (f"⬻ {w['name'].lower()} +{bonus}"
            f"{f' ({tr})' if tr else ''}{rng} __Damage__ {dmg_str} "
            f"{(dmg.get('damageType') or '')}").strip()


def statblock(actor: dict, name: str, mods: dict) -> list[str]:
    items = F.build_items(actor)
    lvl = F.level(actor)
    sv = F.saves(actor, mods)
    sk = F.skills(actor, mods) | F.lores(actor, mods)
    anc = items.get("ancestry", {}).get("name", "")
    langs = ((items.get("ancestry", {}).get("system", {}).get("languages") or {}).get("value") or [])
    speed = items.get("ancestry", {}).get("system", {}).get("speed") or 25
    size_map = {"tiny": "Tiny", "sm": "Small", "med": "Medium", "lg": "Large"}
    size = size_map.get((items.get("ancestry", {}).get("system", {})
                         .get("size") or "med"), "Medium")

    lines = [
        "```statblock",
        "layout: Basic Pathfinder 2e Layout",
        f"name: {name}",
        f"level: {lvl}",
    ]
    for k in ("ancestry", "heritage", "background", "class"):
        if k in items:
            lines.append(f"{k}: {items[k]['name']} # unrendered")
    lines += [
        "",
        f"rare_03: {items.get('class', {}).get('name', '')} # class",
        f"rare_04: {items.get('background', {}).get('name', '')} # background",
        f"size: {size}",
    ]
    for n, t in enumerate([anc, "Humanoid"], start=1):
        if t:
            lines.append(f"trait_0{n}: {t}")
    perc = F.perception(actor, mods)
    lines += [
        "",
        f"modifier: {perc} # unrendered",
        "perception:",
        "  - name: Perception",
        f'    desc: "Perception +{perc}"',
    ]
    if langs:
        lines.append("languages:")
        lines += [f"- {language_link(l)}" for l in langs]
    if sk:
        lines.append("skills:")
        lines += [f"  {k.replace(' ', '_').lower()}: +{v}" for k, v in sk.items()]
    lines.append(f"abilityMods: [{','.join(str(mods[a]) for a in F.ABILITIES)}]")

    ac = F.armor_class(actor, mods)
    hp = F.max_hp(actor, mods)
    lines += [
        "",
        f"ac: {ac} # unrendered",
        "armorclass:",
        '  - name: "AC"',
        f'    desc: "{ac}; __Fort__: +{sv["fortitude"]}; '
        f'__Ref__: +{sv["reflex"]}; __Will__: +{sv["will"]}"',
        f"hp: {hp} # unrendered",
        "health:",
        '  - name: "HP"',
        f"    desc: {hp}",
        "saves: # unrendered",
        f"  fortitude: +{sv['fortitude']}",
        f"  reflex: +{sv['reflex']}",
        f"  will: +{sv['will']}",
        "",
        f"speed: {speed} feet",
    ]
    atks = []
    for w in actor.get("items", []):
        if w.get("type") != "weapon":
            continue
        line = weapon_line(actor, w, mods)
        if line:
            kind = "Ranged" if (w["system"].get("range")) else "Melee"
            atks.append((kind, line))
    if atks:
        lines.append("attacks:")
        for kind, line in sorted(atks, key=lambda x: x[0]):
            lines += [f'  - name: "{kind}"', f'    desc: "{line}"']
    lines.append("```")
    return lines


def feats_section(actor: dict) -> list[str]:
    fs = F.feats(actor)
    if not fs:
        return []
    order = ["classfeature", "class", "ancestryfeature", "ancestry",
             "skill", "general", "bonus"]
    label = {"classfeature": "Class Features", "class": "Class Feats",
             "ancestryfeature": "Ancestry Features", "ancestry": "Ancestry Feats",
             "skill": "Skill Feats", "general": "General Feats",
             "bonus": "Bonus Feats"}
    out = ["", "## Feats and Features", ""]
    seen = set()
    for cat in order + sorted({f["category"] for f in fs} - set(order)):
        group = [f for f in fs if f["category"] == cat and f["name"] not in seen]
        if not group:
            continue
        out.append(f"### {label.get(cat, cat.title() or 'Other')}")
        out.append("")
        for f in sorted(group, key=lambda x: (x["level"] or 0, x["name"])):
            seen.add(f["name"])
            lvl = f" *Level {f['level']}*" if f["level"] else ""
            out.append(f"**{f['name']}**{lvl}")
            if f["traits"]:
                out.append("")
                out.append("  ".join(f"`{t}`" for t in sorted(f["traits"])))
            if f["text"]:
                out += ["", f["text"]]
            out.append("")
    return out


COIN = {"platinum pieces": "pp", "gold pieces": "gp",
        "silver pieces": "sp", "copper pieces": "cp"}
COIN_ORDER = ["pp", "gp", "sp", "cp"]


def pretty_category(cat: str) -> str:
    """Foundry runs category words together, e.g. "ancestryfeature"."""
    if not cat:
        return "Other"
    for word in ("feature", "feat"):
        if cat.endswith(word) and cat != word:
            return f"{cat[:-len(word)].title()} {word.title()}s"
    return cat.title()


def currency_rows(inv: list[dict]) -> tuple[list[dict], list[str]]:
    """Separate coins from the rest of the inventory.

    Coins are quantity-times-denomination, so listing them beside a bedroll in
    a bulk-and-price table reads as nonsense.
    """
    coins, rest = {}, []
    for i in inv:
        denom = COIN.get(i["name"].strip().lower())
        if denom and i["qty"]:
            coins[denom] = coins.get(denom, 0) + int(i["qty"])
        elif denom:
            continue          # a zero-quantity coin pile is not worth a row
        else:
            rest.append(i)
    if not coins:
        return rest, []
    total_cp = (coins.get("pp", 0) * 1000 + coins.get("gp", 0) * 100
                + coins.get("sp", 0) * 10 + coins.get("cp", 0))
    out = ["### Currency", "", "| Denomination | Qty |", "|---|---|"]
    name = {"pp": "Platinum (pp)", "gp": "Gold (gp)",
            "sp": "Silver (sp)", "cp": "Copper (cp)"}
    for d in COIN_ORDER:
        if coins.get(d):
            out.append(f"| {name[d]} | {coins[d]:,} |")
    out.append(f"| **Total** | **{total_cp / 100:,.2f} gp** |")
    return rest, out + [""]


def inventory_section(actor: dict) -> list[str]:
    inv = F.inventory(actor)
    if not inv:
        return []
    inv, coin_rows = currency_rows(inv)
    worn = [i for i in inv if i["worn"] or i["invested"]]
    held = [i for i in inv if i["held"]]
    rest = [i for i in inv if i not in worn and i not in held]
    out = ["", "## Inventory", ""]

    def rows(title: str, group: list[dict]) -> list[str]:
        if not group:
            return []
        body = [f"### {title}", "", "| Item | Qty | Bulk | Price |", "|---|---|---|---|"]
        for i in sorted(group, key=lambda x: x["name"]):
            qty = i["qty"] if i["qty"] and i["qty"] != 1 else ""
            body.append(f"| {i['name']} | {qty} | {i['bulk'] or ''} | {i['price']} |")
        return body + [""]

    out += coin_rows
    out += rows("Held", held)
    out += rows("Worn and Invested", worn)
    out += rows("Carried", rest)
    return out


def build(path: Path, name: str, player: str, companion_of: str | None) -> str:
    actor = F.load(path)
    mods = F.ability_mods(actor)
    items = F.build_items(actor)
    fm = [
        "---",
        f'hp: "{F.max_hp(actor, mods)}"',
        f'ac: "{F.armor_class(actor, mods)}"',
        f'modifier: "{F.perception(actor, mods)}"',
        f'level: "{F.level(actor)}"',
        f"player: {player}",
    ]
    if companion_of:
        fm.append(f"companion_of: {companion_of}")
    if "class" in items:
        fm.append(f"class: {items['class']['name']}")
    if "ancestry" in items:
        fm.append(f"ancestry: {items['ancestry']['name']}")
    fm += [f"source: Foundry export {path.name}", "---", ""]
    body = statblock(actor, name, mods) + feats_section(actor) + inventory_section(actor)
    return "\n".join(fm + body).rstrip() + "\n"


def familiar_section(actor: dict, name: str, master: dict | None,
                     master_name: str) -> list[str]:
    """A familiar has almost no statistics of its own.

    Per Player Core, a familiar is its master's level, has 5 Hit Points per
    level, and uses the master's AC, saves and Perception. Its own export
    carries only the master's id, the creature type and its familiar abilities,
    so everything numeric here comes from the master's sheet.
    """
    creature = (((actor["system"].get("details") or {}).get("creature") or {})
                .get("value") or "Familiar")
    abilities = [i["name"] for i in actor.get("items", []) if i.get("type") == "action"]

    if master is None:
        lvl, ac, hp, perc, sv = 1, 10, 5, 0, {"fortitude": 0, "reflex": 0, "will": 0}
    else:
        mm = F.ability_mods(master)
        lvl = F.level(master)
        ac = F.armor_class(master, mm)
        hp = 5 * lvl
        perc = F.perception(master, mm)
        sv = F.saves(master, mm)

    body = [
        "",
        f"## Companion: {name}",
        "",
        f"*{creature} familiar. Uses {master_name}'s AC, saving throws and Perception,",
        f"and has 5 Hit Points per level. These values are derived from",
        f"{master_name}'s sheet; a familiar stores none of its own.*",
        "",
        "```statblock",
        "layout: Basic Pathfinder 2e Layout",
        f"name: {name}",
        f"level: {lvl}",
        "",
        "rare_03: Familiar # class",
        f"rare_04: {master_name}'s companion # background",
        "size: Tiny",
        f"trait_01: {creature}",
        "trait_02: Minion",
        "",
        f"modifier: {perc} # unrendered",
        "perception:",
        "  - name: Perception",
        f'    desc: "Perception +{perc}"',
        "abilityMods: [0,0,0,0,0,0]",
        "",
        f"ac: {ac} # unrendered",
        "armorclass:",
        '  - name: "AC"',
        f'    desc: "{ac}; __Fort__: +{sv["fortitude"]}; __Ref__: +{sv["reflex"]}; '
        f'__Will__: +{sv["will"]}"',
        f"hp: {hp} # unrendered",
        "health:",
        '  - name: "HP"',
        f"    desc: {hp}",
        "",
        "speed: 25 feet",
        "```",
        "",
    ]
    if abilities:
        body += [f"### {name}'s Abilities", ""]
        body += [f"- **{a}**" for a in sorted(abilities)]
        body.append("")
    return body


def party_note(path: Path) -> str:
    """The shared stash: everything the party owns as a group.

    Foundry's party actor also embeds a copy of each member, which is why the
    export is 588 KB against Gteek's 208 KB. Only the party's own items are
    read here; member sheets come from their own exports.

    Trade cargo is separated from adventuring gear. Ten bulk of Spices is
    freight for the Grim Zephyr, not something anyone puts in a backpack.
    """
    actor = F.load(path)
    inv = F.inventory(actor)
    inv, coin_rows = currency_rows(inv)

    cargo = [i for i in inv if (i["bulk"] or 0) >= 10]
    goods = [i for i in inv if i not in cargo]

    def table(title: str, group: list[dict], note: str = "") -> list[str]:
        if not group:
            return []
        body = [f"## {title}", ""]
        if note:
            body += [note, ""]
        body += ["| Item | Qty | Bulk | Unit price |", "|---|---|---|---|"]
        for i in sorted(group, key=lambda x: x["name"]):
            qty = i["qty"] if i["qty"] and i["qty"] != 1 else ""
            body.append(f"| {i['name']} | {qty} | {i['bulk'] or ''} | {i['price']} |")
        return body + [""]

    total = 0.0
    for i in cargo:
        m = re.match(r"(\d[\d,]*) gp", i["price"] or "")
        if m:
            total += float(m.group(1).replace(",", "")) * (i["qty"] or 1)

    fm = ["---", "aliases: [\"The Party\"]",
          "tags:", "- campaign/votgz/party",
          f"source: Foundry export {path.name}", "---", "",
          "# Party Stash", "",
          "Everything the group owns jointly, as opposed to the individual",
          "inventories on each character sheet.", ""]
    body = []
    if coin_rows:
        body += ["## Currency", ""] + coin_rows[2:]
    body += table("Trade Cargo", cargo,
                  f"Freight carried by the *Grim Zephyr*. Face value "
                  f"**{total:,.0f} gp**.")
    body += table("Shared Gear", goods)
    return "\n".join(fm + body).rstrip() + "\n"


# What each character contributes, and what leaves with them. Rotating GM means
# the GM does not play, so any one of these can be absent for a whole arc --
# the "if absent" column is the part that actually gets used at the table.
CONTRIBUTION: dict[str, tuple[str, str]] = {
    "Flick": (
        "Melee striker and sole party face. Only character trained in "
        "Thievery, and the only one in Performance.",
        "**No Thievery at all** -- locks, traps and pockets go uncovered. "
        "Performance vanishes. Intimidation falls to +4. Stealth drops from "
        "+8 to +5.",
    ),
    "Belegost": (
        "Front-line striker and the party's Athletics muscle: Shove, Trip and "
        "Grapple.",
        "Loses the best Athletics by +2 and a durable body in the front rank. "
        "Nobody else reliably controls position.",
    ),
    "Gripp": (
        "Chirurgeon alchemist -- healing, Crafting, and the only Society "
        "training. Backs up Deception and Diplomacy at +7.",
        "Crafting and Society drop to nothing. If Gteek is also away there is "
        "**no healing whatsoever**.",
    ),
    "Gteek": (
        "Cloistered cleric: the only spellcaster, the only Religion training, "
        "best Perception (+8) and best Will (+10). Sentinel Dedication keeps "
        "him in armour.",
        "**No spellcasting and no divine healing.** Religion goes uncovered, "
        "the party loses its best scout, and Will saves fall off sharply.",
    ),
}

STANDING_GAPS = [
    ("Ranged damage", "Espera and Vaelendil were both ranged; neither is "
     "playing. Gripp throws the occasional bomb but is built as a healer. "
     "Everyone else is melee."),
    ("Arcana", "Nobody trained. No identifying arcane items or wards."),
    ("Occultism", "Nobody trained. No reading curses or occult remains."),
]


def roster_note(built: list[tuple[str, str, dict, dict]]) -> str:
    """Coverage map for the party, written for a rotating-GM table.

    The interesting column is what disappears when a player takes the screen,
    because that is a two-month hole rather than a one-session one.
    """
    out = [
        "---",
        "tags:",
        "- campaign/votgz/party",
        "source: Generated from Foundry exports by tools/import-foundry",
        "---",
        "",
        "# Party Composition",
        "",
        "Who covers what, and what goes missing when they do not play.",
        "Under a rotating GM the person running the game is not playing their",
        "own character, so every row here is a hole that opens for a whole arc.",
        "",
        "## At a glance",
        "",
        "| Character | Player | AC | HP | Perc | Fort | Ref | Will |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for name, player, mods, stats in built:
        out.append(
            f"| [[campaigns/votgz/players/{name.replace(' ', '')}|{name}]] "
            f"| {player} | {stats['ac']} | {stats['hp']} | +{stats['perc']} "
            f"| +{stats['fort']} | +{stats['ref']} | +{stats['will']} |")
    out += ["", "## Contribution and absence", ""]
    for name, _player, _mods, _stats in built:
        brings, absent = CONTRIBUTION.get(
            name, ("_Not yet described._", "_Not yet described._"))
        out += [f"### {name}", "", f"**Brings.** {brings}", "",
                f"**If absent.** {absent}", ""]
    out += ["## Standing gaps", "",
            "Missing whoever is at the table:", ""]
    for gap, why in STANDING_GAPS:
        out.append(f"- **{gap}.** {why}")
    out += ["",
            "Arcana and Occultism are ordinary skills -- any class can train",
            "them with a skill increase. A caster is only needed to *counteract*",
            "curses and wards, not to identify them.",
            ""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--downloads", type=Path, default=Path.home() / "Downloads")
    ap.add_argument("--only", help="substring of the actor file stem")
    args = ap.parse_args()

    # Refuse to generate from derivations that do not reproduce Flick. This
    # caught a real failure: a stale __pycache__ from a negative test silently
    # gave every trained proficiency +3, and the output looked plausible.
    import subprocess
    probe = subprocess.run(
        [sys.executable, str(HERE / "check_flick.py")],
        capture_output=True, text=True)
    if probe.returncode != 0:
        print(probe.stdout, file=sys.stderr)
        print("self-check against Flick failed; refusing to generate", file=sys.stderr)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    # Familiars store only their master's id, so index every character first.
    master_by_id: dict[str, dict] = {}
    for f in args.downloads.glob("fvtt-Actor-*.json"):
        m = re.search(r"-([A-Za-z0-9]{16})\.json$", f.name)
        if m:
            a = F.load(f)
            if a.get("type") == "character":
                master_by_id[m.group(1)] = a
    # Familiars are emitted as a section of their master's page, so gather them
    # before anything is written.
    companions: dict[str, list[str]] = {}
    for stem, (name, _player, comp) in ROSTER.items():
        matches = list(args.downloads.glob(f"fvtt-Actor-{stem}-*.json"))
        if not matches:
            continue
        actor = F.load(matches[0])
        if actor.get("type") != "familiar":
            continue
        mid = (actor["system"].get("master") or {}).get("id")
        master = master_by_id.get(mid)
        companions.setdefault(comp or "?", []).extend(
            familiar_section(actor, name, master, comp or "?"))

    written = 0
    built: list[tuple[str, str, dict, dict]] = []
    for stem, (name, player, comp) in ROSTER.items():
        if args.only and args.only not in stem:
            continue
        matches = list(args.downloads.glob(f"fvtt-Actor-{stem}-*.json"))
        if not matches:
            print(f"  no export for {name} ({stem})", file=sys.stderr)
            continue
        if F.load(matches[0]).get("type") == "familiar":
            continue          # folded into the master's page below
        actor = F.load(matches[0])
        mods = F.ability_mods(actor)
        sv = F.saves(actor, mods)
        built.append((name, player, mods, {
            "ac": F.armor_class(actor, mods), "hp": F.max_hp(actor, mods),
            "perc": F.perception(actor, mods), "fort": sv["fortitude"],
            "ref": sv["reflex"], "will": sv["will"]}))
        text = build(matches[0], name, player, comp)
        extra = companions.get(name)
        if extra:
            text = text.rstrip() + "\n" + "\n".join(extra).rstrip() + "\n"
        dest = OUT / f"{name.replace(' ', '')}.md"
        dest.write_text(text, encoding="utf-8", newline="\n")
        note = f"  (+{', '.join(c for c, v in companions.items() if c == name)})" if extra else ""
        print(f"  {dest.name:18} {len(text):6}b{note}")
        written += 1

    # Remove standalone companion pages from earlier runs.
    for stale in ("SirPickles.md", "Drak.md"):
        f = OUT / stale
        if f.exists():
            f.unlink()
            print(f"  removed {stale} (now a section of its master's page)")
    party = list(args.downloads.glob("fvtt-Actor-the-party-*.json"))
    if party and not args.only:
        dest = OUT.parent / "Party Stash.md"
        dest.write_text(party_note(party[0]), encoding="utf-8", newline="\n")
        print(f"  {dest.name:20} {dest.stat().st_size:6}b")
        written += 1

    if built and not args.only:
        dest = OUT.parent / "Party Composition.md"
        dest.write_text(roster_note(built), encoding="utf-8", newline="\n")
        print(f"  {dest.name:20} {dest.stat().st_size:6}b")
        written += 1

    stale = OUT.parent / "PartyStash.md"
    if stale.exists():
        stale.unlink()
        print("  removed PartyStash.md (renamed to 'Party Stash.md')")

    print(f"\nWrote {written} notes to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
