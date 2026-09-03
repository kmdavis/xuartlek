---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wolf"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Wolf"
level: 1
source: "Monster Core"
aon_id: "creature-3241"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3241"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wolf"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +6, Stealth +7, Survival +7"
abilityMods: [2, 4, 1, -4, 2, -2]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +9; __Will__: +5"
hp: 24
health:
  - name: "HP"
    desc: "24"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 1d6+2 piercing plus Knockdown"
abilities_bot:
  - name: "Pack Attack"
    desc: "The wolf's Strikes deal 1d4 extra damage to creatures within reach of at least two of the wolf's allies."
sourcebook: "_Monster Core_, page 350."
```

```encounter-table
name: Wolf
creatures:
  - 1: Wolf
```
