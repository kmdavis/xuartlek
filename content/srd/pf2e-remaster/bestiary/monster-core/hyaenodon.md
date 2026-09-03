---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hyaenodon"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Hyaenodon"
level: 3
source: "Monster Core"
aon_id: "creature-3066"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3066"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hyaenodon"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +12, Stealth +8"
abilityMods: [5, 3, 3, -4, 2, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +8; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 __Damage__ 1d10+5 piercing plus Knockdown and bonecrunching bite"
abilities_bot:
  - name: "Bonecrunching Bite"
    desc: "A creature that is critically hit by a hyaenodon must succeed at a DC 20 Fortitude save or become wounded 1 as the creature's bones or cartilage are crushed by the beast's jaws."
  - name: "Drag"
    desc: "⬻ The hyaenodon makes a jaws Strike against a prone enemy. If it hits, in addition to dealing damage, the hyaenodon Strides up to 10 feet, dragging the enemy along."
  - name: "Pack Attack"
    desc: "The hyaenodon deals an extra 1d6 damage to any creature within reach of at least two of the hyaenodon's allies."
sourcebook: "_Monster Core_, page 205."
```

```encounter-table
name: Hyaenodon
creatures:
  - 1: Hyaenodon
```
