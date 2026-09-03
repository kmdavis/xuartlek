---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Innkeeper"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Innkeeper"
level: 1
source: "NPC Core"
aon_id: "creature-3496"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3496"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Innkeeper"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Accounting Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Alcohol Lore]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Cooking Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7"
abilityMods: [2, 0, 0, 2, 2, 3]
abilities_top:
  - name: "Font of Gossip"
    desc: "The innkeeper's business gives them insight into the neighborhood's happenings. A person can [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]] from an innkeeper in 30 minutes rather than canvassing an entire neighborhood. Each person can learn gossip from an innkeeper only once per day, and only if the innkeeper is [[srd/pf2e/compendium/rules-elements/conditions#Friendly|friendly]] or [[srd/pf2e/compendium/rules-elements/conditions#Helpful|helpful]] to that individual. Whatever information the innkeeper knows about a given topic doesn't change if someone else asks the innkeeper about that topic, unless the innkeeper has since learned more."
  - name: "Items"
    desc: "broom (functions as a [[srd/pf2e/compendium/equipment/weapons/club/staff|staff]]), innkeeper's apron (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), ledger, pewter mug"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +3; __Will__: +9"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ broom +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ pewter mug +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Home Base Brawler"
    desc: "The innkeeper knows how to settle fights that break out. When the innkeeper is fighting in their establishment, their Strikes gain a +1 circumstance bonus to the attack roll, deal an additional 1d4 damage, and gain the [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] trait if they don't already have it. The innkeeper can choose not to gain this benefit."
  - name: "Innkeeper's Advice"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|Fortune]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The innkeeper gives some pertinent advice to a single creature other than themself. For 24 hours, when that creature fails a skill check or saving throw, they can recall this advice and reroll the check, using the second result instead. Once that creature uses this ability, its effect ends. A creature that receives the Innkeeper's Advice is temporarily immune to the ability for 1 month."
sourcebook: "_NPC Core_, page 69."
```

```encounter-table
name: Innkeeper
creatures:
  - 1: Innkeeper
```
