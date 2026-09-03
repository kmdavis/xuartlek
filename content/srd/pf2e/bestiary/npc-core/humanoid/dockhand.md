---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dockhand"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dockhand"
level: 0
source: "NPC Core"
aon_id: "creature-3490"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3490"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dockhand"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +3, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/lore|Labor Lore]] +4"
abilityMods: [3, 1, 3, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "empty bottle, whiskey, work clothes (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]])"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +5; __Will__: +3"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ bottle +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 15 feet]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Heft Crate"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The dockhand is adjacent to a crate"
  - name: "Effect"
    desc: "The dockhand picks up a crate and heaves it up to 15 feet. Upon landing, the crate breaks open in a 5-foot burst. Each creature in the area takes 2d6 bludgeoning damage with a DC 13 basic Reflex save, and the area is difficult terrain until cleared."
  - name: "Swig"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The dockhand Interacts to either draw a bottle of alcohol or pick up a nearby unattended bottle of alcohol, then drinks the whole thing. For 1 minute, the dockhand gains a +2 item bonus to melee damage rolls and saving throws against [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] but is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]."
sourcebook: "_NPC Core_, page 66."
```

```encounter-table
name: Dockhand
creatures:
  - 1: Dockhand
```
