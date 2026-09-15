---
noteType: pf2eMonster
aliases: "Katpaskir"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Katpaskir"
level: 18
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4322"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Katpaskir"
level: "Creature 18"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 31
perception:
  - name: "Perception"
    desc: "+31; darkvision, [[srd/pf2e/compendium/spells/rank-2/See the Unseen|_see the unseen_]], warp sense"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +31, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +35, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +31, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +32, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +31, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +31"
abilityMods: [6, 5, 9, 7, 6, 5]
abilities_top:
  - name: "Warp Sense"
    desc: "The katpaskir senses changes in the planar fabric within 1 mile, including any [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effects, sensing the direction and distance to the disturbance. If it senses such a disturbance within 500 feet, the katpaskir can cast [[srd/pf2e/compendium/spells/rank-5/Scouting Eye|_scouting eye_]] to observe the area without needing [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Effects#Line of Sight|line of sight]] to the location."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +35; __Ref__: +29; __Will__: +30 +1 status to all saves vs. magic"
hp: 415
health:
  - name: "HP"
    desc: "415; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Distortion Field"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]]) 30 feet. Reality bends and warps all senses without displacing the katpaskir's actual location. Creatures of the katpaskir's choice who start their turn in the aura must succeed at a DC 37 Will save or treat the area as [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Difficult Terrain|greater difficult terrain]] and [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Uneven Ground|uneven ground]] (DC 20). A creature that succeeds still treats the area as difficult terrain. For chosen creatures, the distance through the aura is doubled for determining range penalty."
  - name: "Breach Planar Wards"
    desc: "⭓"
  - name: "Trigger"
    desc: "An effect attempts to prevent the katpaskir from using a [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effect or from casting [[srd/pf2e/compendium/spells/rank-5/Summon Fiend|_summon fiend_]]"
  - name: "Effect"
    desc: "The katpaskir attempts to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] the triggering effect (counteract modifier of +29). The katpaskir automatically fails against an artifact's effect."
  - name: "Mirrored Summons"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 30 feet that the katpaskir is aware of casts [[srd/pf2e/compendium/spells/rank-5/Summon Celestial|_summon celestial_]] or otherwise summons a [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] creature"
  - name: "Effect"
    desc: "The katpaskir casts [[srd/pf2e/compendium/spells/rank-5/Summon Fiend|_summon fiend_]], regaining the daily ability to do so if needed. This effect is automatically [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|sustained]] as long as the triggering summoning is sustained, for up to 1 minute."
speed: "35 feet, burrow 15 feet, fly 35 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ claw +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d12+14 slashing plus 1d6 spirit"
  - name: "Melee"
    desc: "⬻ talon +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d8+14 slashing plus 1d6 spirit"
abilities_bot:
  - name: "Dimensional Ambush"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The katpaskir casts [[srd/pf2e/compendium/spells/rank-4/Translocate|_translocate_]], then makes a melee Strike that deals three extra dice of damage. This Strike counts as two attacks when calculating the katpaskir's multiple attack penalty. Rift Makers Katpaskirs sense weaknesses in planar fabric. These demons worm their way into spaces between dimensions and break down the barriers. They leave holes aimed at causing chaos and dissolution. In this way, katpaskirs gnaw at reality, hoping to one day unravel it."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Planar Tether|Planar Tether]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Scouting Eye|Scouting Eye]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]], [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]] - __8th__ [[srd/pf2e/compendium/spells/rank-5/Banishment|Banishment]] (×3), [[srd/pf2e/compendium/spells/rank-6/Disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-4/Flicker|Flicker]] - __9th__ [[srd/pf2e/compendium/spells/rank-5/Summon Fiend|Summon Fiend]] (demons only) - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
  - name: "Rituals"
    desc: "DC 40 - __1st__ [[srd/pf2e/compendium/spells/rituals/Demonic Pact|Demonic Pact]]"
sourcebook: "_Monster Core 2_, page 94."
```

```encounter-table
name: Katpaskir
creatures:
  - 1: Katpaskir
```
