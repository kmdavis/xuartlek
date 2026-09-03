---
obsidianUIMode: preview
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
aon_id: "creature-4405"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4405"
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
    desc: "Perception +20; darkvision"
languages: "Common, Empyrean, Vudrani; plus two others; speaker of the skies"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +21, Diplomacy +19, Intimidation +17, Religion +19"
abilityMods: [6, 4, 4, 2, 4, 4]
abilities_top:
  - name: "Speaker of the Skies"
    desc: "A garuda can speak with any type of bird."
  - name: "Vehicle of the Gods"
    desc: "Garudas were created to serve as transport for other beings. A holy creature can ride the garuda by using the Mount action to move onto them. Unlike the normal rules for riding other creatures, both the garuda and the rider continue to receive all 3 of their actions each turn, and the garuda's rider can be Medium or smaller. A ga ruda can have only a single rider at a time. The garuda can choose to allow a non-holy (but not an unholy) creature to ride them, but generally only does so in specific circumstances."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +19; __Will__: +16"
hp: 160
health:
  - name: "HP"
    desc: "160; __Resistances__ 10; __Weaknesses__ unholy 10"
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +21 (Holy, magical) __Damage__ 2d10+9 piercing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ talon +21 (Agile, finesse, holy, magical) __Damage__ 2d8+9 bludgeoning plus 1d6 fire and Grab"
  - name: "Ranged"
    desc: "⬻ sun beam +19 (Fire, magical, holy, range 100 feet) __Damage__ 2d10 fire plus 2d6 spirit"
abilities_bot:
  - name: "Celestial Meteor"
    desc: "⬽ (Divine, fire, move)"
  - name: "Requirements"
    desc: "The garuda doesn't have a rider"
  - name: "Effect"
    desc: "The garuda Flies straight up and then comes crashing down toward the ground, landing in an unoccupied space within 30 feet. As the garuda lands, a burst of solar flames erupts from them, dealing 5d6 fire damage to all creatures in a 10-foot emanation (DC 28 basic Reflex save). If the garuda lands adjacent to a creature, they can attempt to Grapple that creature. On a success or critical success, the garuda can then Fly up to 30 feet with the creature."
  - name: "Divine Grasp"
    desc: "When a garuda moves, they can bring grabbed creatures along with them."
  - name: "Raise by the Sun"
    desc: ""
  - name: "Requirements"
    desc: "The garuda doesn't have a rider"
  - name: "Effect"
    desc: "The garuda Flies and picks up a willing creature at any point during the flight, who then begins riding the garuda, and then the garuda continues their Fly action. If the garuda uses three actions, they can instead Fly twice. At any point during the garuda's movement, the rider can use a reaction to attempt a Strike with a ranged weapon. Sun-Borne Servants According to the old tales, the first garudas were born from celestial eggs kept warm within the heart of the sun. These eggs incubated for hundreds of years. Most of the eggs hatched at different times, revealing a number of different celestial creatures, but the last clutch of eggs remained, waiting patiently until ordered to open. Once one hundred and eight lifetimes passed, the gods returned to the sun and bid the garudas be born. Seeing as they were obedient even before their birth, the gods made garudas their blessed servants."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +18 - __3rd__ Haste - __4th__ Blazing Bolt, Holy Light, Translocate"
sourcebook: "_Monster Core 2_, page 159."
```

```encounter-table
name: Garuda
creatures:
  - 1: Garuda
```
