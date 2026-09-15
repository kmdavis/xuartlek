---
noteType: pf2eMonster
aliases: "Tripkee Fiend Keeper"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Fiend Keeper"
level: 7
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3675"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tripkee Fiend Keeper"
level: "Creature 7"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Tripkee|Tripkee]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +16, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +16"
abilityMods: [2, 3, 2, 1, 4, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/club/Cruuk|cruuk]]_, Leather Armor"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +15; __Will__: +18"
hp: 125
health:
  - name: "HP"
    desc: "125"
speed: "25 feet, climb 20 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ _cruuk_ +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]]) __Damage__ 1d6+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ cruuk +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]]) __Damage__ 1d6+5 bludgeoning"
abilities_bot:
  - name: "Bounce Cruuk"
    desc: "⬺ The tripkee fiend keeper makes a ranged Strike with their cruuk against a target within 30 feet. Once the Strike is complete, the cruuk ricochets back into the tripkee fiend keeper's hand. If their hands are full when the cruuk returns, it falls to the ground in their space."
  - name: "Harness Wickedness"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]])"
  - name: "Requirements"
    desc: "The tripkee fiend keeper isn't [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]]"
  - name: "Effect"
    desc: "The tripkee fiend keeper allows a portion of the fiendish power they have absorbed to flow through their body. For the next minute, the tripkee fiend keeper's Strikes deal an additional die of damage and gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] trait. The tripkee fiend keeper also gains 10 temporary Hit Points, a +5- foot status bonus to Speed for the duration, and weakness 5 to [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]]. At the end of the duration, the tripkee fiend keeper is stupefied 1 for 1 hour."
  - name: "Hunter of Virtue"
    desc: "Whenever the tripkee fiend keeper critically hits an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] creature, they reduce the value of their stupefied condition by 1."
  - name: "Forest Passage"
    desc: "The tripkee ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 215."
```

```encounter-table
name: Tripkee Fiend Keeper
creatures:
  - 1: Tripkee Fiend Keeper
```
