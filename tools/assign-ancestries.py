#!/usr/bin/env python3
"""Assign PF2e heritages to Xuartlek's eleven reachable worlds.

Heritages are placed by theme, not in ancestry blocks: rats live in sewers and
in ruins and in snow, so ratfolk heritages scatter rather than all landing on
the post-apocalyptic world. The rules of thumb, from Kevan:

1. No ancestry except human, elf and dwarf appears on every world.
2. No heritage on more than ~half the worlds (6 of 11; 7-8 tolerated for human).
3. An ancestry may be on several worlds, but need not be.
4. If an ancestry spans worlds, no more than ~half its heritages share a world.
5. Ancestry count per world should be broadly even.
6. Heritage count per world should be broadly even.
7. A themed heritage goes to the matching world unless that breaks a rule above.
8. Common sense wins.
9. Exceptions are allowed where they make sense, and are named here so a
   breach is either deliberate or a bug, never ambiguous.

On oceans: every world except Profugae and Khashayar has one, so aquatic
ancestries are not confined to Shubae. Khashayar's sister world -- the ocean
hanging in its sky -- has no ancestries at all.

Reads the existing spreadsheet for the 123 already-assigned rows, adds the 62
this file decides, and reports every rule breach rather than silently fixing
one. Run from the repo root.
"""
import csv
import json
import pathlib
import re
import collections

WORLDS = ["Arborisle", "Profugae", "Tertara", "Shubae", "Langsevain", "Hrimgard",
          "Emerraine", "Khashayar", "Qigang", "Strafmack", "Mortuus Rex"]

# The spreadsheet predates the rename; Nevermelt is Hrimgard.
LEGACY_WORLDS = [w if w != "Hrimgard" else "Nevermelt" for w in WORLDS]

BIG_THREE = {"Human", "Elf", "Dwarf"}

# Heritage -> worlds. Keyed by (ancestry, heritage) exactly as AoN names them.
NEW: dict[tuple[str, str], list[str]] = {
    # Automaton: built things. Langsevain builds them, Emerraine has the
    # industry but no magic, Mortuus Rex keeps the old ones running.
    ("Automaton", "Defensive Automaton"):    ["Mortuus Rex", "Langsevain"],
    ("Automaton", "Hunter Automaton"):       ["Strafmack", "Arborisle"],
    ("Automaton", "Mage Automaton"):         ["Tertara", "Qigang"],
    ("Automaton", "Newly Minted Automaton"): ["Langsevain", "Emerraine"],
    ("Automaton", "Sharpshooter Automaton"): ["Emerraine", "Langsevain"],
    ("Automaton", "Warrior Automaton"):      ["Mortuus Rex", "Strafmack"],

    # Yaksha: guardian spirits. Qigang is home; the "Deny" heritages are
    # refusals of a fate, which suits worlds that are losing something.
    ("Yaksha", "Respite of a Thousand Roofs"): ["Qigang", "Langsevain"],
    ("Yaksha", "Respite of Cloudless Paths"):  ["Qigang", "Khashayar"],
    ("Yaksha", "Respite of Loam and Leaf"):    ["Arborisle", "Tertara"],
    ("Yaksha", "Deny Lady Nanbyo's Charity"):  ["Mortuus Rex", "Strafmack"],
    ("Yaksha", "Deny the Firstborn Pursuit"):  ["Tertara", "Shubae"],
    ("Yaksha", "Deny the Traitor's Rebirth"):  ["Qigang", "Mortuus Rex"],

    # Yaoguai: things that became people. Each is born of what it was.
    ("Yaoguai", "Born of Animal"):     ["Arborisle", "Qigang"],
    ("Yaoguai", "Born of Celestial"):  ["Tertara", "Qigang"],
    ("Yaoguai", "Born of Elements"):   ["Qigang", "Strafmack"],
    ("Yaoguai", "Born of Item"):       ["Langsevain", "Emerraine"],
    ("Yaoguai", "Born of Vegetation"): ["Arborisle", "Tertara"],

    # Sarangay: moon-phase heritages, so they follow the worlds that have
    # moons worth naming -- Qigang has six, Tertara and Shubae three each.
    ("Sarangay", "Full Moon Sarangay"):   ["Qigang", "Tertara"],
    ("Sarangay", "Half Moon Sarangay"):   ["Tertara", "Shubae"],
    ("Sarangay", "New Moon Sarangay"):    ["Mortuus Rex", "Profugae"],
    ("Sarangay", "Waning Moon Sarangay"): ["Shubae", "Khashayar"],
    ("Sarangay", "Waxing Moon Sarangay"): ["Qigang", "Hrimgard"],

    # Jotunborn: giant-blooded, so the frozen moon and the world that swings
    # between fire and ice. Weaver and Plane-Hopper travel further.
    ("Jotunborn", "Keeper Jotunborn"):       ["Hrimgard", "Mortuus Rex"],
    ("Jotunborn", "Plane-Hopper Jotunborn"): ["Tertara", "Qigang"],
    ("Jotunborn", "Sage Jotunborn"):         ["Hrimgard", "Langsevain"],
    ("Jotunborn", "Warrior Jotunborn"):      ["Strafmack", "Hrimgard"],
    ("Jotunborn", "Weaver Jotunborn"):       ["Arborisle", "Emerraine"],

    # Wayang: shadow-touched. Mortuus Rex is a world of perpetual darkness,
    # which suits them, but they are city people first.
    ("Wayang", "Shadow of the Courtier"):  ["Qigang", "Langsevain"],
    ("Wayang", "Shadow of the Hermit"):    ["Mortuus Rex", "Arborisle"],
    ("Wayang", "Shadow of the Sailor"):    ["Shubae", "Khashayar"],
    ("Wayang", "Shadow of the Smith"):     ["Langsevain", "Hrimgard"],
    ("Wayang", "Shadow of the Wanderer"):  ["Khashayar", "Strafmack"],

    # Surki: insectile, built for hostile ground.
    ("Surki", "Breaker Surki"):   ["Profugae", "Langsevain"],
    ("Surki", "Elytron Surki"):   ["Arborisle", "Tertara"],
    ("Surki", "Hardshell Surki"): ["Khashayar", "Strafmack"],
    ("Surki", "Lantern Surki"):   ["Mortuus Rex", "Profugae"],

    # Awakened Animal: the forest world first, then wherever that animal lives.
    ("Awakened Animal", "Climbing Animal"): ["Arborisle", "Qigang"],
    ("Awakened Animal", "Flying Animal"):   ["Tertara", "Hrimgard"],
    ("Awakened Animal", "Running Animal"):  ["Strafmack", "Khashayar"],
    ("Awakened Animal", "Swimming Animal"): ["Shubae", "Emerraine"],

    # Sprite: fey. Gandharva are celestial musicians, which is Tertara exactly.
    ("Sprite", "Dijiang"):   ["Tertara", "Qigang"],
    ("Sprite", "Gandharva"): ["Tertara", "Shubae"],
    ("Sprite", "Kanchil"):   ["Arborisle", "Qigang"],
    ("Sprite", "Leungli"):   ["Shubae", "Hrimgard"],

    # Singles: additions to ancestries already placed, so these mostly fill
    # thin worlds rather than reinforcing where their ancestry already sits.
    ("Leshy", "Chrysanthemum Leshy"):   ["Qigang", "Tertara"],
    # Peaches are the most distinctly eastern of the leshy, so this is the one
    # that moves off Arborisle rather than sitting on both.
    ("Leshy", "Peachchild Leshy"):      ["Qigang"],
    ("Tanuki", "Courageous Tanuki"):    ["Qigang", "Shubae"],
    ("Goblin", "Dokkaebi Goblin"):      ["Qigang", "Emerraine"],
    ("Minotaur", "Glacier Cavern Minotaur"): ["Hrimgard", "Strafmack"],
    ("Halfling", "Hillock Halfling"):   ["Emerraine", "Arborisle"],
    ("Athamaru", "Kaleidoscopic Athamaru"): ["Shubae", "Tertara"],
    ("Gnome", "Kijimuna Gnome"):        ["Qigang", "Arborisle"],
    ("Poppet", "Tsukumogami Poppet"):   ["Qigang", "Langsevain"],

    # The one row the spreadsheet left blank. Elemental-touched kobolds belong
    # where the elements are visible from the ground: Qigang's six elemental
    # rings, and the world that swings between fire and ice every year.
    ("Kobold", "Elementheart"): ["Qigang", "Strafmack"],

}

# Rule 1: only human, elf and dwarf are everywhere. Catfolk and ratfolk had
# crept onto all eleven worlds between them. Pulled back to the worlds where
# each heritage actually means something -- both stay widespread, neither is
# universal. These use the spreadsheet's short names, which omit the ancestry.
REASSIGNED_SPREAD: dict[tuple[str, str], list[str]] = {
    ("Catfolk", "Hunting"):    ["Arborisle", "Strafmack"],
    ("Catfolk", "Nine Lives"): ["Qigang", "Tertara"],
    ("Catfolk", "Winter"):     ["Hrimgard", "Strafmack"],
    ("Ratfolk", "Longsnout"):  ["Arborisle", "Shubae", "Emerraine"],
    ("Ratfolk", "Sewer"):      ["Langsevain", "Emerraine", "Qigang"],

    # Aquatic ancestries had all five merfolk and all five athamaru on Shubae.
    # Shubae is the ocean world, but nine of the eleven have seas, so these
    # spread to the ones whose water suits the heritage. Never Profugae or
    # Khashayar, which have none, and never Khashayar's sister world.
    ("Merfolk", "Abyssal"):     ["Mortuus Rex", "Hrimgard"],
    ("Merfolk", "Carcharodon"): ["Shubae", "Emerraine"],
    ("Merfolk", "Pelagic"):     ["Shubae", "Tertara"],
    ("Merfolk", "Reef"):        ["Qigang", "Shubae"],
    ("Merfolk", "Sailfish"):    ["Emerraine", "Langsevain"],
    ("Athamaru", "Coral"):      ["Shubae", "Qigang"],
    ("Athamaru", "Hopeful"):    ["Tertara", "Emerraine"],
    ("Athamaru", "Quilled"):    ["Hrimgard", "Strafmack"],
    # The spreadsheet spells this "Kaleidscopic"; AoN has "Kaleidoscopic
    # Athamaru". Same heritage, so the typo row is emptied rather than left
    # to double-count.
    ("Athamaru", "Kaleidscopic"):          [],
    ("Athamaru", "Kaleidoscopic Athamaru"): ["Shubae", "Tertara"],
}

# Rule 9. Each of these is a rule-4 breach kept on purpose, because spreading
# the ancestry would read worse than the imbalance does.
EXEMPT_RULE_4 = {
    # Six-tailed fox spirits are Tian Xia to the bone, and Qigang is the only
    # world drawing on that. Scattering them would dilute both.
    "Kitsune",
    # Ancestries whose whole identity is one climate.
    "Jotunborn",   # giant-blooded, and Hrimgard is the frozen moon
    "Leshy",       # plant people, and Arborisle is the world the forest won
    # Rule 1 already treats the big three as universal. Rule 4 has to agree, or
    # human trips every cap it meets: with three heritages, any world carrying
    # all three breaches a cap of two.
    *BIG_THREE,
}

# Strafmack had become what Mortuus Rex was: everything hardy landed there, 51
# heritages against Hrimgard's 25. The two are neighbours in theme -- Strafmack
# swings between fire and ice, Hrimgard simply is ice -- so the ice-flavoured
# entries move across. What stays on Strafmack is the heat, the height and the
# sky-reading, which is what makes that world distinct rather than merely cold.
ICE_TO_HRIMGARD: dict[tuple[str, str], list[str]] = {
    ("Catfolk", "Winter"):          ["Hrimgard"],
    ("Goblin", "Snow"):             ["Hrimgard", "Profugae"],
    ("Human", "Wintertouched"):     ["Hrimgard", "Khashayar", "Strafmack"],
    ("Orc", "Winter"):              ["Hrimgard"],
    ("Ratfolk", "Snow"):            ["Hrimgard"],
    ("Minotaur", "Glacier"):        ["Hrimgard"],
    ("Minotaur", "Glacier Cavern Minotaur"): ["Hrimgard"],
    ("Minotaur", "Ghost Bull"):     ["Hrimgard", "Mortuus Rex"],
    ("Centaur", "Mottle-Coat"):     ["Hrimgard", "Arborisle"],
    ("Centaur", "Stoutheart"):      ["Hrimgard", "Mortuus Rex"],
    ("Dwarf", "Oathkeeper"):        ["Hrimgard", "Langsevain"],
    ("Jotunborn", "Warrior Jotunborn"): ["Hrimgard"],
    ("Athamaru", "Quilled"):        ["Hrimgard", "Shubae"],
    ("Samsaran", "Mountaineer"):    ["Hrimgard", "Qigang"],
    ("Halfling", "Twilight"):       ["Hrimgard", "Mortuus Rex"],
}

# Profugae keeps its low ancestry count on purpose -- a sunless world after a
# catastrophe should be thinly peopled, and rule 9 covers that. But survivors
# adapt, and a few underground heritages would have come out of the dark rather
# than into it. These are additions, not a backfill to hit a target.
PROFUGAE_ADAPTED: dict[tuple[str, str], list[str]] = {
    ("Awakened Animal", "Climbing Animal"): ["Arborisle", "Profugae"],
    ("Automaton", "Defensive Automaton"):   ["Mortuus Rex", "Profugae"],
    ("Tengu", "Dogtooth"):                  ["Profugae", "Qigang"],
    ("Catfolk", "Clawed"):                  ["Langsevain", "Profugae"],
}

# Last pass. Three ancestries still clustered past their cap, and Khashayar was
# the thinnest world at 24. These move the entries whose theme suits a desert,
# a long night or a trade road better than where they were.
FINAL_SPREAD: dict[tuple[str, str], list[str]] = {
    # Gnome: wellspring gnomes draw on raw magic, which is Tertara's business,
    # and sensate gnomes chase new sensation rather than one workshop city.
    ("Gnome", "Wellspring"): ["Tertara", "Qigang"],
    ("Gnome", "Sensate"):    ["Khashayar", "Shubae"],

    # Goblin: charhide belongs where it is hot, and irongut where food is
    # scarce enough that eating anything is a survival trait.
    ("Goblin", "Charhide"):  ["Khashayar", "Strafmack"],
    ("Goblin", "Irongut"):   ["Khashayar", "Profugae"],

    # Tanuki: ascetics and the even-tempered suit the disciplined worlds more
    # than the forest one.
    ("Tanuki", "Ascetic"):        ["Qigang", "Khashayar"],
    ("Tanuki", "Even-tempered"):  ["Qigang", "Tertara"],
}

# The spreadsheet's typo row for Kaleidoscopic Athamaru, emptied on purpose so
# it does not double-count. Not a missing assignment.
KNOWN_EMPTY = {("Athamaru", "Kaleidscopic")}

# Rule 9, for worlds rather than ancestries.
EXEMPT_SPREAD = {"Qigang"}

# Emerraine is the world where magic does not work, so most heritages have no
# business being common there and it sat lowest at 25. The fix is not to pad
# it, but to notice that the mundane heritages -- the ones that are muscle,
# nerve and stubbornness rather than any kind of spark -- belong on the
# industrial world more than they belong anywhere else.
EMERRAINE_MUNDANE: dict[tuple[str, str], list[str]] = {
    ("Halfling", "Gutsy"):       ["Strafmack", "Emerraine"],
    ("Halfling", "Observant"):   ["Emerraine", "Langsevain"],
    ("Dwarf", "Forge"):          ["Langsevain", "Emerraine"],
    ("Orc", "Battle-Ready"):     ["Strafmack", "Emerraine"],
    ("Minotaur", "Littlehorn"):  ["Emerraine", "Strafmack"],
    ("Centaur", "Ponygait"):     ["Shubae", "Emerraine"],
    ("Lizardfolk", "Frilled"):   ["Strafmack", "Emerraine"],
    ("Catfolk", "Hunting"):      ["Arborisle", "Emerraine"],
}

# Arborisle ended up highest and Khashayar lowest, so the last four moves go
# between them. Each is a heritage that reads as arid or hard-country rather
# than forest: Khashayar is a desert world with week-long days, which suits an
# ambush hunter, a tough-jawed kobold and a venomous serpent at least as well
# as a rainforest does.
ARID_TO_KHASHAYAR: dict[tuple[str, str], list[str]] = {
    ("Kobold", "Strongjaw"):     ["Khashayar"],
    ("Nagaji", "Venomshield"):   ["Khashayar"],
    ("Tengu", "Taloned"):        ["Khashayar", "Strafmack"],
    # Titan nagaji would make four of six on Khashayar, past the cap, so this
    # one goes to the other hard-country worlds instead.
    ("Nagaji", "Titan"):         ["Strafmack", "Mortuus Rex"],
}

# Mortuus Rex originally collected every ancestry with an "evil" reputation --
# all seven hobgoblins, all six nagaji, four of seven orcs. That is a read of
# the ancestries, not of the world. Mortuus Rex is where darkness won a
# thousand years ago and one bastion of light is still holding, so what belongs
# there is the undead-adjacent, the lightless and the besieged. A hobgoblin is
# a disciplined soldier, which suits an industrial world or a war footing
# anywhere; it is not a creature of darkness.
#
# These entries replace the spreadsheet's rows outright.
REASSIGNED: dict[tuple[str, str], list[str]] = {
    # Hobgoblin: militaristic and industrious. Smokeworker is a coal-smoke
    # world in one word. Warmarch stays -- a bastion under permanent siege is
    # exactly where a marching company belongs.
    ("Hobgoblin", "Elfbane"):     ["Arborisle", "Tertara"],
    ("Hobgoblin", "Runtboss"):    ["Profugae", "Strafmack"],
    ("Hobgoblin", "Shortshanks"): ["Strafmack", "Khashayar"],
    ("Hobgoblin", "Smokeworker"): ["Langsevain", "Emerraine"],
    ("Hobgoblin", "Steelskin"):   ["Langsevain", "Hrimgard"],
    ("Hobgoblin", "Warmarch"):    ["Mortuus Rex", "Emerraine"],
    ("Hobgoblin", "Warrenbred"):  ["Profugae", "Mortuus Rex"],

    # Nagaji: serpents want heat, water and jungle, not a dark world.
    ("Nagaji", "Hooded"):        ["Khashayar", "Qigang"],
    ("Nagaji", "Sacred"):        ["Tertara", "Qigang"],
    ("Nagaji", "Shimmertongue"): ["Tertara", "Shubae"],
    ("Nagaji", "Titan"):         ["Strafmack", "Arborisle"],
    ("Nagaji", "Venomshield"):   ["Khashayar", "Arborisle"],
    ("Nagaji", "Whipfang"):      ["Khashayar", "Shubae"],

    # Orc: Grave orcs are literally death-touched, so that one stays. The rest
    # were there for reputation alone.
    ("Orc", "Badlands"):     ["Khashayar", "Strafmack"],
    ("Orc", "Battle-Ready"): ["Strafmack", "Langsevain"],
    ("Orc", "Grave"):        ["Mortuus Rex", "Profugae"],
    ("Orc", "Hold-Scarred"): ["Hrimgard", "Mortuus Rex"],
}

# Circumstantial versatile heritages: you become one, you are not from
# somewhere. A dhampir is made by a vampire and a duskwalker by dying, so
# neither says anything about where you were born. The spreadsheet placed
# several of these -- mostly on Mortuus Rex, again for being spooky -- so they
# are cleared rather than reassigned.
CIRCUMSTANTIAL = {"Changeling", "Dhampir", "Duskwalker", "Nephilim",
                  "Reflection", "Hungerseed", "Aasimaar"}


def load_existing(path: pathlib.Path) -> dict[tuple[str, str], list[str]]:
    out: dict[tuple[str, str], list[str]] = {}
    anc = None
    for r in csv.DictReader(path.open()):
        if r["Ancestry"].strip():
            anc = r["Ancestry"].strip()
        h = r["Heritage"].strip()
        if not h:
            continue
        out[(anc, h)] = [w for w, legacy in zip(WORLDS, LEGACY_WORLDS)
                         if (r.get(legacy) or "").strip().upper() == "TRUE"]
    return out


def check(assign: dict[tuple[str, str], list[str]]) -> list[str]:
    problems: list[str] = []
    per_anc_world = collections.defaultdict(collections.Counter)
    anc_total = collections.Counter()
    anc_worlds = collections.defaultdict(set)
    world_her = collections.Counter()
    world_anc = collections.defaultdict(set)

    for (a, h), ws in assign.items():
        anc_total[a] += 1
        for w in ws:
            per_anc_world[a][w] += 1
            anc_worlds[a].add(w)
            world_her[w] += 1
            world_anc[w].add(a)
        if len(ws) == 0:
            if (h not in CIRCUMSTANTIAL and a not in CIRCUMSTANTIAL
                    and (a, h) not in KNOWN_EMPTY):
                problems.append(f"rule 0  {a}/{h} is on no world")
        elif len(ws) > 6 and a != "Human":
            problems.append(f"rule 2  {a}/{h} on {len(ws)} worlds")
        elif len(ws) > 8:
            problems.append(f"rule 2  {a}/{h} on {len(ws)} worlds (human cap 8)")

    for a, ws in anc_worlds.items():
        if len(ws) == len(WORLDS) and a not in BIG_THREE:
            problems.append(f"rule 1  {a} appears on all {len(WORLDS)} worlds")

    for a, c in per_anc_world.items():
        if anc_total[a] < 2 or len(anc_worlds[a]) < 2:
            continue
        if a in EXEMPT_RULE_4:
            continue
        # "Approximately half", so round up: 3 of 5 is fine, 4 of 5 is not.
        cap = -(-anc_total[a] // 2)
        for w, n in c.items():
            if n > cap:
                problems.append(f"rule 4  {a}: {n}/{anc_total[a]} heritages on {w} (cap {cap})")

    # Rule 9: Qigang carries five Tian Xia ancestries on purpose, so it is the
    # biggest world by design and is excluded from the spread checks rather
    # than dragging the whole distribution around to accommodate it.
    hv = [n for w, n in world_her.items() if w not in EXEMPT_SPREAD]
    av = [len(v) for w, v in world_anc.items() if w not in EXEMPT_SPREAD]
    if hv and max(hv) > 1.5 * min(hv):
        problems.append(f"rule 6  heritage spread {min(hv)}-{max(hv)} is uneven")
    if av and max(av) > 1.5 * min(av):
        problems.append(f"rule 5  ancestry spread {min(av)}-{max(av)} is uneven")
    return problems


def main() -> int:
    src = pathlib.Path.home() / "Downloads" / \
        "PF2E Ancestry_Heritage Assignments - Ancestries (1).csv"
    assign = load_existing(src)
    assign.update(NEW)
    assign.update(REASSIGNED)
    assign.update(REASSIGNED_SPREAD)
    assign.update(ICE_TO_HRIMGARD)
    assign.update(PROFUGAE_ADAPTED)
    assign.update(FINAL_SPREAD)
    assign.update(EMERRAINE_MUNDANE)
    assign.update(ARID_TO_KHASHAYAR)
    for (a, h) in list(assign):
        if h in CIRCUMSTANTIAL or a in CIRCUMSTANTIAL:
            assign[(a, h)] = []

    world_her = collections.Counter()
    world_anc = collections.defaultdict(set)
    for (a, _h), ws in assign.items():
        for w in ws:
            world_her[w] += 1
            world_anc[w].add(a)

    print(f"  {len(assign)} heritages assigned across {len(WORLDS)} worlds\n")
    print(f"    {'world':14}{'heritages':>10}{'ancestries':>12}")
    for w in WORLDS:
        print(f"    {w:14}{world_her[w]:10}{len(world_anc[w]):12}")

    problems = check(assign)
    print(f"\n  rule breaches: {len(problems)}")
    for p in sorted(problems):
        print(f"    {p}")
    json.dump({f"{a}|{h}": ws for (a, h), ws in sorted(assign.items())},
              open("/tmp/assignments.json", "w"), indent=1)
    write_note(assign, world_her, world_anc)
    write_csv(assign)
    return 0


# Ancestries whose heritages live on a page of their own, because the ancestry
# itself is in a book we do not import.
ORPHAN_ANCESTRIES = {"Kitsune", "Nagaji", "Poppet", "Sprite"}

SRD_ANCESTRIES = pathlib.Path("content/srd/pf2e/compendium/character/ancestries")
VERSATILE = pathlib.Path("content/srd/pf2e/compendium/character/versatile-heritages")
MAP_FILE = pathlib.Path("tools/import-aon/.snapshot/heritage-ancestry.json")


def _norm(s: str, ancestry: str) -> str:
    """Compare heritage names across the two naming styles.

    The spreadsheet drops the ancestry ("Deep", "Ancient Blooded") where AoN
    keeps it and sometimes shortens it ("Deep Rat", "Ancient-Blooded Dwarf"),
    and hyphenation differs. Strip the ancestry word or its stem, then reduce
    to letters and digits so the two forms meet in the middle.
    """
    s = s.lower()
    for tail in (ancestry.lower(), ancestry.lower().rstrip("s"),
                 "rat", "animal", "automaton", "jotunborn", "sarangay"):
        if s.endswith(" " + tail):
            s = s[: -len(tail) - 1]
            break
    return re.sub(r"[^a-z0-9]", "", s)


def _heritage_index() -> dict[tuple[str, str], tuple[str, str]]:
    """(ancestry, normalised short name) -> (note stem, exact anchor).

    Built from the scraped ancestry mapping, so it knows the real heritage
    names rather than reconstructing them from the spreadsheet's abbreviations.
    """
    try:
        owners = json.loads(MAP_FILE.read_text())
    except FileNotFoundError:
        return {}
    idx: dict[tuple[str, str], tuple[str, str]] = {}
    for full, ancestry in owners.items():
        stem = f"{ancestry} Heritages" if ancestry in ORPHAN_ANCESTRIES else ancestry
        idx[(ancestry, _norm(full, ancestry))] = (stem, full)
    return idx


HERITAGE_INDEX = _heritage_index()


def heritage_link(ancestry: str, short: str) -> str:
    """Link a heritage to its section on the ancestry's SRD note.

    Heritages are sections rather than notes, so the target is an anchor, and
    the alias pipe is escaped because these land inside list items that may sit
    in a table. Anything with no SRD entry -- the Tian Xia heritages whose
    ancestry we do not import -- stays plain text rather than linking nowhere.
    """
    if ancestry == "Versatile":
        note = VERSATILE / f"{short}.md"
        if note.exists():
            return f"[[srd/pf2e/compendium/character/versatile-heritages/{short}\\|{short}]]"
        return short
    key = _norm(short, ancestry)
    hit = HERITAGE_INDEX.get((ancestry, key))
    if not hit:
        # Some heritages are named as a phrase the spreadsheet abbreviates to
        # its last word: "Courtier" for "Shadow of the Courtier". Match on the
        # tail, scoped to one ancestry so the risk of a wrong hit is small.
        for (anc, full_key), value in HERITAGE_INDEX.items():
            if anc == ancestry and full_key.endswith(key) and key:
                hit = value
                break
    if not hit:
        return short
    stem, anchor = hit
    if not (SRD_ANCESTRIES / f"{stem}.md").exists():
        return short
    return (f"[[srd/pf2e/compendium/character/ancestries/{stem}"
            f"#{anchor}\\|{short}]]")


def write_note(assign, world_her, world_anc) -> None:
    """Write the player-facing guide into the vault."""
    by_world = collections.defaultdict(lambda: collections.defaultdict(list))
    for (a, h), ws in sorted(assign.items()):
        short = h[: -len(a) - 1].strip() if h.lower().endswith(" " + a.lower()) else h
        for w in ws:
            by_world[w][a].append(short)
    out = [
        "---",
        'title: "Ancestries by World"',
        "type: reference",
        "publish: true",
        "socialImage: og-image.png",
        "---",
        "",
        "# Ancestries by World",
        "",
        "Where each ancestry and heritage is *common*. Nothing here is a",
        "restriction: anyone can play anything, and an unusual origin is a",
        "character hook rather than a problem. This says where your kind is",
        "unremarkable, and so where nobody looks twice.",
        "",
        "Some heritages come from being made rather than being born -- changeling,",
        "dhampir, duskwalker, nephilim, hungerseed, reflection. Those happen",
        "anywhere and appear on no list below.",
        "",
        "| World | Ancestries | Heritages |",
        "|---|---:|---:|",
    ]
    for w in WORLDS:
        out.append(f"| [[{w}]] | {len(world_anc[w])} | {world_her[w]} |")
    for w in WORLDS:
        out += ["", f"## {w}", ""]
        for a in sorted(by_world[w]):
            links = [heritage_link(a, h) for h in sorted(by_world[w][a])]
            out.append(f"- **{a}**: {', '.join(links)}")
    dest = pathlib.Path("content/setting/concepts/Ancestries by World.md")
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\n  wrote {dest}")


def write_csv(assign) -> None:
    dest = pathlib.Path.home() / "Downloads" / "xuartlek-ancestry-assignments.csv"
    with dest.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Ancestry", "Heritage"] + WORLDS)
        for (a, h), ws in sorted(assign.items()):
            w.writerow([a, h] + ["TRUE" if x in ws else "FALSE" for x in WORLDS])
    print(f"  wrote {dest}")


if __name__ == "__main__":
    raise SystemExit(main())
