---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf Warrior"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dwarf Warrior"
level: 1
source: "Monster Core"
aon_id: "creature-2965"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2965"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dwarf Warrior"
level: "Creature 1"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Dwarven|Dwarven]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +3, Dwarven Lore +5"
abilityMods: [4, 1, 3, 1, 3, -1]
abilities_top:
  - name: "Items"
    desc: "Half Plate, Steel Shield (Hardness 5, HP 20, BT 10), warhammer"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +3; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d8+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ clan dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/parry|Parry]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile B]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Dwarven Doughtiness"
    desc: "A dwarf is often calm and collected in the face of imminent danger. At the end of this dwarf's turn, reduce their [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition by 2 instead of 1."
  - name: "Shielded Charge"
    desc: "⬺ The dwarf warrior [[srd/pf2e/compendium/rules-elements/actions/player-core#Raise a Shield|Raises a Shield]] and Strides twice."
sourcebook: "_Monster Core_, page 135."
```

```encounter-table
name: Dwarf Warrior
creatures:
  - 1: Dwarf Warrior
```
