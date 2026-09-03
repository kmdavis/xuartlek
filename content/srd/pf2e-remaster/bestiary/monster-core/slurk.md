---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Slurk"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Slurk"
level: 2
source: "Monster Core"
aon_id: "creature-3199"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3199"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Slurk"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +8, Stealth +5"
abilityMods: [4, 2, 4, -4, 0, 0]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10 (+12 vs. Grapple); __Ref__: +6; __Will__: +4"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusks +11 (deadly d10) __Damage__ 1d8+4 piercing"
  - name: "Ranged"
    desc: "⬻ slime squirt +9 (range increment 30 feet) __Damage__ entangling slime"
abilities_bot:
  - name: "Belly Grease"
    desc: "⬽ The slurk extrudes a slippery grease from its ventral glands to coat the floor under it and in a 5-foot emanation, turning the affected area into uneven ground for 10 minutes, after which it dries to a putrid crust. The DC to Balance across the slime is 18."
  - name: "Entangling Slime"
    desc: "A creature struck by a slurk's slime squirt becomes clumsy 1 and takes a –5-foot penalty to Speed for 1 hour or until the slime is removed. The slime can be removed with a total of three Interact actions by the entangled creature or creatures adjacent to the creature. These actions don't need to be consecutive or made by the same creature. Slurk Riding As long as a slurk is willing or broken, a creature at least one size smaller than the slurk can use it as a mount. A slurk's back slime grants its rider a +2 circumstance bonus against any attempts to physically dismount the rider."
sourcebook: "_Monster Core_, page 315."
```

```encounter-table
name: Slurk
creatures:
  - 1: Slurk
```
