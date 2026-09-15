---
noteType: pf2eMonster
aliases: "Smith"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Smith"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3413"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Smith"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "+5"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +15, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/Lore|Smithy Lore]] +15, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +8"
abilityMods: [3, 1, 2, 3, 0, 0]
abilities_top:
  - name: "Smithing Specialist"
    desc: "For encounters involving smithing or other crafting tasks, the smith is a 6th-level challenge."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Artisan's Toolkit|Artisan's Toolkit]], leather apron (functions as [[srd/pf2e/compendium/equipment/Armor#Padded Armor|padded armor]]), light hammer"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +8; __Will__: +5"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light hammer +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d6+3 bludgeoning plus smith's fury"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ light hammer +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d6+3 bludgeoning plus smith's fury"
abilities_bot:
  - name: "Smith's Fury"
    desc: "The smith deals an additional 1d6 damage when they hit with a weapon they created."
sourcebook: "_NPC Core_, page 9."
```

```encounter-table
name: Smith
creatures:
  - 1: Smith
```
