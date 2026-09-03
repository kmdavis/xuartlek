---
obsidianUIMode: preview
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
aon_id: "creature-3441"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3441"
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
    desc: "Perception +8"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7"
abilityMods: [3, 1, 0, 1, 2, 3]
abilities_top:
  - name: "Twisted Faith"
    desc: "When attempting a [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] skill check, the blasphemer can roll [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] instead, so long as they have an intelligent creature around as a witness. If the creature is a follower of the blasphemer's faith, the blasphemer receives a +2 circumstance bonus to the check."
  - name: "Items"
    desc: "Hand Crossbow, [[srd/pf2e/compendium/equipment/adventuring-gear/religious-symbol-silver|religious symbol]] of Zon-Kuthon, spiked chain"
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
    desc: "⬻ spiked chain +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d8+5 slashing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +7 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "False Blessing"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The blasphemer attempts a DC 15 [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] check to attempt to cast the 1st-rank spell their deity grants to clerics ([[srd/pf2e/compendium/spells/rank-1/phantom-pain|_phantom pain_]] for Zon-Kuthon). The spell must take 1, 2, or 3 actions to Cast. The blasphemer can use twisted faith to roll [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] instead if they have a witness, as normal."
  - name: "Critical Success"
    desc: "The blasphemer successfully Casts the Spell, then is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] with a value equal to the number of actions the spell takes – 1."
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
