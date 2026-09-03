---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Fangtooth"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Fangtooth"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3278"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3278"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Giant Fangtooth"
level: "Creature 4"
size: "Medium"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, scent (imprecise) 120 feet, wavesense (precise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +14"
abilityMods: [5, 2, 3, -5, 2, -1]
abilities_top:
  - name: "Sunless Sight"
    desc: "In an area of bright light, the giant fangtooth is blinded and slowed 1."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +11; __Will__: +8"
hp: 75
health:
  - name: "HP"
    desc: "75"
speed: "swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +15 __Damage__ 2d8+5 piercing plus deep puncture and Grab"
abilities_bot:
  - name: "Deep Puncture"
    desc: "Creatures critically hit by the fangtooth's bite take an additional 1d8 persistent bleed damage."
  - name: "Constrict"
    desc: "⬻ 2d8 piercing, DC 21"
sourcebook: "_Howl of the Wild_, page 149."
```

```encounter-table
name: Giant Fangtooth
creatures:
  - 1: Giant Fangtooth
```
