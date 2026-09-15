---
noteType: pf2eMonster
aliases: "Vrolikai"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Vrolikai"
level: 20
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2901"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vrolikai"
level: "Creature 20"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 34
perception:
  - name: "Perception"
    desc: "+34; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +37, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +33, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +36, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +36, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +38, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +34, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +34, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +34"
abilityMods: [10, 7, 9, 6, 6, 8]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +35; __Ref__: +33; __Will__: +34 +1 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 440
health:
  - name: "HP"
    desc: "440; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Death-Stealing Gaze"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) 30 feet. When a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Demon|demon]] ends its turn in the aura, it must attempt a DC 38 Fortitude save. If it fails, it becomes [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]]. A creature that dies while it has drain from a vrolikai's gaze rises as a [[srd/pf2e/compendium/gm/creature-families/Ghoul|ghoul]] the next midnight. The GM determines what kind of ghoul."
speed: "35 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ black flame knife +40 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d4+18 piercing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d12+18 piercing"
  - name: "Melee"
    desc: "⬻ stinger +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d8+18 piercing plus mindwarping"
abilities_bot:
  - name: "Black Flame Knives"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) The vrolikai manifests a dagger-shaped blade of what looks like crystallized black flame in each of their four hands. These weapons function as _+2 [[srd/pf2e/compendium/equipment/runes/Striking|greater striking]] [[srd/pf2e/compendium/equipment/weapons/knife/Dagger|daggers]]_ that deal an additional 2d6 void damage. They fade away into nothingness 1 minute after a vrolikai no longer carries them."
  - name: "Consume Death"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The vrolikai focuses their deathstealing gaze upon a single target they can see within 30 feet. The target must immediately attempt a Fortitude save against death-stealing gaze."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is affected by death-stealing gaze and becomes [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]]. If the creature was already drained 1 by the death-stealing gaze before attempting the save, a failed save increases the value of the drained condition by 1, to a maximum of drained 4. The vrolikai gains 10 temporary Hit Points, and the drained creature is temporarily immune until the start of the vrolikai's next turn."
  - name: "Critical Failure"
    desc: "As failure, but the creature increases the amount of drain by 2."
  - name: "Focused Flames"
    desc: "⬺ The vrolikai attacks a single target with all of their black flame knives. The demon makes a black flame knife Strike with the following additional effects. This counts toward the vrolikai's multiple attack penalty as a number of attacks equal to the number of back flame knives the vrolikai used."
  - name: "Critical Success"
    desc: "The target takes an additional 2d6 void damage for each knife beyond the first (typically 6d6 extra damage) and takes 4d6 persistent void damage."
  - name: "Success"
    desc: "The target takes an additional 2d6 void damage for each knife beyond the first."
  - name: "Failure"
    desc: "The vrolikai deals the damage their black flame knife Strike normally deals on a hit."
  - name: "Mindwarping"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The sting of a vrolikai is mind-warping. A creature struck must attempt a DC 44 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] for 1 minute."
  - name: "Failure"
    desc: "The creature becomes stupefied 1. If it's already stupefied, its stupefied value increases by 1 instead (to a maximum of stupefied 4)."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Regenerate|Regenerate]] - __10th__ [[srd/pf2e/compendium/spells/rank-7/Execute|Execute]], [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-9/Massacre|Massacre]], [[srd/pf2e/compendium/spells/rank-6/Vampiric Exsanguination|Vampiric Exsanguination]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 44 - __1st__ [[srd/pf2e/compendium/spells/rituals/Demonic Pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 82."
```

```encounter-table
name: Vrolikai
creatures:
  - 1: Vrolikai
```
