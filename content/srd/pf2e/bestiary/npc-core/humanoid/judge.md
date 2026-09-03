---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Judge"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Judge"
level: -1
source: "NPC Core"
aon_id: "creature-3547"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3547"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Judge"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; (15 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +14"
abilityMods: [0, -1, 1, 3, 3, 2]
abilities_top:
  - name: "Group Impression"
    desc: "When the judge [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Makes an Impression]], they can compare their [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] check result to the Will DCs of up to four targets instead of one."
  - name: "Legal Specialist"
    desc: "In a legal proceeding, the judge is a 6th-level challenge."
  - name: "Items"
    desc: "gavel (functions as a [[srd/pf2e/compendium/equipment/weapons/club/club|club]]), judge's robes, _Law and Rhetoric_"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +5; __Ref__: +1; __Will__: +12"
hp: 5
health:
  - name: "HP"
    desc: "5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ gavel +4 __Damage__ 1d6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ gavel +3 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4 bludgeoning __Remember, You're Under Oath__ ⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The judge reminds a creature of the oath they swore to the court. The judge makes an [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check against the target' s Will DC. On a success, the target takes a –2 status penalty to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Lie|Lie]] for 10 minutes (or a –4 status penalty on a critical success). Regardless of the result, the target is temporarily immune to this ability for 24 hours."
sourcebook: "_NPC Core_, page 108."
```

```encounter-table
name: Judge
creatures:
  - 1: Judge
```
