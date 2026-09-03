---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ocean Nomad"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Ocean Nomad"
level: 6
source: "NPC Core"
aon_id: "creature-3605"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3605"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Ocean Nomad"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +13"
abilityMods: [4, 4, 2, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Leather Armor, Net, _+1 [[srd/pf2e/compendium/equipment/weapons/spear/trident|trident]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +17; __Will__: +11"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Tidal Pressure"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]])"
  - name: "Trigger"
    desc: "An adjacent creature attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]]"
  - name: "Effect"
    desc: "The ocean nomad chooses to either prop the swimmer up or yanks them down into the depths. Increase or decrease the result of the Athletics check by one step. If the ocean nomad chooses to decrease the result, the creature can attempt a DC 24 Fortitude save to negate the effect."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +17 __Damage__ 1d8+10 piercing"
  - name: "Ranged"
    desc: "⬻ _trident_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d8+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning"
abilities_bot:
  - name: "Stab and Twist"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ocean nomad's last action was a successful melee trident Strike"
  - name: "Effect"
    desc: "The ocean nomad wrenches out the barbed tines of their trident, inflicting 1d6 persistent bleed to the target."
sourcebook: "_NPC Core_, page 150."
```

```encounter-table
name: Ocean Nomad
creatures:
  - 1: Ocean Nomad
```
