---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tzitzimitl"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/electricity
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tzitzimitl"
level: 19
source: "Monster Core 2"
other_sources: "Pathfinder #150: Broken Promises"
aon_id: "creature-4597"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4597"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tzitzimitl"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Electricity"
trait_02: "Uncommon"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +37, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +37, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +37, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +40"
abilityMods: [10, 8, 6, 5, 7, 8]
ac: 43
armorclass:
  - name: "AC"
    desc: "43; __Fort__: +29; __Ref__: +32; __Will__: +35"
hp: 390
health:
  - name: "HP"
    desc: "390 (fast healing 15, void healing (page 362)); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15, physical 15 (except bludgeoning); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Light to Dark"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]])"
  - name: "Trigger"
    desc: "A creature uses an ability or spell with the [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] trait within 120 feet of the tzitzimitl"
  - name: "Effect"
    desc: "The tzitzimitl inverts the energy used in the triggering ability or spell, causing it to lose the vitality trait and gain the void trait, and changing all instances of vitality energy or healing in the ability's description to void energy."
speed: "50 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d12+10 slashing plus 3d8 electricity and drain life"
  - name: "Ranged"
    desc: "⬻ eye beam +34 (range 100 feet) __Damage__ 4d12 electricity plus 10d6 force"
abilities_bot:
  - name: "Drain Life"
    desc: "When a tzitzimitl's claw Strike deals damage to a living creature, the tzitzimitl gains 20 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]], and the target must succeed at a DC 41 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 2. Further damage dealt by a tzitzimitl's claw Strike increases the value of the drained condition by 2 on a failed save, to a maximum of drained 4."
  - name: "Eclipse"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Effect"
    desc: "The tzitzimitl casts [[srd/pf2e/compendium/spells/rank-2/darkness|_darkness_]] and drains the heat and warmth from the darkness spell's area. Each creature within the spell's area must attempt a DC 41 Fortitude save."
  - name: "Critical Success"
    desc: "The creature takes 4d8 cold damage."
  - name: "Success"
    desc: "The creature takes 8d8 cold damage and is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for 1 round."
  - name: "Failure"
    desc: "The creature takes 16d8 cold damage and is slowed 1 for 1 minute."
  - name: "Critical Failure"
    desc: "The creature takes 16d8 cold damage, is slowed 2 for 1 minute, and is [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1. Harbingers Of The End A tzitzimitl's arrival in a region often precedes a deadly disaster or apocalyptic event. It isn't known whether the tzitzimitl accompanies an event already fated to occur or if the undead causes such events through their own strange magic."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 38 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/haste|Haste]] (×3) - __4th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-7/eclipse-burst|Eclipse Burst]], [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]] (×3) - __9th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (×3), [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]], [[srd/pf2e/compendium/spells/rank-9/wails-of-the-damned|Wails of the Damned]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 38 - __2nd__ Create Undead (9th rank)"
sourcebook: "_Monster Core 2_, page 334."
```

```encounter-table
name: Tzitzimitl
creatures:
  - 1: Tzitzimitl
```
