---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Severed Head"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Severed Head"
level: -1
source: "Monster Core 2"
aon_id: "creature-4279"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4279"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Severed Head"
level: "Creature -1"
size: "Tiny"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +4"
abilityMods: [1, 2, 0, -5, 2, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +4; __Ref__: +6; __Will__: +4"
hp: 7
health:
  - name: "HP"
    desc: "7 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Weaknesses__ vitality 1"
speed: "15 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +6 (Agile, finesse) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Gnash"
    desc: "⬻"
  - name: "Requirements"
    desc: "The severed head's previous action was a jaws Strike that dealt damage to its target"
  - name: "Effect"
    desc: "The severed head makes a second jaws Strike as it violently shakes itself, trying to rip away a mouthful of flesh. On a success, the target takes an additional 1d4 slashing damage and 1 persistent bleed damage."
sourcebook: "_Monster Core 2_, page 56."
```

```encounter-table
name: Severed Head
creatures:
  - 1: Severed Head
```
