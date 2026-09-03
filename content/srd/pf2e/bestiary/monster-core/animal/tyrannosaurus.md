---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tyrannosaurus"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tyrannosaurus"
level: 10
source: "Monster Core"
aon_id: "creature-2923"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2923"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tyrannosaurus"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +24"
abilityMods: [8, 1, 5, -4, 3, 0]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +15; __Will__: +19"
hp: 180
health:
  - name: "HP"
    desc: "180"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ; jaws +22 (deadly d12, reach 20 feet) __Damage__ 2d12+12 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ foot +22 (reach 15 feet) __Damage__ 2d10+12 bludgeoning"
abilities_bot:
  - name: "Fling"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is grabbed in the tyrannosaurus's jaws"
  - name: "Effect"
    desc: "The tyrannosaurus flings the creature into the air up to 10 feet up from its mouth and 20 feet away. The creature falls 25 feet (assuming the tyrannosaurus flings it as high as it can) and takes falling damage accordingly. If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage. The creature being landed on can attempt a DC 23 basic Reflex save."
  - name: "Pin Prey"
    desc: "⬲"
  - name: "Trigger"
    desc: "The tyrannosaurus critically hits a Large or smaller foe with its foot"
  - name: "Effect"
    desc: "The creature struck by the foot is knocked prone and held in place. As long as the tyrannosaurus doesn't move from its position, the pinned creature is grabbed. A tyrannosaurus gains a +2 circumstance bonus to attack a creature it has pinned in this manner but can only Swallow Whole if that creature is grabbed with its jaws."
  - name: "Swallow Whole"
    desc: "⬻ (attack) Medium, 3d6+8 bludgeoning, Rupture 26"
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 29"
sourcebook: "_Monster Core_, page 101."
```

```encounter-table
name: Tyrannosaurus
creatures:
  - 1: Tyrannosaurus
```
