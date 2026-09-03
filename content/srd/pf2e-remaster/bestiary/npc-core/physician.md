---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Physician"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Physician"
level: -1
source: "NPC Core"
aon_id: "creature-3480"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3480"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Physician"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; (8 to notice ailments)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Diplomacy +6, Medicine +12, Society +5"
abilityMods: [-1, 1, 1, 4, 2, 2]
abilities_top:
  - name: "Medical Specialist"
    desc: "For medical matters, the physician is a 4th-level challenge."
  - name: "Bedside Manner"
    desc: "A physician has a +4 circumstance bonus to Diplomacy checks to Make an Impression on or make a Request of a diseased, poisoned, or wounded creature."
  - name: "Doctor's Hand"
    desc: "When the physician rolls a critical failure on a check to Treat Disease, Treat Poison, or Treat Wounds, they get a failure instead."
  - name: "Items"
    desc: "minor elixir of life (2), Healer's Toolkit, medical textbook"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +9; __Ref__: +3; __Will__: +8"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4–1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ medical textbook +5 (Nonlethal, thrown 10 feet) __Damage__ 1d4–1 bludgeoning"
sourcebook: "_NPC Core_, page 60."
```

```encounter-table
name: Physician
creatures:
  - 1: Physician
```
