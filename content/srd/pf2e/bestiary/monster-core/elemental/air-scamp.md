---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Air Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/small
statblock: inline
name: "Air Scamp"
level: 1
source: "Monster Core"
aon_id: "creature-2985"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2985"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Air Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Air"
trait_02: "Elemental"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision, fog vision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Stealth +7"
abilityMods: [1, 4, 0, -2, 0, 0]
abilities_top:
  - name: "Fog Vision"
    desc: "The air scamp ignores the concealed condition from fog and mist."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +2; __Ref__: +9; __Will__: +7"
hp: 12
health:
  - name: "HP"
    desc: "12 (fast healing 2 (in open air)); __Immunities__ bleed, paralyzed, poison, sleep"
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 (Finesse) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Sirocco Breath"
    desc: "⬺ (Air, Arcane) The air scamp creates cutting winds in a 15-foot cone that deal 2d6 slashing damage to each creature within the area (DC 17 basic Reflex save). A creature that fails its save is also pushed back 10 feet. The air scamp can't use Sirocco Breath again for 1d4 rounds."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17 - __1st__ Gust of Wind - __2nd__ Blur"
sourcebook: "_Monster Core_, page 146."
```

```encounter-table
name: Air Scamp
creatures:
  - 1: Air Scamp
```
