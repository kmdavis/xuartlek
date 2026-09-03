---
obsidianUIMode: preview
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
aon_id: "creature-3608"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3608"
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
    desc: "Perception +8; (10 to find traps)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +6"
abilityMods: [1, 3, 1, 2, 2, 1]
abilities_top:
  - name: "Snare Crafting"
    desc: "The saboteur can [[srd/pf2e/compendium/rules-elements/actions/player-core#Craft|Craft]] snares and has the supplies to make up to two [[srd/pf2e/compendium/equipment/snares/caltrop-snare|caltrop snares]] and up to two [[srd/pf2e/compendium/equipment/snares/hampering-snare|hampering snares]]. Snare rules can be found [[srd/pf2e/books/player-core-2/snares/index|here]]."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]] (snare toolkit), Crowbar, Disguise Kit, Hand Crossbow (10 bolts), Sap, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
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
    desc: "⬻ sap +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The saboteur deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 153."
```

```encounter-table
name: Saboteur
creatures:
  - 1: Saboteur
```
