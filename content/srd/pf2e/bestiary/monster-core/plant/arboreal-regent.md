---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arboreal Regent"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Arboreal Regent"
level: 8
source: "Monster Core"
aon_id: "creature-2831"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2831"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Arboreal Regent"
level: "Creature 8"
size: "Huge"
trait_01: "Plant"
trait_02: "Wood"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [7, -1, 6, 1, 4, 2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +20; __Ref__: +11; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ bludgeoning 5, piercing 5; __Weaknesses__ axes 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ branch +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d12+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ root +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 2d8+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +19 (Brutal, range increment 120 feet) __Damage__ 2d10+7 bludgeoning"
abilities_bot:
  - name: "Awaken Tree"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The arboreal regent causes a tree within 180 feet to uproot itself and fight as a minion using the statistics for an [[srd/pf2e/bestiary/monster-core/plant/awakened-tree|awakened tree]]. The arboreal regent can control up to two awakened trees at a time, and they can issue commands to both trees as a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] traits."
  - name: "Sunder Objects"
    desc: "When an arboreal regent damages an item or structure, they deal an additional 2d10 damage to that item or structure."
  - name: "Throw Rock"
    desc: "⬻"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 26 - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]]"
sourcebook: "_Monster Core_, page 25."
```

```encounter-table
name: Arboreal Regent
creatures:
  - 1: Arboreal Regent
```
