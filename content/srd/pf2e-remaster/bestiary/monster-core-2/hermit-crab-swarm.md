---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hermit Crab Swarm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Hermit Crab Swarm"
level: 4
source: "Monster Core 2"
aon_id: "creature-4303"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4303"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hermit Crab Swarm"
level: "Creature 4"
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, tremorsense (imprecise) 15 feet"
skills:
  - name: "Skills"
    desc: "Athletics +12"
abilityMods: [4, 2, 3, -4, 1, -1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +10; __Will__: +7"
hp: 42
health:
  - name: "HP"
    desc: "42; __Immunities__ precision, swarm mind; __Resistances__ piercing 5, slashing 5; __Weaknesses__ area damage 5, splash damage 5"
speed: "30 feet, swim 15 feet"
abilities_bot:
  - name: "Swarming Snips"
    desc: "⬻ Each enemy in the swarm's space takes 2d8 piercing damage (DC 20 basic Reflex save). Creatures that fail this save also take 1d4 persistent bleed damage."
sourcebook: "_Monster Core 2_, page 77."
```

```encounter-table
name: Hermit Crab Swarm
creatures:
  - 1: Hermit Crab Swarm
```
