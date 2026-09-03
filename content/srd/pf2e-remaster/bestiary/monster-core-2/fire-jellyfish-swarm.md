---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fire Jellyfish Swarm"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Fire Jellyfish Swarm"
level: 6
source: "Monster Core 2"
aon_id: "creature-4448"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4448"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fire Jellyfish Swarm"
level: "Creature 6"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Mindless"
trait_04: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +15"
abilityMods: [-4, 5, 4, -5, 0, -5]
abilities_top:
  - name: "Agile Swimmer"
    desc: "Fire jellyfish swarms use Acrobatics to Swim."
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +16; __Ref__: +15; __Will__: +10"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ critical hits, mental, precision, swarm mind; __Resistances__ bludgeoning 9, piercing 9, poison 10, slashing 5; __Weaknesses__ area damage 7, splash damage 7"
speed: "swim 20 feet"
abilities_bot:
  - name: "Burning Swarm"
    desc: "⬻ (Poison) Each enemy in the swarm's space takes 3d8 poison damage (DC 24 basic Reflex save) and is exposed to fire jelly venom."
  - name: "Fire Jelly Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "clumsy 3 (1 round)"
sourcebook: "_Monster Core 2_, page 200."
```

```encounter-table
name: Fire Jellyfish Swarm
creatures:
  - 1: Fire Jellyfish Swarm
```
