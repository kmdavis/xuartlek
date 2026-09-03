---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Construction Worker"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Construction Worker"
level: 2
source: "NPC Core"
aon_id: "creature-3498"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3498"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Construction Worker"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Architecture Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +6"
abilityMods: [4, 0, 3, 2, 1, 0]
abilities_top:
  - name: "Specialty Contractor"
    desc: "For encounters involving architecture or construction, the construction worker is a 6th-level challenge."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]], bricks (4), Chalk, safety gear (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), sledgehammer (functions as a [[srd/pf2e/compendium/equipment/weapons/hammer/maul|maul]])"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +6; __Will__: +7"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ maul +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d12+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ brick +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "By Design"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|Exploration]]) The construction worker spends 1 minute inspecting the layout of a room and attempts a DC 22 [[srd/pf2e/compendium/rules-elements/skills/lore|Architecture Lore]] check. On a success, they learn the size and layout of all adjacent rooms on the same floor (or all rooms on the floor on a critical success). They can inspect each room only once per day."
  - name: "Demolishing Swing"
    desc: "⬺ The construction worker makes a maul Strike against a creature. If it hits, the creature is pushed 10 feet. If the target is wearing metal armor, its armor also takes the damage, which bypasses 5 of the armor's Hardness."
sourcebook: "_NPC Core_, page 70."
```

```encounter-table
name: Construction Worker
creatures:
  - 1: Construction Worker
```
