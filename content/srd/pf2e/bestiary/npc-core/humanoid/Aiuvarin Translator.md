---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3630"
socialImage: og-image.png
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
    desc: "+5; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]]; two other common or [[srd/pf2e/compendium/rules-elements/traits/player-core/Uncommon|uncommon]] languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +7, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +7, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +6, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +5, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +7"
abilityMods: [0, 2, 0, 3, 1, 2]
abilities_top:
  - name: "Linguistic Mastery"
    desc: "The translator gains a +5 circumstance bonus to skill checks involving translating or deciphering languages. If the translator rolls a critical failure on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Decipher Writing|Decipher Writing]], they get a failure instead."
  - name: "Translation Specialist"
    desc: "For encounters involving translating or deciphering languages, the translator is a 4th-level challenge."
  - name: "Items"
    desc: "book of translations, quill pen (functions as a [[srd/pf2e/compendium/equipment/weapons/dart/Dart|dart]]), Staff, Writing Set"
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
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "A creature within 20 feet of the translator would be targeted by or in the area of an ability with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]] trait"
  - name: "Effect"
    desc: "The translator attempts a [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] check with a +5 circumstance bonus against the Will DC of the creature. On a success, the creature is unaffected by the linguistic effect, and the translator can choose to make the creature [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] until the end of the creature's next turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ quill pen +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d4+2 piercing"
sourcebook: "_NPC Core_, page 178."
```

```encounter-table
name: Aiuvarin Translator
creatures:
  - 1: Aiuvarin Translator
```
