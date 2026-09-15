---
noteType: pf2eMonster
aliases: "Garuda"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Garuda"
level: 9
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4405"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Garuda"
level: "Creature 9"
size: "Medium"
trait_01: "Celestial"
trait_02: "Holy"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Vudrani|Vudrani]]; plus two others; speaker of the skies"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +19"
abilityMods: [6, 4, 4, 2, 4, 4]
abilities_top:
  - name: "Speaker of the Skies"
    desc: "A garuda can speak with any type of bird."
  - name: "Vehicle of the Gods"
    desc: "Garudas were created to serve as transport for other beings. A [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] creature can ride the garuda by using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Mount|Mount]] action to move onto them. Unlike the normal rules for riding other creatures, both the garuda and the rider continue to receive all 3 of their actions each turn, and the garuda's rider can be Medium or smaller. A ga ruda can have only a single rider at a time. The garuda can choose to allow a non-holy (but not an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) creature to ride them, but generally only does so in specific circumstances."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +19; __Will__: +16"
hp: 160
health:
  - name: "HP"
    desc: "160; __Resistances__ 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 10"
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d10+9 piercing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ talon +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d8+9 bludgeoning plus 1d6 fire and Grab"
  - name: "Ranged"
    desc: "⬻ sun beam +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]], range 100 feet) __Damage__ 2d10 fire plus 2d6 spirit"
abilities_bot:
  - name: "Celestial Meteor"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Move|move]])"
  - name: "Requirements"
    desc: "The garuda doesn't have a rider"
  - name: "Effect"
    desc: "The garuda [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] straight up and then comes crashing down toward the ground, landing in an unoccupied space within 30 feet. As the garuda lands, a burst of solar flames erupts from them, dealing 5d6 fire damage to all creatures in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] (DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). If the garuda lands adjacent to a creature, they can attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] that creature. On a success or critical success, the garuda can then Fly up to 30 feet with the creature."
  - name: "Divine Grasp"
    desc: "When a garuda moves, they can bring [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] creatures along with them."
  - name: "Raise by the Sun"
    desc: ""
  - name: "Requirements"
    desc: "The garuda doesn't have a rider"
  - name: "Effect"
    desc: "The garuda [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] and picks up a willing creature at any point during the flight, who then begins riding the garuda, and then the garuda continues their Fly action. If the garuda uses three actions, they can instead Fly twice. At any point during the garuda's movement, the rider can use a reaction to attempt a Strike with a ranged weapon. Sun-Borne Servants According to the old tales, the first garudas were born from celestial eggs kept warm within the heart of the sun. These eggs incubated for hundreds of years. Most of the eggs hatched at different times, revealing a number of different celestial creatures, but the last clutch of eggs remained, waiting patiently until ordered to open. Once one hundred and eight lifetimes passed, the gods returned to the sun and bid the garudas be born. Seeing as they were obedient even before their birth, the gods made garudas their blessed servants."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +18 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Blazing Bolt|Blazing Bolt]], [[srd/pf2e/compendium/spells/rank-3/Holy Light|Holy Light]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]]"
sourcebook: "_Monster Core 2_, page 159."
```

```encounter-table
name: Garuda
creatures:
  - 1: Garuda
```
