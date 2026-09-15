---
noteType: pf2eMonster
aliases: "Gargoyle Wing"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Gargoyle Wing"
level: 9
source: "Battlecry!"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3917"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Gargoyle Wing"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Earth"
trait_03: "Troop"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +20, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +18"
abilityMods: [4, 3, 4, -2, 3, -2]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +20; __Ref__: +17; __Will__: +17"
hp: 150
health:
  - name: "HP"
    desc: "150 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]]; __Resistances__ physical 10 (except [[srd/pf2e/compendium/equipment/materials/Adamantine|adamantine]]); __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage 10"
abilities_mid:
  - name: "Death From Above"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|attack]])"
  - name: "Trigger"
    desc: "The gargoyle wing is Flying, and a creature moves into an adjacent square below it"
  - name: "Effect"
    desc: "The gargoyle wing swoops down with their talons. The triggering creature takes 2d8+9 slashing damage (DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, fly 40 feet; troop movement"
abilities_bot:
  - name: "Catch and Release"
    desc: "⬺ The gargoyle wing attempts an [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]], comparing the result to the Fortitude DC of a number of Large or smaller creatures in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] equal to the gargoyle wing's remaining number of segments, then Flies up to 40 feet, bringing any successfully [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] creatures along, and Releases them."
  - name: "Raking Swoop"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The gargoyle wing rips and tears with their stony talons at each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] (DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The damage dealt depends on the number of actions. ⬻ 1d8+2 slashing damage ⬺ 2d8+9 slashing damage ⬽ 3d8+11 slashing damage"
sourcebook: "_Battlecry!_, page 181."
```

```encounter-table
name: Gargoyle Wing
creatures:
  - 1: Gargoyle Wing
```
