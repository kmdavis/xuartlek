---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aiuvarin Translator"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/aiuvarin
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/half-elf
statblock: inline
name: "Aiuvarin Translator"
level: 0
source: "NPC Core"
aon_id: "creature-3630"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3630"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Aiuvarin Translator"
level: "Creature 0"
size: "Medium"
trait_01: "Aiuvarin"
trait_02: "Elf"
trait_03: "Humanoid"
trait_04: "Half-Elf"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]]; two other common or [[srd/pf2e/compendium/rules-elements/traits/player-core/uncommon|uncommon]] languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +7, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +7, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +6, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +5, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7"
abilityMods: [0, 2, 0, 3, 1, 2]
abilities_top:
  - name: "Linguistic Mastery"
    desc: "The translator gains a +5 circumstance bonus to skill checks involving translating or deciphering languages. If the translator rolls a critical failure on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Decipher Writing|Decipher Writing]], they get a failure instead."
  - name: "Translation Specialist"
    desc: "For encounters involving translating or deciphering languages, the translator is a 4th-level challenge."
  - name: "Items"
    desc: "book of translations, quill pen (functions as a [[srd/pf2e/compendium/equipment/weapons/dart/dart|dart]]), Staff, Writing Set"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +6; __Will__: +9"
hp: 12
health:
  - name: "HP"
    desc: "12"
abilities_mid:
  - name: "Crosstalk"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "A creature within 20 feet of the translator would be targeted by or in the area of an ability with the [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]] trait"
  - name: "Effect"
    desc: "The translator attempts a [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] check with a +5 circumstance bonus against the Will DC of the creature. On a success, the creature is unaffected by the linguistic effect, and the translator can choose to make the creature [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] until the end of the creature's next turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ quill pen +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d4+2 piercing"
sourcebook: "_NPC Core_, page 178."
```

```encounter-table
name: Aiuvarin Translator
creatures:
  - 1: Aiuvarin Translator
```
