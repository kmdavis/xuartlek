---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Raven Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Raven Swarm"
level: 3
source: "Monster Core 2"
aon_id: "creature-4528"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4528"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Raven Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +10"
abilityMods: [0, 3, 0, -4, 4, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +12; __Will__: +9"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "10 feet, fly 40 feet"
abilities_bot:
  - name: "Enraged Cunning"
    desc: "There are few things as dangerously persistent in the natural world as an angry unkindness of ravens. A raven swarm can hound its prey through most barriers. Simple latches, unsecured chimney flues, loosely shuttered windows, and similar obstacles rarely keep an unkindness away. A raven swarm attempts a [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to bypass many of these simple obstructions, typically against DC 20."
  - name: "Swarming Beaks"
    desc: "⬻ The ravens' angry pecking deals 2d8 piercing damage to each enemy in the swarm's space (DC 20 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature that critically fails its save is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1d4 rounds as the ravens focus their attacks on the target's vulnerable face."
sourcebook: "_Monster Core 2_, page 267."
```

```encounter-table
name: Raven Swarm
creatures:
  - 1: Raven Swarm
```
