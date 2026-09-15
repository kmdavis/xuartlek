---
noteType: pf2eMonster
aliases: "Samsaran Anchorite"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/samsaran
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Samsaran Anchorite"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4539"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Samsaran Anchorite"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Samsaran"
trait_03: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "+9; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Samsaran"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +6, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +6, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +7, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +4"
abilityMods: [0, 2, 0, 1, 4, 2]
abilities_top:
  - name: "Cryptomnesia"
    desc: "A samsaran subconsciously retains bits of knowledge from their innumerable former lives, granting them a +1 circumstance bonus to skill checks that aren't listed in their skills above and allowing them to attempt all skill actions that normally require the user to be trained."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sling/Sling|Sling]] (10 bullets), [[srd/pf2e/compendium/equipment/weapons/spear/Spear|Spear]]"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +3; __Ref__: +7; __Will__: +9"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "All This Has Happened Before"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The samsaran is about to roll initiative"
  - name: "Effect"
    desc: "The anchorite experiences a flash of recognition from a previous existence, gaining a +4 circumstance bonus to the triggering roll. If this causes the anchorite to be the first creature to act, they also become [[srd/pf2e/compendium/rules-elements/Conditions#Quickened|quickened]] for 1 round, but they can use the extra action only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Step|Step]]."
  - name: "All This Will Happen Again"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The samsaran fails or critically fails a Will save against an [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]] effect"
  - name: "Effect"
    desc: "Even in the face of overwhelming tribulation, the anchorite finds solace in the notion that all things are merely part of a never-ending cycle. They reroll the saving throw with a +1 status bonus; they must use the second result."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spear +5 __Damage__ 1d6+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +7 (range increment 50 feet, reload 1) __Damage__ 1d4+2 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Command|Command]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/Sanctuary|Sanctuary]]"
sourcebook: "_Monster Core 2_, page 280."
```

```encounter-table
name: Samsaran Anchorite
creatures:
  - 1: Samsaran Anchorite
```
