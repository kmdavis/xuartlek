---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crag Linnorm"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Crag Linnorm"
level: 14
source: "Monster Core"
aon_id: "creature-3083"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3083"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Crag Linnorm"
level: "Creature 14"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Uncommon"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, scent (imprecise) 60 feet, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +28"
abilityMods: [8, 4, 6, -3, 4, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +28; __Ref__: +24; __Will__: +22 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 270
health:
  - name: "HP"
    desc: "270 , regeneration 10 (deactivated by [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Curse of Fire"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) When a creature slays the crag linnorm, it must succeed at a DC 35 Will save or gain weakness to fire 15 with an unlimited duration."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "35 feet, fly 100 feet, swim 60 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d12+14 piercing plus crag linnorm venom"
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d8+14 slashing"
  - name: "Melee"
    desc: "⬻ tail +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d6+14 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d6+14 bludgeoning, DC 34"
  - name: "Crag Linnorm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 34 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "4d6 fire damage and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "6d6 fire damage and drained 2 (1 round)"
  - name: "Magma Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The crag linnorm breathes out a stream of magma in a 120-foot line that deals 12d6 fire damage to creatures within the area (DC 34 basic Reflex save). Any creature that fails its save also takes 4d6 persistent fire damage. The linnorm can't use Magma Breath again for 1d4 rounds. The magma remains until the start of the linnorm's next turn. If the linnorm was on the ground, the magma remains as a burning line on the ground directly under the line of the Magma Breath; if the linnorm was airborne, the magma rains down in a sheet 60 feet high. Any creature that moves across or through the magma takes 6d6 fire damage (DC 34 basic Reflex save). At the start of the linnorm's next turn, the magma cools to a thin layer of brittle stone, or the magma rain finishes falling and turns to harmless pebbles. The cooled magma quickly degrades to powder and sand over the course of several hours."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33 - __6th__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 220."
```

```encounter-table
name: Crag Linnorm
creatures:
  - 1: Crag Linnorm
```
