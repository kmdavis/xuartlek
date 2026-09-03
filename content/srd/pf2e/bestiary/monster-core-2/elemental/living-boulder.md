---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Boulder"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Living Boulder"
level: 2
source: "Monster Core 2"
aon_id: "creature-4382"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4382"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Living Boulder"
level: "Creature 2"
size: "Small"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, tremorsense 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +8, Stealth +5"
abilityMods: [4, -1, 4, -4, 2, -1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +5; __Will__: +8"
hp: 35
health:
  - name: "HP"
    desc: "35; __Immunities__ bleed, paralyzed, poison, sleep"
speed: "20 feet, burrow 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Earth Glide"
    desc: "A living boulder can Burrow through earthen matter, including rock. When it does so, it moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Rolling Charge"
    desc: "⬺ The living boulder Strides twice, and can then make a Strike with its jaws. This jaws Strike gains Knockdown."
sourcebook: "_Monster Core 2_, page 146."
```

```encounter-table
name: Living Boulder
creatures:
  - 1: Living Boulder
```
