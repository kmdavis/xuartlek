---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spear Frog"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Spear Frog"
level: 0
source: "Monster Core 2"
aon_id: "creature-4403"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4403"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Spear Frog"
level: "Creature 0"
size: "Tiny"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +0"
abilityMods: [-2, 3, 1, -4, 2, 0]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +7; __Will__: +6"
hp: 12
health:
  - name: "HP"
    desc: "12"
abilities_mid:
  - name: "Toxic Skin"
    desc: "Anytime a creature touches the spear frog or an adjacent creature Strikes the spear frog with a melee attack, that creature is exposed to spear frog venom."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 (Agile, finesse) __Damage__ 1d6 piercing plus spear frog venom"
abilities_bot:
  - name: "Spear Frog Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 15 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and enfeebled 1 (1 round)"
  - name: "Sticky Feet"
    desc: "Spear frogs are not off-guard when Balancing on a narrow surface, and they gain a +4 circumstance bonus to Reflex saves to avoid falling."
sourcebook: "_Monster Core 2_, page 158."
```

```encounter-table
name: Spear Frog
creatures:
  - 1: Spear Frog
```
