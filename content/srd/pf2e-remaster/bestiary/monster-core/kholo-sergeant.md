---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kholo Sergeant"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kholo
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/gnoll
statblock: inline
name: "Kholo Sergeant"
level: 4
source: "Monster Core"
aon_id: "creature-3071"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3071"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kholo Sergeant"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: "Gnoll"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common, Kholo"
skills:
  - name: "Skills"
    desc: "Athletics +13, Intimidation +9, Stealth +11, Survival +10"
abilityMods: [4, 2, 2, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Hide Armor, Scimitar"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +10; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +14 (Forceful, Sweep) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ jaws +14 (Agile) __Damage__ 1d6+7 piercing"
  - name: "Ranged"
    desc: "⬻ composite shortbow +12 (deadly d10, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Bark Orders"
    desc: "⬻ (Auditory, Linguistic) The kholo sergeant commands their allies to reposition. Any allies who hear and understand this order can use a reaction to Step."
  - name: "Pack Attack"
    desc: "A kholo sergeant deals 1d4 extra damage to any creature that's within reach of at least two of the kholo sergeant's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
sourcebook: "_Monster Core_, page 209."
```

```encounter-table
name: Kholo Sergeant
creatures:
  - 1: Kholo Sergeant
```
