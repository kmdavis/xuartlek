---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ice Linnorm"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ice Linnorm"
level: 17
source: "Monster Core"
aon_id: "creature-3084"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3084"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ice Linnorm"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Cold"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, scent (imprecise) 60 feet, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +28, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +32"
abilityMods: [9, 5, 7, -3, 6, 7]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +32; __Ref__: +28; __Will__: +27 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 330
health:
  - name: "HP"
    desc: "330 , regeneration 10 (deactivated by [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]]; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Curse of Frost"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) When a creature slays the ice linnorm, it must succeed at a DC 40 Will save or gain weakness to cold 15 with an unlimited duration."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "35 feet, fly 100 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d12+17 piercing plus ice linnorm venom"
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d6+17 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d6+18 bludgeoning, DC 38"
  - name: "Ice Linnorm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 38 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "5d6 cold damage and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "7d6 cold damage and drained 2 (1 round)"
  - name: "Icemire Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The ice linnorm spews out a blast of freezing, viscous ooze in a 60-foot cone that deals 15d6 cold damage to creatures within the area (DC 38 basic Reflex save). The freezing ooze clings to those struck and hardens into thick sheets of ice. A creature that fails the saving throw is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] by the ice until it succeeds at a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] or it or an ally [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Forces Open]] the ice (DC 34 for either case). At the start of its turn, a creature still immobilized by the ice takes 4d6 cold damage. Another creature can free a frozen target by dealing a total of 20 fire damage to the frozen target. Left unattended, the ice crumbles away in 1 minute on its own. Creatures with the [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] trait can't be frozen in place by Icemire Breath. Flying creatures fall if frozen, and swimming creatures that are frozen rise toward the surface of the water at a speed of 60 feet per round. The linnorm can't use Icemire Breath again for 1d4 rounds."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 38 - __7th__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 221."
```

```encounter-table
name: Ice Linnorm
creatures:
  - 1: Ice Linnorm
```
