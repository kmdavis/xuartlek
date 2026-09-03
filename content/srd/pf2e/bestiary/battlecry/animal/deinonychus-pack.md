---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deinonychus Pack"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Deinonychus Pack"
level: 7
source: "Battlecry!"
aon_id: "creature-3909"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3909"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Deinonychus Pack"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: "Troop"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [4, 4, 6, -4, 2, 3]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +15; __Will__: +12"
hp: 120
health:
  - name: "HP"
    desc: "120 (4 segments); __Weaknesses__ area damage 6, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 6"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; troop movement"
abilities_bot:
  - name: "Jaws and Claws"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The pack makes a melee attack against each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 22 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. ⬻ 1d6 slashing or piercing damage plus 1d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] ⬺ 2d6+4 slashing or piercing damage plus 2d4 persistent bleed damage ⬽ 3d6+6 slashing or piercing damage plus 2d4 persistent bleed damage"
  - name: "Predator's Advantage"
    desc: "Bleeding creatures take a –2 circumstance penalty to Reflex saves against a deinonychus pack's Jaws and Claws."
  - name: "Surround Prey"
    desc: "⬺"
  - name: "Requirements"
    desc: "The deinonychus pack has at least 3 segments"
  - name: "Effect"
    desc: "The pack Strides, positioning its segments so that at least two of them are adjacent to the same creature, and lashes out with its talons. That creature must succeed at a DC 22 Reflex save or take 2d4 persistent bleed damage"
sourcebook: "_Battlecry!_, page 175."
```

```encounter-table
name: Deinonychus Pack
creatures:
  - 1: Deinonychus Pack
```
