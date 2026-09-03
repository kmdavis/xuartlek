---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vampire Bat Swarm"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Vampire Bat Swarm"
level: 1
source: "Monster Core"
aon_id: "creature-2848"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2848"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vampire Bat Swarm"
level: "Creature 1"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; echolocation (precise) 20 feet, low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +4, Stealth +7"
abilityMods: [1, 4, 1, -4, 3, -3]
abilities_top:
  - name: "Echolocation"
    desc: "A bat swarm can use its hearing as a precise sense at the listed range."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +9; __Will__: +6"
hp: 11
health:
  - name: "HP"
    desc: "11; __Immunities__ grabbed, precision, prone, restrained, swarm mind; __Resistances__ bludgeoning 6, piercing 6, slashing 3; __Weaknesses__ area damage 3, splash damage 3"
speed: "5 feet, fly 30 feet"
abilities_bot:
  - name: "Blood Feast"
    desc: "⬻ Each enemy in the bat swarm's space takes 1d4 piercing damage (DC 16 basic Reflex save). Creatures that fail this save also take 1 persistent bleed damage."
sourcebook: "_Monster Core_, page 40."
```

```encounter-table
name: Vampire Bat Swarm
creatures:
  - 1: Vampire Bat Swarm
```
