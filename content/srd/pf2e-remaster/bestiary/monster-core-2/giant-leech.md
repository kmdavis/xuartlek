---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Leech"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Leech"
level: 2
source: "Monster Core 2"
aon_id: "creature-4461"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4461"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Leech"
level: "Creature 2"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; tremorsense 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +8, Stealth +7"
abilityMods: [4, 1, 3, -5, 1, -5]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +7; __Will__: +5"
hp: 32
health:
  - name: "HP"
    desc: "32; __Weaknesses__ salt 5"
speed: "5 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mouth +9 __Damage__ 1d4+6 piercing plus Grab"
abilities_bot:
  - name: "Blood Drain"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant leech has a living creature grabbed or restrained; Effect The giant leech drains blood from the creature it has grabbed or restrained. This deals 2d4 piercing damage (DC 18 basic Fortitude save). A creature that takes any damage from having its blood drained by a giant leech is drained 1 until it receives any kind or amount of healing."
sourcebook: "_Monster Core 2_, page 212."
```

```encounter-table
name: Giant Leech
creatures:
  - 1: Giant Leech
```
