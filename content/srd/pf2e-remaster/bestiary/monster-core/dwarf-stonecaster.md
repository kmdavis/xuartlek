---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf Stonecaster"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dwarf Stonecaster"
level: 4
source: "Monster Core"
aon_id: "creature-2966"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2966"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dwarf Stonecaster"
level: "Creature 4"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, tremorsense (imprecise) 10 feet"
languages: "Common, Dwarven, Petran"
skills:
  - name: "Skills"
    desc: "Athletics +11, Crafting +8, Dwarven Lore +8, Nature +12"
abilityMods: [4, 2, 3, 2, 5, -1]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Staff"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +8; __Will__: +14"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +12 (two-handed d8) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ clan dagger +12 (Agile, Parry, versatile B) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Boulder Roll"
    desc: "⬺ (Earth, Primal) The stonecaster conjures a rolling boulder that deals 5d6 bludgeoning damage to each creature in a 60-foot line with a DC 21 basic Reflex save. The stonecaster can't use Boulder Roll again for 1d4 rounds."
  - name: "Dwarven Doughtiness"
    desc: "A dwarf is often calm and collected in the face of imminent danger. At the end of this dwarf's turn, reduce their frightened condition by 2 instead of 1."
  - name: "Tremor"
    desc: "⬻ (Earth, Primal) The stonecaster causes the earth below to tremble. Each creature on the ground in a 10-foot emanation takes 2d8 bludgeoning damage with a DC 21 basic Fortitude save. A creature that critically fails is knocked prone."
sourcebook: "_Monster Core_, page 135."
```

```encounter-table
name: Dwarf Stonecaster
creatures:
  - 1: Dwarf Stonecaster
```
