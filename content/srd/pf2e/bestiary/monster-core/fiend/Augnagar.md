---
noteType: pf2eMonster
aliases: "Augnagar"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/qlippoth
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Augnagar"
level: 14
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3156"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Augnagar"
level: "Creature 14"
size: "Huge"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "+27; darkvision, scent (imprecise) 30 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +27, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +26"
abilityMods: [8, 5, 8, -2, 5, 4]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +28; __Ref__: +23; __Will__: +25"
hp: 225
health:
  - name: "HP"
    desc: "225; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 15, physical 15 (except cold iron)"
speed: "40 feet, climb 40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d12+14 piercing plus 3d6 persistent bleed and rotting curse"
  - name: "Melee"
    desc: "⬻ sting +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d8+14 slashing plus 3d6 persistent bleed"
abilities_bot:
  - name: "Confusing Display"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) The augnagar's writhing limbs and flesh seethe and squirm in a disorienting and unsettling manner. Creatures in a 30-foot emanation must attempt a DC 34 Will save, after which they are temporarily immune to further Confusing Displays for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] for 1 round."
  - name: "Failure"
    desc: "The creature is stupefied 1 and [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the creature can't attempt a flat check to recover from confusion whenever it takes damage from an attack or spell."
  - name: "Inhale Vitality"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The augnagar inhales sharply, drawing life force out of creatures in a 50-foot cone. Creatures in the area take 14d6 void damage with a DC 34 basic Fortitude save. A creature that fails its save is also [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]]. If any creatures take damage from this activity, the augnagar becomes [[srd/pf2e/compendium/rules-elements/Conditions#Quickened|quickened]] for 1 round, and it can use the extra action only to Stride or Strike."
  - name: "Rotting Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]] (1 day)"
  - name: "Stage 2"
    desc: "drained 2 and the creature displays hideous, festering wounds exuding a horrific stench. When the victim takes piercing or slashing damage, creatures within 30 feet must succeed at a DC 32 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 1]]. The victim automatically fails this save (1 day)."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 31 - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (×3) - __Constant (7th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core_, page 281."
```

```encounter-table
name: Augnagar
creatures:
  - 1: Augnagar
```
