---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ferrous Butterfly"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Ferrous Butterfly"
level: 1
source: "Rage of Elements"
aon_id: "creature-2643"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2643"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Ferrous Butterfly"
level: "Creature 1"
size: "Tiny"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +9"
abilityMods: [2, 4, 3, -4, 0, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +9; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 3"
speed: "5 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wing +9 (Finesse) __Damage__ 1d4+2 slashing plus 1 persistent bleed and a thousand cuts"
abilities_bot:
  - name: "A Thousand Cuts"
    desc: "A ferrous butterfly's knifelike wings cause terrible lacerations that continue to bleed. Any creature with persistent bleed damage from a ferrous butterfly's wing attack has weakness 2 to slashing damage until the bleeding is stopped."
  - name: "Swoop"
    desc: "⬺ The ferrous butterfly Flies up to its Speed and makes a wing Strike at any point during that movement."
sourcebook: "_Rage of Elements_, page 152."
```

```encounter-table
name: Ferrous Butterfly
creatures:
  - 1: Ferrous Butterfly
```
