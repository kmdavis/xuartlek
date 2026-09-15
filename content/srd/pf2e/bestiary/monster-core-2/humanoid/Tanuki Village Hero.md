---
noteType: pf2eMonster
aliases: "Tanuki Village Hero"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tanuki
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Tanuki Village Hero"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4575"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tanuki Village Hero"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tanuki"
trait_03: "Uncommon"
modifier: 4
perception:
  - name: "Perception"
    desc: "+4"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Tanuki"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +3, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6"
abilityMods: [2, 3, 2, 0, -1, 3]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/dart/Dart|Dart]] (10), [[srd/pf2e/compendium/equipment/weapons/knife/Kama|Kama]], studded leather"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +8; __Will__: +2"
hp: 21
health:
  - name: "HP"
    desc: "21"
abilities_mid:
  - name: "Tactical Retreat"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "The tanuki takes damage"
  - name: "Effect"
    desc: "The tanuki runs to a better tactical position. The tanuki gains the [[srd/pf2e/compendium/rules-elements/Conditions#Fleeing|fleeing]] condition until the beginning of their next turn and [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kama +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 1d6+2 slashing"
  - name: "Ranged"
    desc: "⬻ dart +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The tanuki takes on the form of a mundane raccoon dog. This makes them Tiny and gives them a +2 status bonus to their Stealth modifier, but they can't make Strikes."
  - name: "Tricky Throw"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The tanuki winds up and puts their everything into a throw. They make a dart Strike at one enemy within 40 feet. If the Strike is unsuccessful, the tanuki falls [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. If the Strike is successful, they really did put everything into the throw, having transformed into the dart the moment they threw it. The tanuki disappears from the space they threw from, appears in a space adjacent to the enemy and makes a kama Strike against said enemy, who's [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the attack."
sourcebook: "_Monster Core 2_, page 315."
```

```encounter-table
name: Tanuki Village Hero
creatures:
  - 1: Tanuki Village Hero
```
