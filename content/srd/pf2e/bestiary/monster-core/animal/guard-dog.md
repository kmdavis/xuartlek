---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Guard Dog"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Guard Dog"
level: -1
source: "Monster Core"
aon_id: "creature-2924"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2924"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Guard Dog"
level: "Creature -1"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +4, Stealth +5, Survival +4"
abilityMods: [1, 2, 2, -4, 1, -1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +7; __Will__: +4"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +6 __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Pack Attack"
    desc: "The dog's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the dog's allies."
sourcebook: "_Monster Core_, page 102."
```

```encounter-table
name: Guard Dog
creatures:
  - 1: Guard Dog
```
