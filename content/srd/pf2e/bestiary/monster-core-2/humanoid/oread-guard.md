---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Oread Guard"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/oread
  - pf2e/creature/trait/medium
statblock: inline
name: "Oread Guard"
level: 1
source: "Monster Core 2"
aon_id: "creature-4508"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4508"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Oread Guard"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Oread"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +3, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +3, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [4, 1, 2, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Bastard Sword, Full Plate, light hammer, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +6; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bastard sword +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d12]]) __Damage__ 1d8+4 slashing"
  - name: "Ranged"
    desc: "⬻ light hammer +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Vicious Blow"
    desc: "⬺ The oread guard makes a melee Strike. This counts as two attacks when calculating the guard's multiple attack penalty. If this Strike hits, the oread guard deals an extra die of weapon damage."
sourcebook: "_Monster Core 2_, page 251."
```

```encounter-table
name: Oread Guard
creatures:
  - 1: Oread Guard
```
