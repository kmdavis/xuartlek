---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dire Wolf"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Dire Wolf"
level: 3
source: "Monster Core"
aon_id: "creature-3242"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3242"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dire Wolf"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +10, Stealth +8, Survival +10"
abilityMods: [5, 3, 4, -4, 3, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +8; __Will__: +8"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 20"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 (reach 10 feet) __Damage__ 1d10+5 piercing plus Grab or Knockdown"
abilities_bot:
  - name: "Pack Attack"
    desc: "The dire wolf's Strikes deal 1d6 extra damage to creatures within reach of at least two of the wolf's allies."
  - name: "Worry"
    desc: "⬻ (Attack)"
  - name: "Requirements"
    desc: "The dire wolf has a creature grabbed or restrained in its jaws"
  - name: "Effect"
    desc: "The dire wolf fiercely shakes the creature with its teeth, dealing 1d10+2 damage with a DC 20 basic Fortitude save."
sourcebook: "_Monster Core_, page 350."
```

```encounter-table
name: Dire Wolf
creatures:
  - 1: Dire Wolf
```
