---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Combat Engineer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Combat Engineer"
level: 1
source: "NPC Core"
aon_id: "creature-3521"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3521"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Combat Engineer"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +13"
abilityMods: [3, 2, 1, 4, 2, 1]
abilities_top:
  - name: "Logistics Specialist"
    desc: "In situations involving battlefield engineering or logistics, the combat engineer is a 5th-level challenge."
  - name: "Items"
    desc: "entrenching tool (functions as a [[srd/pf2e/compendium/equipment/weapons/pick/pick|pick]]), Heavy Crossbow (10 bolts), Studded Leather Armor"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +5; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ entrenching tool +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]]) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ heavy crossbow +7 (range increment 120 feet, reload 2) __Damage__ 1d10 piercing"
abilities_bot:
  - name: "Fortify"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|Exploration]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The combat engineer digs trenches and constructs earthen barricades at a rate of one 5-foot cube per hour. A combat engineer can instead direct the work of four allied Small or larger creatures to quadruple this rate."
  - name: "Improvised Barricade"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The combat engineer has at least 5 Bulk of loose items or material within reach"
  - name: "Effect"
    desc: "The combat engineer slaps together a 5-foot high barrier in an adjacent square. The barrier is an object with 10 Hit Points, 5 Hardness, AC 10, and it provides standard cover. After 1 minute, the barrier collapses under its own weight."
sourcebook: "_NPC Core_, page 88."
```

```encounter-table
name: Combat Engineer
creatures:
  - 1: Combat Engineer
```
