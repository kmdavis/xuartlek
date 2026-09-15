---
noteType: pf2eMonster
aliases: "Ogre Boss"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Ogre Boss"
level: 7
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3120"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ogre Boss"
level: "Creature 7"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11"
abilityMods: [7, 0, 4, 0, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Javelin (6), _+1 ogre hook_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +12; __Will__: +15"
hp: 130
health:
  - name: "HP"
    desc: "130"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _ogre hook_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d10+11 piercing"
  - name: "Ranged"
    desc: "⬻ javelin +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]]) __Damage__ 1d6+11 piercing"
abilities_bot:
  - name: "Bellowing Command"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The ogre boss issues a command to hasten their fellows. Each ogre ally who hears and understands this command becomes [[srd/pf2e/compendium/rules-elements/Conditions#Quickened|quickened]] until the end of that ally's next turn but can use the extra action only to Step or Stride."
  - name: "Sweeping Hook"
    desc: "⬲"
  - name: "Trigger"
    desc: "The ogre boss successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trips]] a creature using an ogre hook"
  - name: "Effect"
    desc: "The ogre boss makes an ogre hook Strike against the creature they tripped."
sourcebook: "_Monster Core_, page 251."
```

```encounter-table
name: Ogre Boss
creatures:
  - 1: Ogre Boss
```
