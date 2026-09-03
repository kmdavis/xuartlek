---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vegetable Lamb"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/small
statblock: inline
name: "Vegetable Lamb"
level: 1
source: "Rage of Elements"
aon_id: "creature-2669"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2669"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Vegetable Lamb"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
skills:
  - name: "Skills"
    desc: "Athletics +5, Nature +6"
abilityMods: [3, 1, 2, -4, 0, 3]
abilities_top:
  - name: "Nature's Bounty"
    desc: "(healing, plant, primal, vitality) Each day, a vegetable lamb grows 1d4 edible flowers (such as artichoke, broccoli, or dandelion) among the green cotton covering its body. These vegetables can be picked without hurting the lamb. A living creature can eat the vegetable with an Interact action to regain 1d6+4 Hit Points."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +6; __Ref__: +3; __Will__: +8"
hp: 28
health:
  - name: "HP"
    desc: "28; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ fire 3, slashing 2"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ headbutt +8 __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ hoof +6 __Damage__ 1d6 bludgeoning"
abilities_bot:
  - name: "Cottonseed Burst"
    desc: "⬺ The vegetable lamb releases a cloud of cottony green pollen in a 10-foot burst centered on itself. All creatures caught in the burst that need to breathe, apart from the lamb, must succeed at a DC 15 Fortitude save or be slowed 1 by coughing (slowed 2 on a critical failure)."
sourcebook: "_Rage of Elements_, page 204."
```

```encounter-table
name: Vegetable Lamb
creatures:
  - 1: Vegetable Lamb
```
