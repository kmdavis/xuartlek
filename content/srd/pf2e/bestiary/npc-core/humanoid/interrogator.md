---
noteType: pf2eMonster
aliases: "Interrogator"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Interrogator"
level: 6
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3615"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Interrogator"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +13"
abilityMods: [4, 3, 1, 0, 2, 2]
abilities_top:
  - name: "Items"
    desc: "Dart (5), [[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit|Healer's Toolkit]], leather apron (functions as [[srd/pf2e/compendium/equipment/Armor#Leather Armor|leather armor]]), _+1 [[srd/pf2e/compendium/equipment/weapons/knife/War Razor|war razor]]_"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +12; __Ref__: +12; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _war razor_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Backstabber|Backstabber]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d4+10 slashing plus torment"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning plus torment"
  - name: "Ranged"
    desc: "⬻ dart +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+7 piercing plus torment"
abilities_bot:
  - name: "Blood and Fear"
    desc: "⬺ The interrogator Strikes with a slashing melee weapon. If they hit and deal damage, the target takes an additional 1d4 persistent bleed damage and is [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]] (or 2d4 persistent bleed damage and frightened 2 on a critical hit). Each of the interrogator's other enemies in a 30-foot emanation around the target that witnesses the bloodshed must succeed at a DC 19 Will save or be frightened 1. The frightened part of this ability is an [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], and [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]] effect."
  - name: "Hobble"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] by the interrogator"
  - name: "Effect"
    desc: "One creature grabbed or restrained by the interrogator takes 2d6 bludgeoning damage with a DC 23 basic Fortitude save. If the creature fails its save, it also gains a condition of the interrogator's choice: [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 2]] for 1 minute, [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled 2]] for 1 minute, or [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]]."
  - name: "Torment"
    desc: "The interrogator's Strikes deal an additional 1d8 mental damage to [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] creatures."
sourcebook: "_NPC Core_, page 158."
```

```encounter-table
name: Interrogator
creatures:
  - 1: Interrogator
```
