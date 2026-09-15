---
noteType: pf2eMonster
aliases: "Mitflit Vermin Cavalry"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Mitflit Vermin Cavalry"
level: 4
source: "Battlecry!"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3927"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Mitflit Vermin Cavalry"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Fey"
trait_03: "Gremlin"
trait_04: "Troop"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +12"
abilityMods: [0, 5, 1, -1, 2, -1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +14; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60 (4 segments); __Weaknesses__ area damage 5, [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 4, splash damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "15 feet, climb 15 feet; troop movement"
abilities_bot:
  - name: "Crawling Stabs"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The mitflits thrust with their shortswords, coordinated with bites from their giant vermin mounts. All enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] must attempt a DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 1d6 piercing damage ⬺ 2d6+4 piercing damage ⬽ 2d6+8 piercing damage"
  - name: "Leaping Charge"
    desc: "⬺ The mitflit vermin cavalry Leaps up to 30 feet. If it moves at least 15 feet, the cavalry deals 2d6+4 piercing damage (DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save) to each enemy within a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] at the end of its movement."
  - name: "Mounted Troop"
    desc: "Effects that target only animals or only humanoids may not work on the mitflit vermin cavalry, subject to the GM's discretion."
  - name: "Vengeful Wrath"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) As long as it's not [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]], the mitflit vermin cavalry gains a +2 status bonus to the DC of its Crawling Stabs ability against creatures that have previously damaged or tormented it."
sourcebook: "_Battlecry!_, page 185."
```

```encounter-table
name: Mitflit Vermin Cavalry
creatures:
  - 1: Mitflit Vermin Cavalry
```
