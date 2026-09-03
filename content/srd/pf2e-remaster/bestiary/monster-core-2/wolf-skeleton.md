---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wolf Skeleton"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Wolf Skeleton"
level: 0
source: "Monster Core 2"
aon_id: "creature-4546"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4546"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wolf Skeleton"
level: "Creature 0"
size: "Medium"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +5, Stealth +6"
abilityMods: [2, 4, 1, -5, 2, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +8; __Will__: +6"
hp: 12
health:
  - name: "HP"
    desc: "12 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 5, electricity 5, fire 5, piercing 5, slashing 5"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d4+2 piercing plus Knockdown"
abilities_bot:
  - name: "Surge of Speed"
    desc: "⬺ The wolf skeleton Strides three times, but it's off-guard until the start of its next turn."
sourcebook: "_Monster Core 2_, page 289."
```

```encounter-table
name: Wolf Skeleton
creatures:
  - 1: Wolf Skeleton
```
