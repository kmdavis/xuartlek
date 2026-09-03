---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rat Snake Swarm"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Rat Snake Swarm"
level: 2
source: "Monster Core 2"
aon_id: "creature-4554"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4554"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Rat Snake Swarm"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Stealth +8"
abilityMods: [0, 4, 2, -4, 2, -3]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +10; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 3, piercing 5, slashing 5; __Weaknesses__ area damage 3, splash damage 3"
abilities_mid:
  - name: "Mass Wriggle"
    desc: "⬲"
  - name: "Trigger"
    desc: "The rat snake swarm takes damage from a melee Strike"
  - name: "Effect"
    desc: "Snakes slither up and around the creature's weapon and limbs. The target must succeed at a DC 15 Will save or become frightened 1."
speed: "20 feet, climb 20 feet, swim 20 feet"
abilities_bot:
  - name: "Swarming Strikes"
    desc: "⬻ Each enemy in the swarm's space takes 1d8 piercing damage (DC 17 basic Reflex save). Slithering Packs Despite their solitary natures, snakes come together in swarms for purposes of hibernation or mating. However, a few species have learned to stick together and coordinate their hunting efforts, leading to slithering packs of predatory snakes."
sourcebook: "_Monster Core 2_, page 294."
```

```encounter-table
name: Rat Snake Swarm
creatures:
  - 1: Rat Snake Swarm
```
