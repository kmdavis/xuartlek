---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cockroach Swarm"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Cockroach Swarm"
level: 2
source: "Monster Core 2"
aon_id: "creature-4301"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4301"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Cockroach Swarm"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [2, 4, 3, -5, 0, -4]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +10; __Will__: +6"
hp: 26
health:
  - name: "HP"
    desc: "26; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
speed: "20 feet, climb 20 feet, fly 15 feet"
abilities_bot:
  - name: "Swarming Bites"
    desc: "⬻ Each enemy in the swarm's space takes 1d8 piercing damage (DC 18 basic Reflex save)."
sourcebook: "_Monster Core 2_, page 76."
```

```encounter-table
name: Cockroach Swarm
creatures:
  - 1: Cockroach Swarm
```
