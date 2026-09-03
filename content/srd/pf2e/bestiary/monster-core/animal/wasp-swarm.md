---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wasp Swarm"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Wasp Swarm"
level: 4
source: "Monster Core"
aon_id: "creature-3234"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3234"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wasp Swarm"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12"
abilityMods: [-4, 4, 2, -5, 2, -1]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +10; __Ref__: +12; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ bludgeoning 7, piercing 7, slashing 3; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "20 feet, fly 40 feet"
abilities_bot:
  - name: "Swarming Stings"
    desc: "⬻ Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 basic Reflex save). A creature that fails its save is also exposed to wasp venom."
  - name: "Wasp Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 (2 rounds)"
sourcebook: "_Monster Core_, page 343."
```

```encounter-table
name: Wasp Swarm
creatures:
  - 1: Wasp Swarm
```
