---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Jellyfish"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Jellyfish"
level: 7
source: "Monster Core 2"
aon_id: "creature-4449"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4449"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Jellyfish"
level: "Creature 7"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Mindless"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +17, Stealth +15"
abilityMods: [6, 4, 6, -5, 0, -5]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +17; __Ref__: +15; __Will__: +1"
hp: 165
health:
  - name: "HP"
    desc: "165; __Immunities__ critical hits, mental, precision; __Resistances__ bludgeoning 5, poison 10; __Weaknesses__ piercing 5, slashing 5"
speed: "swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +18 (Agile, reach 20 feet) __Damage__ 2d8+8 bludgeoning plus jellyfish venom"
abilities_bot:
  - name: "Jellyfish Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d8 poison damage and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "2d10 poison damage and paralyzed (1 round)"
  - name: "Squeeze"
    desc: "A giant jellyfish can fit into tight spaces as if it were a Medium creature. It can move at its full Speed while Squeezing."
sourcebook: "_Monster Core 2_, page 200."
```

```encounter-table
name: Giant Jellyfish
creatures:
  - 1: Giant Jellyfish
```
