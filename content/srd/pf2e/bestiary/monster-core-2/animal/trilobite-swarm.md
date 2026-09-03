---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Trilobite Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Trilobite Swarm"
level: 3
source: "Monster Core 2"
aon_id: "creature-4588"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4588"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Trilobite Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Swarm"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, wavesense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +8, Stealth +9, Survival +7"
abilityMods: [1, 4, 3, -5, 2, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +9; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 3, piercing 3, slashing 5; __Weaknesses__ area damage 5, splash damage 5"
speed: "swim 25 feet"
abilities_bot:
  - name: "Clinging Bites"
    desc: "⬻ The trilobites in the swarm latch onto creatures and gnaw at them. Each enemy in the swarm's space takes 2d6 slashing damage (DC 18 basic Reflex save)."
sourcebook: "_Monster Core 2_, page 326."
```

```encounter-table
name: Trilobite Swarm
creatures:
  - 1: Trilobite Swarm
```
