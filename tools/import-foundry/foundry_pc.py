"""Derive a PF2e character sheet from a Foundry VTT actor export.

The export is sparse. Foundry stores only what a user chose -- ability boosts,
skill ranks, item lists -- and recomputes AC, HP, saves and attack bonuses at
runtime from the embedded ancestry, background, class and equipment items. None
of those derived numbers are in the JSON, so this module reimplements the parts
of the PF2e build rules needed to get them back.

Every derivation here is checked against Flick, whose sheet was entered by hand
from the Foundry UI and is therefore known good. Run `check_flick.py` after any
change; two values (intimidation, Sailing Lore) are known not to reproduce and
are documented there.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ABILITIES = ["str", "dex", "con", "int", "wis", "cha"]

# Proficiency rank -> bonus, before adding level. Untrained adds no level.
RANK_BONUS = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

SKILL_ABILITY = {
    "acrobatics": "dex", "arcana": "int", "athletics": "str", "crafting": "int",
    "deception": "cha", "diplomacy": "cha", "intimidation": "cha", "medicine": "wis",
    "nature": "wis", "occultism": "int", "performance": "cha", "religion": "wis",
    "society": "int", "stealth": "dex", "survival": "wis", "thievery": "dex",
}

BUILD_TYPES = {"ancestry", "heritage", "background", "class"}
INVENTORY_TYPES = {"weapon", "armor", "equipment", "consumable", "ammo", "backpack",
                   "treasure", "shield"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_items(actor: dict) -> dict[str, dict]:
    """The ancestry / heritage / background / class items, by type."""
    out: dict[str, dict] = {}
    for i in actor.get("items", []):
        if i.get("type") in BUILD_TYPES:
            out[i["type"]] = i
    return out


def ability_mods(actor: dict) -> dict[str, int]:
    """Ability modifiers from boosts and flaws.

    Everyone starts at 10 (+0). Each boost is +1 at this tier; a level-1
    character never reaches 18, where boosts start costing double, so the
    partial-boost rule is not needed for a level 1-4 party.
    """
    mods = dict.fromkeys(ABILITIES, 0)
    items = build_items(actor)

    def apply(entry: dict, sign: int) -> None:
        for slot in (entry or {}).values():
            vals = slot.get("value") or []
            pick = slot.get("selected")
            if pick:
                mods[pick] = mods.get(pick, 0) + sign
            elif len(vals) == 1:
                mods[vals[0]] = mods.get(vals[0], 0) + sign

    for kind in ("ancestry", "background"):
        sys = items.get(kind, {}).get("system", {})
        apply(sys.get("boosts"), +1)
        apply(sys.get("flaws"), -1)

    # The class key ability is a boost in its own right.
    cls = items.get("class", {}).get("system", {})
    key = (cls.get("keyAbility") or {})
    chosen = key.get("selected") or (key.get("value") or [None])[0]
    if chosen:
        mods[chosen] = mods.get(chosen, 0) + 1

    # Level-1 (and every 5th level) free boosts.
    for lvl, picks in ((actor["system"].get("build") or {})
                       .get("attributes", {}).get("boosts", {}).items()):
        for a in picks:
            mods[a] = mods.get(a, 0) + 1

    return mods


def level(actor: dict) -> int:
    return int(((actor["system"].get("details") or {}).get("level") or {}).get("value") or 1)


def max_hp(actor: dict, mods: dict[str, int]) -> int:
    """Ancestry HP + (class HP + Con) per level, after rule elements.

    Ancestry HP is not simply the ancestry item's value. Sturdy heritages
    replace it: Unbreakable Goblin overrides ancestryhp from 6 to 10 rather
    than adding 4, so the override has to be applied before multiplying.
    """
    items = build_items(actor)
    lvl = level(actor)
    anc = items.get("ancestry", {}).get("system", {}).get("hp") or 0
    anc = apply_ancestry_hp_rules(actor, anc)
    cls = items.get("class", {}).get("system", {}).get("hp") or 0
    return anc + (cls + mods.get("con", 0)) * lvl + flat_hp(actor, lvl)


def apply_ancestry_hp_rules(actor: dict, base: int) -> int:
    """ActiveEffectLike rules touching system.attributes.ancestryhp."""
    for i in actor.get("items", []):
        for rule in i.get("system", {}).get("rules") or []:
            if (rule.get("key") != "ActiveEffectLike"
                    or rule.get("path") != "system.attributes.ancestryhp"):
                continue
            val = rule.get("value")
            if not isinstance(val, (int, float)):
                continue
            mode = rule.get("mode")
            if mode == "override":
                base = int(val)
            elif mode == "upgrade":
                base = max(base, int(val))
            elif mode in ("add", "multiply"):
                base = base + int(val) if mode == "add" else base * int(val)
    return base


def flat_hp(actor: dict, lvl: int) -> int:
    """Extra HP from FlatModifier rules, e.g. a toughness-style feat."""
    total = 0
    for i in actor.get("items", []):
        for rule in i.get("system", {}).get("rules") or []:
            if rule.get("key") != "FlatModifier" or rule.get("selector") != "hp":
                continue
            val = rule.get("value")
            if isinstance(val, (int, float)):
                total += int(val)
            elif isinstance(val, str):
                m = re.search(r"@actor\.level\s*\*\s*(\d+)", val)
                if m:
                    total += int(m.group(1)) * lvl
                elif val.lstrip("+-").isdigit():
                    total += int(val)
    return total


def _class_sys(actor: dict) -> dict:
    return build_items(actor).get("class", {}).get("system", {}) or {}


PROF_PATH = re.compile(r"^system\.proficiencies\.(defenses|attacks)\.(\w+)\.rank$")


def granted_proficiencies(actor: dict) -> dict[tuple[str, str], int]:
    """Armor and weapon proficiency raised by a feat rather than by the class.

    Sentinel Dedication is the case that matters here: it trains its holder in
    light, medium and heavy armor, which is why a cloistered cleric can be
    found wearing leather. Without this the derived AC is several points low.

    Predicates are not evaluated. A rule on an item the character actually has
    is assumed to apply, which holds for dedication feats but would not for a
    conditional effect.
    """
    base: dict[tuple[str, str], int] = {}
    cls = _class_sys(actor)
    for kind, key in (("defenses", "defenses"), ("attacks", "attacks")):
        for slot, rank in (cls.get(key) or {}).items():
            if isinstance(rank, int):
                base[(kind, slot)] = rank

    pending = []
    for i in actor.get("items", []):
        for rule in i.get("system", {}).get("rules") or []:
            if rule.get("key") != "ActiveEffectLike":
                continue
            m = PROF_PATH.match(str(rule.get("path") or ""))
            if m:
                pending.append(((m.group(1), m.group(2)), rule.get("value")))

    out = dict(base)
    # Sentinel's light and medium entries reference each other, so settle by
    # repeating until nothing changes.
    for _ in range(4):
        changed = False
        for key, val in pending:
            n = eval_formula(val, actor, out)
            if n is not None and n > out.get(key, 0):
                out[key] = n
                changed = True
        if not changed:
            break
    return {k: v for k, v in out.items() if v > base.get(k, 0)}


REF = re.compile(r"@actor\.system\.proficiencies\.(defenses|attacks)\.(\w+)\.rank")


def eval_formula(val, actor: dict, ranks: dict[tuple[str, str], int]) -> int | None:
    """Evaluate the small formula language Foundry uses in rule values.

    Only max, min, ternary and gte appear in the rules this importer meets.
    Anything else returns None and is skipped rather than guessed at.
    """
    if isinstance(val, (int, float)):
        return int(val)
    if not isinstance(val, str):
        return None
    expr = REF.sub(lambda m: str(ranks.get((m.group(1), m.group(2)), 0)), val)
    expr = expr.replace("@actor.level", str(level(actor)))
    if re.search(r"[@a-zA-Z_]", expr.replace("max", "").replace("min", "")
                 .replace("ternary", "").replace("gte", "")):
        return None
    env = {
        "max": max, "min": min,
        "ternary": lambda c, a, b: a if c else b,
        "gte": lambda a, b: a >= b,
        "__builtins__": {},
    }
    try:
        return int(eval(expr, env, {}))  # noqa: S307 - inputs constrained above
    except Exception:
        return None


def perception(actor: dict, mods: dict[str, int]) -> int:
    rank = _class_sys(actor).get("perception") or 0
    return RANK_BONUS[rank] + (level(actor) if rank else 0) + mods.get("wis", 0)


def saves(actor: dict, mods: dict[str, int]) -> dict[str, int]:
    st = _class_sys(actor).get("savingThrows") or {}
    lvl = level(actor)
    pair = {"fortitude": "con", "reflex": "dex", "will": "wis"}
    out = {}
    for name, ab in pair.items():
        rank = st.get(name) or 0
        out[name] = RANK_BONUS[rank] + (lvl if rank else 0) + mods.get(ab, 0)
    return out


def worn_armor(actor: dict) -> dict | None:
    """The armor actually being worn.

    Keyed on carryType rather than inSlot: some items omit inSlot entirely
    (Vaelendil's Rattan Armor does), and treating those as unworn silently
    reports the character as unarmoured.
    """
    for i in actor.get("items", []):
        if i.get("type") != "armor":
            continue
        eq = i["system"].get("equipped") or {}
        if eq.get("carryType") == "worn" and eq.get("inSlot") is not False:
            return i
    return None


def armor_class(actor: dict, mods: dict[str, int]) -> int:
    lvl = level(actor)
    defenses = dict(_class_sys(actor).get("defenses") or {})
    for (kind, slot), rank in granted_proficiencies(actor).items():
        if kind == "defenses":
            defenses[slot] = max(defenses.get(slot) or 0, rank)
    armor = worn_armor(actor)
    if armor is None:
        rank = defenses.get("unarmored") or 0
        return 10 + mods.get("dex", 0) + RANK_BONUS[rank] + (lvl if rank else 0)
    s = armor["system"]
    cap = s.get("dexCap")
    dex = mods.get("dex", 0) if cap is None else min(mods.get("dex", 0), cap)
    rank = defenses.get(s.get("category") or "light") or 0
    potency = ((s.get("runes") or {}).get("potency") or 0)
    return 10 + dex + (s.get("acBonus") or 0) + potency + RANK_BONUS[rank] + (lvl if rank else 0)


def skills(actor: dict, mods: dict[str, int]) -> dict[str, int]:
    """Trained skills only.

    Ranks come from system.skills, plus anything the background or class trains.
    Skills the player set in the Foundry UI after exporting will be missing;
    that is a limit of the export, not of this function.
    """
    lvl = level(actor)
    ranks: dict[str, int] = {}
    items = build_items(actor)
    for kind in ("background", "class"):
        t = (items.get(kind, {}).get("system", {}).get("trainedSkills") or {})
        for s in t.get("value") or []:
            ranks[s] = max(ranks.get(s, 0), 1)
    for name, v in (actor["system"].get("skills") or {}).items():
        ranks[name] = max(ranks.get(name, 0), int(v.get("rank") or 0))
    # Feats and class features can train a skill through a rule element rather
    # than through system.skills. Braggart trains Intimidation this way, which
    # is why it is absent from the actor's own skill list.
    for name, rank in granted_skill_ranks(actor).items():
        ranks[name] = max(ranks.get(name, 0), rank)
    out = {}
    for name, rank in sorted(ranks.items()):
        if rank <= 0:
            continue
        ab = SKILL_ABILITY.get(name, "int")
        out[name] = RANK_BONUS[rank] + lvl + mods.get(ab, 0)
    return out


SKILL_RANK_PATH = re.compile(r"^system\.skills\.([a-z]+)\.rank$")


def granted_skill_ranks(actor: dict) -> dict[str, int]:
    """Skill ranks set by ActiveEffectLike rules on feats and class features."""
    out: dict[str, int] = {}
    for i in actor.get("items", []):
        for rule in i.get("system", {}).get("rules") or []:
            if rule.get("key") != "ActiveEffectLike":
                continue
            m = SKILL_RANK_PATH.match(str(rule.get("path") or ""))
            val = rule.get("value")
            if not m or not isinstance(val, (int, float)):
                continue
            name, val = m.group(1), int(val)
            out[name] = max(out[name], val) if name in out else val
    return out


def precision_damage(actor: dict) -> int:
    """Flat precision damage added to qualifying melee Strikes.

    Swashbuckler's Precise Strike is the case that matters for this party. Its
    size lives in an ActiveEffectLike as "ceil(@actor.level/4) + 1"; only that
    one formula shape is evaluated, and anything else is ignored rather than
    guessed at.
    """
    lvl = level(actor)
    for i in actor.get("items", []):
        for rule in i.get("system", {}).get("rules") or []:
            path = str(rule.get("path") or "")
            if not path.endswith("preciseStrike"):
                continue
            val = str(rule.get("value") or "")
            m = re.match(r"ceil\(@actor\.level\s*/\s*(\d+)\)\s*\+\s*(\d+)", val)
            if m:
                return -(-lvl // int(m.group(1))) + int(m.group(2))
    return 0


def lores(actor: dict, mods: dict[str, int]) -> dict[str, int]:
    """Lore skills. Rank is not stored on the item, so trained is assumed."""
    lvl = level(actor)
    out = {}
    for i in actor.get("items", []):
        if i.get("type") == "lore":
            out[f"{i['name']} Lore"] = RANK_BONUS[1] + lvl + mods.get("int", 0)
    return out


def attack_bonus(actor: dict, weapon: dict, mods: dict[str, int]) -> tuple[int, str]:
    """Attack modifier and the ability used.

    Finesse and all ranged weapons use Dexterity; everything else uses Strength.
    """
    s = weapon["system"]
    traits = s.get("traits", {}).get("value") or []
    ranged = bool((s.get("range") or 0)) or s.get("category") == "ranged"
    ability = "dex" if ("finesse" in traits or ranged) else "str"
    if ability == "dex" and not ranged and mods.get("str", 0) > mods.get("dex", 0):
        ability = "str"
    prof = dict(_class_sys(actor).get("attacks") or {})
    for (kind, slot), r in granted_proficiencies(actor).items():
        if kind == "attacks":
            prof[slot] = max(prof.get(slot) or 0, r)
    rank = prof.get(s.get("category") or "simple", prof.get("simple", 0)) or 0
    potency = ((s.get("runes") or {}).get("potency") or 0)
    bonus = (RANK_BONUS[rank] + (level(actor) if rank else 0)
             + mods.get(ability, 0) + potency + (s.get("bonus") or {}).get("value", 0))
    return bonus, ability


def inventory(actor: dict) -> list[dict]:
    out = []
    for i in actor.get("items", []):
        if i.get("type") not in INVENTORY_TYPES:
            continue
        s = i["system"]
        eq = s.get("equipped") or {}
        out.append({
            "name": i["name"],
            "type": i["type"],
            "qty": s.get("quantity") or 1,
            "carry": eq.get("carryType"),
            "held": bool(eq.get("handsHeld")),
            "worn": eq.get("inSlot") is True,
            "invested": eq.get("invested") is True,
            "bulk": ((s.get("bulk") or {}).get("value")),
            "price": price_str(s.get("price")),
        })
    return out


def price_str(price: dict | None) -> str:
    v = ((price or {}).get("value")) or {}
    parts = [f"{v[c]} {c}" for c in ("pp", "gp", "sp", "cp") if v.get(c)]
    return ", ".join(parts)


def feats(actor: dict) -> list[dict]:
    out = []
    for i in actor.get("items", []):
        if i.get("type") != "feat":
            continue
        s = i["system"]
        out.append({
            "name": i["name"],
            "category": s.get("category") or "",
            "level": (s.get("level") or {}).get("value"),
            "traits": (s.get("traits") or {}).get("value") or [],
            "actions": (s.get("actions") or {}).get("value"),
            "text": clean_html(((s.get("description") or {}).get("value")) or ""),
        })
    return out


UUID_LINK = re.compile(r"@UUID\[[^\]]+\]\{([^}]*)\}")
CHECK = re.compile(r"@Check\[[^\]]*\](?:\{([^}]*)\})?")
DAMAGE = re.compile(r"@Damage\[([^\]]*)\](?:\{([^}]*)\})?")
TEMPLATE = re.compile(r"@Template\[[^\]]*\](?:\{([^}]*)\})?")
LOCALIZE = re.compile(r"@Localize\[[^\]]*\]")


def clean_html(html: str) -> str:
    """Foundry rich text to plain markdown."""
    t = html
    t = UUID_LINK.sub(r"\1", t)
    t = CHECK.sub(lambda m: m.group(1) or "check", t)
    t = DAMAGE.sub(lambda m: m.group(2) or m.group(1).split("[")[0], t)
    t = TEMPLATE.sub(lambda m: m.group(1) or "area", t)
    t = LOCALIZE.sub("", t)
    t = re.sub(r"<hr\s*/?>", "\n\n", t, flags=re.I)
    t = re.sub(r"</p>|<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"<li[^>]*>", "\n- ", t, flags=re.I)
    t = re.sub(r"<strong>(.*?)</strong>", r"**\1**", t, flags=re.I | re.S)
    t = re.sub(r"<em>(.*?)</em>", r"*\1*", t, flags=re.I | re.S)
    t = re.sub(r"<[^>]+>", "", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
          .replace("&#39;", "'").replace("&mdash;", "--").replace("&ndash;", "-"))
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()
