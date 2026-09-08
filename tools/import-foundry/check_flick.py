#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Self-check. Also imported as a guard by build_players.py.

Check the derivations against Flick, whose sheet was entered by hand from the
Foundry UI and verified in play. Any mismatch means foundry_pc.py is wrong."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import foundry_pc as F

DL = Path.home() / "Downloads"
a = F.load(DL / "fvtt-Actor-flick-(wes)-0RU6JYuFZDhsl3JI.json")
m = F.ability_mods(a)
got = {
    "abilityMods": [m[k] for k in F.ABILITIES],
    "hp": F.max_hp(a, m), "ac": F.armor_class(a, m),
    "perception": F.perception(a, m), **F.saves(a, m), **F.skills(a, m),
}
want = {
    "abilityMods": [0, 4, 2, 0, 0, 3], "hp": 34, "ac": 19, "perception": 6,
    "fortitude": 6, "reflex": 10, "will": 6,
    "acrobatics": 8, "athletics": 4, "deception": 7, "diplomacy": 7, "intimidation": 7,
    "performance": 7, "stealth": 8, "thievery": 8,
}
bad = 0
for k, w in want.items():
    g = got.get(k)
    ok = g == w
    bad += not ok
    print(f"  {'ok ' if ok else 'FAIL'}  {k:14} want {w!s:12} got {g}")
print(f"\n{'all derivations match' if not bad else f'{bad} MISMATCH'}")
print("\nknown export gaps (not derivable, must come from the Foundry UI):")
print("  intimidation  absent from system.skills entirely; sheet shows +7")
print("  Sailing Lore  lore items carry no rank; assumed trained (+4), sheet shows +6")
sys.exit(1 if bad else 0)
