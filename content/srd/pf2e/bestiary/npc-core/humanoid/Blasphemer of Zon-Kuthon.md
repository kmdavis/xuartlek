---
noteType: pf2eMonster
aliases: "Blasphemer of Zon-Kuthon"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Blasphemer of Zon-Kuthon"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3441"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Blasphemer of Zon-Kuthon"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +6, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +7"
abilityMods: [3, 1, 0, 1, 2, 3]
abilities_top:
  - name: "Twisted Faith"
    desc: "When attempting a [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] skill check, the blasphemer can roll [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] instead, so long as they have an intelligent creature around as a witness. If the creature is a follower of the blasphemer's faith, the blasphemer receives a +2 circumstance bonus to the check."
  - name: "Items"
    desc: "Hand Crossbow, [[srd/pf2e/compendium/equipment/adventuring-gear/Religious Symbol|religious symbol]] of [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Zon-Kuthon|Zon-Kuthon]], spiked chain"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +7; __Will__: +10"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spiked chain +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d8+5 slashing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +7 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "False Blessing"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]]) The blasphemer attempts a DC 15 [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] check to attempt to cast the 1st-rank spell their deity grants to clerics ([[srd/pf2e/compendium/spells/rank-1/Phantom Pain|_phantom pain_]] for [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Zon-Kuthon|Zon-Kuthon]]). The spell must take 1, 2, or 3 actions to Cast. The blasphemer can use twisted faith to roll [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] instead if they have a witness, as normal."
  - name: "Critical Success"
    desc: "The blasphemer successfully Casts the Spell, then is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] with a value equal to the number of actions the spell takes – 1."
  - name: "Success"
    desc: "As critical success, plus the blasphemer takes 1d6 mental damage."
  - name: "Failure"
    desc: "The blasphemer fails to Cast the Spell and takes 1d6 mental damage."
  - name: "Critical Failure"
    desc: "The blasphemer fails to Cast the Spell, takes 2d6 mental damage, and is stunned 1."
sourcebook: "_NPC Core_, page 29."
```

```encounter-table
name: Blasphemer of Zon-Kuthon
creatures:
  - 1: Blasphemer of Zon-Kuthon
```
