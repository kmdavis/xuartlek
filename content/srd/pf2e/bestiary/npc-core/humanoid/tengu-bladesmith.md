---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tengu Bladesmith"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tengu
  - pf2e/creature/trait/medium
statblock: inline
name: "Tengu Bladesmith"
level: 6
source: "NPC Core"
aon_id: "creature-3672"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3672"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tengu Bladesmith"
level: "Creature 6"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Tengu; plus two others"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/lore|Tengu Lore]] +14"
abilityMods: [4, 3, 2, 1, 1, 1]
abilities_top:
  - name: "Items"
    desc: "cold iron [[srd/pf2e/compendium/equipment/weapons/sword/wakizashi|wakizashi]], _+1 [[srd/pf2e/compendium/equipment/weapons/sword/katana|katana]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +16; __Will__: +11"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _katana_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d6+7 slashing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ cold iron wakizashi +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 1d4+7 slashing"
  - name: "Melee"
    desc: "⬻ beak +15 __Damage__ 1d6+7 piercing"
abilities_bot:
  - name: "Feinting Failure"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The tengu bladesmith's previous action this turn was a Strike that failed or critically failed"
  - name: "Effect"
    desc: "The tengu bladesmith Strikes the same target, who is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against this attack. On a hit, the bladesmith deals 1d6 additional precision damage."
  - name: "Swirling Blade"
    desc: "⬻ The tengu bladesmith Interacts to draw a weapon in the sword group, then attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] a weapon held by a foe within reach. The weapon the tengu bladesmith draws gains the [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|disarm]] trait for this attempt."
sourcebook: "_NPC Core_, page 213."
```

```encounter-table
name: Tengu Bladesmith
creatures:
  - 1: Tengu Bladesmith
```
