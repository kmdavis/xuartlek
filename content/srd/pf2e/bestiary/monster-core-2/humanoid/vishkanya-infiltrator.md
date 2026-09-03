---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vishkanya Infiltrator"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/vishkanya
  - pf2e/creature/trait/medium
statblock: inline
name: "Vishkanya Infiltrator"
level: 3
source: "Monster Core 2"
aon_id: "creature-4613"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4613"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vishkanya Infiltrator"
level: "Creature 3"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Rare"
trait_03: "Vishkanya"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "Common, Vishkanyan"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +7, Deception +11, Diplomacy +9, Society +7, Stealth +11, Thievery +9"
abilityMods: [2, 4, 1, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Disguise Kit, Kukri, Leather Armor, Shuriken (10), Thieves' Toolkit"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6 (+8 vs. poisons); __Ref__: +11; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +11 (Agile, finesse, trip) __Damage__ 1d6+4 slashing"
  - name: "Ranged"
    desc: "⬻ shuriken +11 (Agile, thrown 20 feet) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Envenom"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Using either saliva or blood, the vishkanya applies vishkanyan venom to one weapon they're holding. To use their blood, they must be injured, or they can deal themself 1 slashing damage as part of the action."
  - name: "Flexible"
    desc: "The vishkanya is adept at dealing with tight situations. They have a +1 circumstance bonus to checks to Escape."
  - name: "Proficient Poisoner"
    desc: "The vishkanya doesn't lose the poison on a weapon due to a critically failed Strike."
  - name: "Sneak Attack"
    desc: "The vishkanya's Strikes deal an additional 1d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core 2_, page 3."
```

```encounter-table
name: Vishkanya Infiltrator
creatures:
  - 1: Vishkanya Infiltrator
```
