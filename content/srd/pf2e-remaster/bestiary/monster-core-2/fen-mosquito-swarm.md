---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fen Mosquito Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Fen Mosquito Swarm"
level: 3
source: "Monster Core 2"
aon_id: "creature-4481"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4481"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fen Mosquito Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Stealth +8"
abilityMods: [0, 4, 3, -5, 0, -5]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +11; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, splash damage 5"
speed: "5 feet, fly 25 feet"
abilities_bot:
  - name: "Pyrexic Malaria"
    desc: "(Disease) The victim can't reduce its sickened condition while it's affected by pyrexic malaria"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Onset"
    desc: "4 days"
  - name: "Stage 1"
    desc: "sickened 1 (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 1 and sickened 1 (1 day)"
  - name: "Stage 3"
    desc: "as stage 2 (1 day)"
  - name: "Stage 4"
    desc: "unconscious (1 day)"
  - name: "Stage 5"
    desc: "dead"
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 1d6 piercing damage (DC 20 basic Reflex save) and is exposed to pyrexic malaria. Creatures that fail the saving throw also take 1d4 persistent bleed damage."
sourcebook: "_Monster Core 2_, page 228."
```

```encounter-table
name: Fen Mosquito Swarm
creatures:
  - 1: Fen Mosquito Swarm
```
