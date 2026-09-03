---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brood Leech Swarm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Brood Leech Swarm"
level: 4
source: "Monster Core 2"
aon_id: "creature-4462"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4462"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Brood Leech Swarm"
level: "Creature 4"
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: "Swarm"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; tremorsense 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [0, 3, 4, -5, 1, -5]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +12; __Ref__: +11; __Will__: +9"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, salt 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "5 feet, swim 20 feet"
abilities_bot:
  - name: "Blood-Draining Bites"
    desc: "⬻ Each enemy in the swarm's space takes 2d6 piercing damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature who fails the Reflex save also takes 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] and is exposed to brood leech swarm venom."
  - name: "Brood Leech Swarm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1, [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1, and –5-foot status penalty to Speed (1 round)"
  - name: "Stage 2"
    desc: "clumsy 1, sickened 1, and –10-foot status penalty to Speed (1 round)"
sourcebook: "_Monster Core 2_, page 212."
```

```encounter-table
name: Brood Leech Swarm
creatures:
  - 1: Brood Leech Swarm
```
