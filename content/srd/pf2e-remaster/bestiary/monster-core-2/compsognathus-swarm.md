---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Compsognathus Swarm"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Compsognathus Swarm"
level: 3
source: "Monster Core 2"
aon_id: "creature-4333"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4333"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Compsognathus Swarm"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: "Swarm"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +9, Stealth +10"
abilityMods: [2, 4, 2, 0, 1, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +8; __Ref__: +12; __Will__: +7"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ grabbed, precision, prone, restrained, swarm mind; __Resistances__ bludgeoning 2, piercing 5, slashing 5; __Weaknesses__ area damage 5, splash damage 5"
abilities_mid:
  - name: "Evade"
    desc: "⬲"
  - name: "Trigger"
    desc: "An adjacent enemy targets the swarm with a Strike"
  - name: "Effect"
    desc: "With quick movements, the swarm gains a +1 circumstance bonus to AC against the triggering attack. If the attack misses, the swarm can Stride up to 10 feet after the Strike."
speed: "30 feet, swim 15 feet"
abilities_bot:
  - name: "Venomous Bites"
    desc: "⬻ Each enemy in the swarm's space takes 2d4 piercing damage (DC 20 basic Reflex save). A creature who fails the save is also exposed to compsognathus venom."
  - name: "Compsognathus Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d8 poison damage and enfeebled 1 (1 round) Dinosaur Swarms Because they all depend on laying eggs to reproduce, dinosaurs generally have nesting areas of which they're fiercely protective. While larger dinosaurs like allosauruses are slightly more prepared to take on a threat alone, smaller species often rely on safety in numbers to protect their homes. Once a threat is posed to their eggs, these diminutive creatures seem to form a cloud of frenzied jaws and claws, all moving together as if sharing one mind."
sourcebook: "_Monster Core 2_, page 106."
```

```encounter-table
name: Compsognathus Swarm
creatures:
  - 1: Compsognathus Swarm
```
