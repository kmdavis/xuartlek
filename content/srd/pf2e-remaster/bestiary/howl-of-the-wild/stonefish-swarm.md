---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stonefish Swarm"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Stonefish Swarm"
level: 2
source: "Howl of the Wild"
aon_id: "creature-3275"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3275"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Stonefish Swarm"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Swarm"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +6, Stealth +11"
abilityMods: [2, 3, 2, -5, 1, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +11; __Ref__: +8; __Will__: +5"
hp: 25
health:
  - name: "HP"
    desc: "25; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 3, slashing 3; __Weaknesses__ area damage 3, splash damage 3"
abilities_mid:
  - name: "Defensive Spines"
    desc: "When a creature enters the stonefish swarm's space, that creature takes 1d4 piercing damage and is exposed to stonefish swarm venom."
speed: "swim 25 feet"
abilities_bot:
  - name: "Inject Poison"
    desc: "⬻ Each enemy in the swarm's space takes 2d4 piercing damage (DC 18 basic Reflex save). Creatures that fail the save are exposed to stonefish swarm venom."
  - name: "Reef Camouflage"
    desc: "⬻ (Concentrate) Until the next time it acts, the stonefish swarm appears to be a colorful coral reef. It has an automatic result of 26 on Deception checks and DCs to pass as a reef."
  - name: "Stonefish Swarm Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage and clumsy 2 (1 round)"
sourcebook: "_Howl of the Wild_, page 148."
```

```encounter-table
name: Stonefish Swarm
creatures:
  - 1: Stonefish Swarm
```
