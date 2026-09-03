---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf General"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dwarf General"
level: 8
source: "NPC Core"
aon_id: "creature-3629"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3629"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dwarf General"
level: "Creature 8"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +15, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +15"
abilityMods: [5, 0, 4, 2, 2, 1]
abilities_top:
  - name: "Opening Orders"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic [free-action]]])"
  - name: "Trigger"
    desc: "The dwarf general rolls initiative and can see at least one enemy"
  - name: "Effect"
    desc: "The general unleashes a command to ready for combat. Each ally within 120 feet that can hear the general can either [[srd/pf2e/compendium/rules-elements/actions/player-core#Raise a Shield|Raise a Shield]] or Step as a free action when it rolls initiative."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/crossbow/arbalest|Arbalest]] (10 bolts), Clan Dagger, Full Plate, Steel Shield (Hardness 5, HP 20, BT 10), _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/hammer/warhammer|warhammer]]_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +14; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150"
abilities_mid:
  - name: "Dwarven Doughtiness"
    desc: "Dwarves are often calm and collected in the face of imminent danger. At the end of the general's turn, reduce its [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition by 2 instead of 1."
  - name: "Reactive Strike"
    desc: "⬲ The dwarf general gains an additional reaction at the beginning of each of their turns that they can use only for a Reactive Strike."
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _warhammer_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 2d8+11 bludgeoning"
  - name: "Melee"
    desc: "⬻ clan dagger +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile B]]) __Damage__ 1d4+11 piercing"
  - name: "Melee"
    desc: "⬻ fist +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arbalest +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backstabber|Backstabber]], range increment 110 feet, reload 1) __Damage__ 1d10+6 piercing"
abilities_bot:
  - name: "Advancing Orders"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]]) The dwarf general issues a command to push forward on the battlefield. Each ally who hears and understands this command becomes [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] until the end of its next turn but can use the extra action only to Step or Stride."
  - name: "Hammer Critical Specialization"
    desc: "When the general critically hits with a hammer, the target of the critical hit is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] unless it succeeds at a DC 26 Fortitude save."
  - name: "Sudden Charge"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dwarf general Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against that enemy."
sourcebook: "_NPC Core_, page 176."
```

```encounter-table
name: Dwarf General
creatures:
  - 1: Dwarf General
```
