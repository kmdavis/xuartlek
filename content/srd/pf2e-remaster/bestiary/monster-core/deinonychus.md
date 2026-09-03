---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deinonychus"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/medium
statblock: inline
name: "Deinonychus"
level: 2
source: "Monster Core"
aon_id: "creature-2916"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2916"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Deinonychus"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +9, Stealth +7"
abilityMods: [3, 3, 4, -4, 1, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +9; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 2d6+3 piercing"
  - name: "Melee"
    desc: "⬻ talon +9 (Agile) __Damage__ 1d6+3 slashing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Darting Attack"
    desc: "⬻ The deinonychus Strides up to 10 feet and then makes a Strike, or makes a Strike and then Strides up to 10 feet."
  - name: "Predator's Advantage"
    desc: "Bleeding creatures are off-guard to the deinonychus"
sourcebook: "_Monster Core_, page 97."
```

```encounter-table
name: Deinonychus
creatures:
  - 1: Deinonychus
```
