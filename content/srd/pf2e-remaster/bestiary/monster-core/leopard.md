---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leopard"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Leopard"
level: 2
source: "Monster Core"
aon_id: "creature-2865"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2865"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Leopard"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +7, Stealth +8"
abilityMods: [3, 4, 2, -4, 1, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 (Finesse) __Damage__ 1d10+3 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +10 (Agile, Finesse) __Damage__ 1d6+3 slashing"
abilities_bot:
  - name: "Maul"
    desc: "⬻ The leopard makes two claw Strikes against a creature it has grabbed. Both count toward its multiple attack penalty, but the penalty increases only after both attacks are made."
  - name: "Pounce"
    desc: "⬻ The leopard Strides and makes a Strike at the end of that movement. If the leopard began this action hidden, it remains hidden until after this ability's Strike."
  - name: "Sneak Attack"
    desc: "The leopard deals 1d4 extra precision damage to off-guard creatures."
sourcebook: "_Monster Core_, page 50."
```

```encounter-table
name: Leopard
creatures:
  - 1: Leopard
```
