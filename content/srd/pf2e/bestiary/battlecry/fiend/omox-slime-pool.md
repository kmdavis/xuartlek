---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Omox Slime Pool"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Omox Slime Pool"
level: 17
source: "Battlecry!"
aon_id: "creature-3930"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3930"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Omox Slime Pool"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Ooze"
trait_04: "Troop"
trait_05: "Unholy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +36"
abilityMods: [9, 6, 9, 2, 4, 4]
abilities_top:
  - name: "Clean Vulnerability"
    desc: "Omoxes embody filth, and they find the concept of cleanliness abhorrent. An omox slime pool subjected to an effect that cleans them takes 4d6 mental damage. They also take this damage the first time each round a creature damaged by an omox slime pool spends actions cleaning off the resultant filth."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +29; __Will__: +26 +1 status to all saves vs. magic"
hp: 315
health:
  - name: "HP"
    desc: "315 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], critical hits, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision; __Weaknesses__ area damage 15, [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 15"
abilities_mid:
  - name: "Absorb Weapon"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]])"
  - name: "Trigger"
    desc: "A creature hits the omox slime pool with a melee weapon"
  - name: "Effect"
    desc: "The omoxes attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]] the creature. On a critical success, the weapon becomes subsumed within the body of an omox rather than falling to the ground. Retrieving the weapon requires a successful DC 45 [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to Disarm."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet, climb 20 feet, swim 80 feet; troop movement"
abilities_bot:
  - name: "Slime Barrage"
    desc: "⬺ The omoxes hurl balls of heavy slime in a 10- foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 30 feet. All creatures in the area take 4d6 bludgeoning damage and 2d6 acid damage (DC 35 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature that fails the save is mired in the slime, taking a –10-foot circumstance penalty to its Speeds for 1 minute or until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 38); on a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 for the same duration. When the slime pool is reduced to 2 segments, the area decreases to a 5-foot burst."
  - name: "Smothering Grasp"
    desc: "⬻"
  - name: "Requirements"
    desc: "The omox slime pool has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "Omox slime flows onto the creature, completely covering it. The creature must then succeed at a DC 38 Fortitude save or it becomes [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] and must hold its breath or begin [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Drowning and Suffocating|suffocating]]. These effects last as long as the omoxes have the creature grabbed or restrained."
  - name: "Waves of Sludge"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The omoxes attack all enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] with slimy tendrils (DC 35 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature that critically fails this saving throw is also [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the slime pool. The damage depends on the number of actions. ⬻ 1d6+3 bludgeoning damage plus 1d6 acid damage ⬺ 3d6+12 bludgeoning damage plus 2d6 acid damage ⬽ 4d6+14 bludgeoning damage plus 3d6 acid damage"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]], [[srd/pf2e/compendium/spells/rank-1/create-water|Create Water]] (at will), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]]"
  - name: "Rituals"
    desc: "DC 38 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Battlecry!_, page 186."
```

```encounter-table
name: Omox Slime Pool
creatures:
  - 1: Omox Slime Pool
```
