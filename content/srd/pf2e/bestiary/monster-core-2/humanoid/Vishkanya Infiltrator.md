---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4613"
socialImage: og-image.png
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
    desc: "+10; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Vishkanyan"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +9"
abilityMods: [2, 4, 1, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Disguise Kit|Disguise Kit]], [[srd/pf2e/compendium/equipment/weapons/knife/Kukri|Kukri]], [[srd/pf2e/compendium/equipment/Armor#Leather Armor|Leather Armor]], [[srd/pf2e/compendium/equipment/weapons/dart/Shuriken|Shuriken]] (10), [[srd/pf2e/compendium/equipment/adventuring-gear/Thieves' Toolkit|Thieves' Toolkit]]"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6 (+8 vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poisons]]); __Ref__: +11; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 1d6+4 slashing"
  - name: "Ranged"
    desc: "⬻ shuriken +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Envenom"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Using either saliva or blood, the vishkanya applies vishkanyan venom to one weapon they're holding. To use their blood, they must be injured, or they can deal themself 1 slashing damage as part of the action."
  - name: "Flexible"
    desc: "The vishkanya is adept at dealing with tight situations. They have a +1 circumstance bonus to checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]]."
  - name: "Proficient Poisoner"
    desc: "The vishkanya doesn't lose the [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] on a weapon due to a critically failed Strike."
  - name: "Sneak Attack"
    desc: "The vishkanya's Strikes deal an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core 2_, page 3."
```

```encounter-table
name: Vishkanya Infiltrator
creatures:
  - 1: Vishkanya Infiltrator
```
