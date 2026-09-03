---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spinosaurus"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Spinosaurus"
level: 11
source: "Monster Core 2"
aon_id: "creature-4337"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4337"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Spinosaurus"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Athletics +22"
abilityMods: [8, 4, 6, -4, 2, 1]
abilities_top:
  - name: "Deep Breath"
    desc: "A spinosaurus can hold its breath for 2 hours."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +21; __Will__: +19"
hp: 200
health:
  - name: "HP"
    desc: "200"
speed: "40 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 (deadly d12, reach 20 feet) __Damage__ 2d12+14 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +23 (Agile, reach 15 feet) __Damage__ 2d8+14 slashing"
abilities_bot:
  - name: "Rip and Tear"
    desc: "⬻"
  - name: "Requirements"
    desc: "The spinosaurus has a creature grabbed or restrained in its jaws"
  - name: "Effect"
    desc: "The spinosaurus reaches up and slashes with its claws at the creature it has grabbed, dealing 4d8 slashing damage (DC 30 basic Reflex save). A creature who fails this save also takes 1d6 persistent bleed damage."
  - name: "Staggering Sail"
    desc: "⬺ (incapacitation"
  - name: "Requirements"
    desc: "The spinosaurus is swimming on the surface of water)"
  - name: "Effect"
    desc: "With a powerful lunge to the side, the spinosaurus uses its sail to slap the surface of the water, creating a crushing wave of water that deals 6d6 bludgeoning damage in a 30-foot cone. Each creature in the water in the area must attempt a DC 30 Reflex save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is slowed 1 until the end of its next turn."
  - name: "Critical Failure"
    desc: "The creature takes double damage and is stunned 2."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Medium, 2d12+6 bludgeoning, Rupture 19"
sourcebook: "_Monster Core 2_, page 108."
```

```encounter-table
name: Spinosaurus
creatures:
  - 1: Spinosaurus
```
