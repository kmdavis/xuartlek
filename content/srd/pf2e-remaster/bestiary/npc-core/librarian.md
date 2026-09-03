---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Librarian"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Librarian"
level: -1
source: "NPC Core"
aon_id: "creature-3587"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3587"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Librarian"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common, Draconic, Elven; up to 4 additional languages"
skills:
  - name: "Skills"
    desc: "Academia Lore +11, Arcana +9, Library Lore +13, Nature +8, Religion +8"
abilityMods: [0, 1, 0, 3, 2, 1]
abilities_top:
  - name: "Research Specialist"
    desc: "A librarian is a 3rd-level challenge for encounters involving research."
  - name: "Methodical Research"
    desc: "(concentrate) When Searching through stacks of books, a librarian can find the answer to almost any question. This allows the librarian to use Library Lore in place of other lore skills, given enough time. The GM determines the DC of the check and the amount of time it takes (typically, a librarian can attempt three or four checks during 1 day of downtime)."
  - name: "Items"
    desc: "books, Dagger, Writing Set"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +2; __Ref__: +3; __Will__: +7"
hp: 6
health:
  - name: "HP"
    desc: "6"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ book +4 (Nonlethal) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ book +5 (Nonlethal, thrown 10 feet) __Damage__ 1d4 bludgeoning"
sourcebook: "_NPC Core_, page 138."
```

```encounter-table
name: Librarian
creatures:
  - 1: Librarian
```
