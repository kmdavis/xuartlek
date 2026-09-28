#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Self-check. Also imported as a guard by build_players.py.

Check the derivations against characters whose numbers are known to be right.
Flick's sheet was entered by hand from the Foundry UI and verified in play.
Lorde Morthonk's numbers are Foundry's own derived statistics, and it is here
because it takes the alternate ancestry boosts, which Flick does not. Any
mismatch means foundry_pc.py is wrong."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import foundry_pc as F

# The exports' folder, which build_players.py passes on from its --downloads.
DL = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads"
CHECKS = {
    "fvtt-Actor-flick-(wes)-0RU6JYuFZDhsl3JI.json": {
        "abilityMods": [0, 4, 2, 0, 0, 3], "hp": 34, "ac": 19, "perception": 6,
        "fortitude": 6, "reflex": 10, "will": 6,
        "acrobatics": 8, "athletics": 4, "deception": 7, "diplomacy": 7,
        "intimidation": 7, "performance": 7, "stealth": 8, "thievery": 8,
        "size": "Small", "speed": 25,
    },
    "fvtt-Actor-lorde-morthonk-(joel)-WjgtBBaXatZRzBIC.json": {
        "abilityMods": [0, 2, 1, 4, 2, 0], "hp": 24, "ac": 18, "perception": 6,
        "fortitude": 7, "reflex": 6, "will": 6,
        "acrobatics": 6, "arcana": 8, "intimidation": 4, "medicine": 6,
        "nature": 6, "occultism": 8, "religion": 6, "survival": 6,
        "size": "Small", "speed": 20, "traits": ["Awakened Animal", "Beast"],
        "languages": ["common", "necril", "thalassic", "draconic", "requian"],
        "strikes": {"beak": 6},
    },
}


def check(file: str, want: dict) -> int:
    a = F.load(DL / file)
    m = F.ability_mods(a)
    got = {
        "abilityMods": [m[k] for k in F.ABILITIES],
        "hp": F.max_hp(a, m), "ac": F.armor_class(a, m),
        "perception": F.perception(a, m), **F.saves(a, m), **F.skills(a, m),
        "size": F.size(a), "speed": F.land_speed(a),
        "traits": F.creature_traits(a), "languages": F.languages(a),
        "strikes": {s["name"].lower(): F.attack_bonus(a, s, m)[0]
                    for s in F.rule_strikes(a)},
    }
    bad = 0
    print(a["name"])
    for k, w in want.items():
        g = got.get(k)
        ok = g == w
        bad += not ok
        print(f"  {'ok ' if ok else 'FAIL'}  {k:14} want {w!s:12} got {g}")
    return bad


bad = sum(check(file, want) for file, want in CHECKS.items())
print(f"\n{'all derivations match' if not bad else f'{bad} MISMATCH'}")
print("\nknown export gaps (not derivable, must come from the Foundry UI):")
print("  intimidation  absent from system.skills entirely; sheet shows +7")
print("  Sailing Lore  lore items carry no rank; assumed trained (+4), sheet shows +6")
sys.exit(1 if bad else 0)
