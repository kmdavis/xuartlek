---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sprite"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/sprite
  - pf2e/creature/trait/tiny
statblock: inline
name: "Sprite"
level: -1
source: "Monster Core"
aon_id: "creature-3210"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3210"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sprite"
level: "Creature -1"
size: "Tiny"
trait_01: "Fey"
trait_02: "Sprite"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Stealth +6"
abilityMods: [-3, 4, 0, -2, 0, 2]
abilities_top:
  - name: "Luminous Fire"
    desc: "(light, primal) A sprite naturally sheds light like a torch. The sprite can extinguish, rekindle, or change the color of this light by using an action with the concentrate trait. While this light is extinguished, the sprite's Strikes don't deal fire damage, and they can't use their luminous spark Strike."
  - name: "Items"
    desc: "Rapier"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +8; __Will__: +4"
hp: 7
health:
  - name: "HP"
    desc: "7; __Weaknesses__ cold iron 3"
speed: "10 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +8 (deadly d8, Disarm, Finesse, Fire, Magical, reach 0 feet) __Damage__ 1d6–3 piercing plus 1 fire"
  - name: "Ranged"
    desc: "⬻ luminous spark +8 (Fire, Light, range 20 feet) __Damage__ 1d4 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16 - __Cantrips (1st)__ Daze, Detect Magic, Light - __1st__ Dizzying Colors"
sourcebook: "_Monster Core_, page 322."
```

```encounter-table
name: Sprite
creatures:
  - 1: Sprite
```
