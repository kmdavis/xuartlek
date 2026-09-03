---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Viking Guard"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Viking Guard"
level: 11
source: "Battlecry!"
aon_id: "creature-3940"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3940"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Viking Guard"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Skald|Skald]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +21"
abilityMods: [7, 3, 5, 1, 1, 1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +21; __Will__: +18 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]"
hp: 195
health:
  - name: "HP"
    desc: "195 (4 segments); __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Sacrifice"
    desc: "⬲"
  - name: "Requirements"
    desc: "The viking guard has a charge, and that creature is adjacent to the viking guard"
  - name: "Trigger"
    desc: "The viking guard's charge takes Hit Point damage"
  - name: "Effect"
    desc: "The viking guard's charge takes half damage, and the viking guard takes the remainder of the damage."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, troop movement"
abilities_bot:
  - name: "Berserker Strikes"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "Battle axes in hand, the viking guard engages in a coordinated melee attack against enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], with a DC 27 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 1d8+3 slashing damage ⬺ 2d8+12 slashing damage ⬽ 3d8+15 slashing damage"
  - name: "Guard Charge"
    desc: "⬻ The viking guard designates an ally it can see to be its charge. The charge gains a +2 circumstance bonus to their AC, Reflex saves, and saves against [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]] when they are adjacent to the viking guard. Further, this allows the viking guard to use its Sacrifice and Shield Wall actions. A viking guard can have only one charge at a time, and if it designates a new charge, the old one loses all benefits. If the viking guard's charge is reduced to 0 Hit Points, the viking guard must succeed at a DC 30 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 2; this is an [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], fear, and [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] effect."
  - name: "Shield Wall"
    desc: "⬺"
  - name: "Requirements"
    desc: "The viking guard has a charge, and that creature is adjacent to the viking guard"
  - name: "Effect"
    desc: "Raising shields, the viking guard Strides up to twice its Speed as it protects its charge. The viking guard gains a +2 circumstance bonus to its AC against reactions triggered by this movement. The viking guard's charge can Stride the same distance as a reaction, moving with the troop to maintain the bonuses from Guard Charge during this movement."
sourcebook: "_Battlecry!_, page 193."
```

```encounter-table
name: Viking Guard
creatures:
  - 1: Viking Guard
```
