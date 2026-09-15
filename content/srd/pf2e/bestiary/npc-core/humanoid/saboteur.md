---
noteType: pf2eMonster
aliases: "Saboteur"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Saboteur"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3608"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Saboteur"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; (10 to find traps)"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/Lore|Engineering Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +6, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +9, [[srd/pf2e/compendium/rules-elements/skills/Lore|Underworld Lore]] +6"
abilityMods: [1, 3, 1, 2, 2, 1]
abilities_top:
  - name: "Snare Crafting"
    desc: "The saboteur can [[srd/pf2e/compendium/rules-elements/actions/player-core#Craft|Craft]] snares and has the supplies to make up to two [[srd/pf2e/compendium/equipment/snares/Caltrop Snare|caltrop snares]] and up to two [[srd/pf2e/compendium/equipment/snares/Hampering Snare|hampering snares]]. Snare rules can be found [[srd/pf2e/books/player-core-2/snares/snares|here]]."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Artisan's Toolkit|Artisan's Toolkit]] (snare toolkit), Crowbar, Disguise Kit, Hand Crossbow (10 bolts), Sap, [[srd/pf2e/compendium/equipment/adventuring-gear/Thieves' Toolkit|Thieves' Toolkit]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9 (+11 vs. traps); __Will__: +8"
hp: 28
health:
  - name: "HP"
    desc: "28"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sap +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The saboteur deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 153."
```

```encounter-table
name: Saboteur
creatures:
  - 1: Saboteur
```
