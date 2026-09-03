---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Legbreaker"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Legbreaker"
level: 6
source: "NPC Core"
aon_id: "creature-3431"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3431"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Legbreaker"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +13"
abilityMods: [4, 3, 3, -1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/hammer/maul|maul]]_, studded leather"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +15; __Will__: +12"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _maul_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d10+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 bludgeoning __Break Legs!__ ⬺ The legbreaker makes a maul Strike against an adjacent creature. If it hits, the creature is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] and becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] for 1 minute. As long as this clumsy condition lasts, the creature also takes a –5-foot penalty to its Speeds and has weakness 5 to the legbreaker's Strikes."
abilities_bot:
  - name: "Rushing Strike"
    desc: "⬺ The legbreaker Strides twice. If they end their movement within melee reach of an enemy, they can make a melee Strike against that enemy."
  - name: "Stampeding Shove"
    desc: "⬻ The legbreaker [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shoves]] a creature, gaining a +2 circumstance bonus to their Athletics check if the target is [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. If the Shove succeeds, the target takes 2d10 bludgeoning damage (double damage on a critical success)."
sourcebook: "_NPC Core_, page 21."
```

```encounter-table
name: Legbreaker
creatures:
  - 1: Legbreaker
```
