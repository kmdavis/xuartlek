---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mythic Ogre Boss"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Mythic Ogre Boss"
level: 7
source: "War of Immortals"
aon_id: "creature-3401"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3401"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Mythic Ogre Boss"
level: "Creature 7"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Mythic"
trait_04: "Rare"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [7, 0, 4, 0, 1, 1]
abilities_top:
  - name: "Titanic Might"
    desc: ""
  - name: "Items"
    desc: "Breastplate, Javelin (6), _+1 [[srd/pf2e/compendium/equipment/weapons/pick/ogre-hook|ogre hook]]_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +12; __Will__: +15"
hp: 130
health:
  - name: "HP"
    desc: "130; __Resistances__ [[srd/pf2e/books/war-of-immortals/mythic-rules/mythic-monster-templates#Basic Mythic Abilities|mythic resistance]] 7"
abilities_mid:
  - name: "Mythic Ferocity"
    desc: "⬲"
  - name: "Cost"
    desc: "1 Mythic Point, 65 HP"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ; _ogre hook_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d10+11 piercing"
  - name: "Ranged"
    desc: "⬻ javelin +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+11 piercing"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Mythic Skill_ ⭓"
  - name: "Cost"
    desc: "1 Mythic Point; [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]]"
  - name: "Bellowing Command"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The ogre boss issues a command to hasten their fellows. Each ogre ally who hears and understands this command becomes [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] until the end of that ally's next turn, but can use the extra action only to Step or Stride."
  - name: "Sweeping Hook"
    desc: "⬲"
  - name: "Trigger"
    desc: "The ogre boss successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trips]] a creature using an ogre hook"
  - name: "Effect"
    desc: "The ogre boss makes an ogre hook Strike against the creature they tripped."
sourcebook: "_War of Immortals_, page 171."
```

```encounter-table
name: Mythic Ogre Boss
creatures:
  - 1: Mythic Ogre Boss
```
