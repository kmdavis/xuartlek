---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Centipede Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Centipede Swarm"
level: 3
source: "Monster Core"
aon_id: "creature-2876"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2876"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Centipede Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [2, 4, 3, -5, 0, -4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +11; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], swarm mind; __Resistances__ bludgeoning 5, piercing 5, slashing 2; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "30 feet, climb 30 feet"
abilities_bot:
  - name: "Centipede Swarm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 2"
    desc: "1d8 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], and off-guard (1 round)"
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 1d8 piercing damage (DC 20 basic Reflex save) plus centipede swarm venom."
sourcebook: "_Monster Core_, page 59."
```

```encounter-table
name: Centipede Swarm
creatures:
  - 1: Centipede Swarm
```
