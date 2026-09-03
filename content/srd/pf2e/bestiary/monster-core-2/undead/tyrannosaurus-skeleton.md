---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tyrannosaurus Skeleton"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tyrannosaurus Skeleton"
level: 9
source: "Monster Core 2"
aon_id: "creature-4548"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4548"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tyrannosaurus Skeleton"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +19"
abilityMods: [7, 0, 5, -5, 2, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +13; __Will__: +17"
hp: 140
health:
  - name: "HP"
    desc: "140 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 10, electricity 10, fire 10, piercing 10, slashing 10"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (deadly d12, reach 20 feet) __Damage__ 2d12+9 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ foot +20 (reach 15 feet) __Damage__ 2d10+9 bludgeoning"
abilities_bot:
  - name: "Rib Skewer"
    desc: "⬻ The tyrannosaurus skeleton bends down, attempting to skewer one adjacent creature on one of its massive ribs. The creature takes 2d10+9 piercing damage (DC 28 basic Reflex save). If the creature fails its save and is Medium or smaller, it's also impaled and stuck to the rib. It is immobilized but moves with the skeleton and takes 2d6 persistent bleed damage until it either Escapes or someone uses Force Open to break the rib (either is DC 28)."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 28"
sourcebook: "_Monster Core 2_, page 290."
```

```encounter-table
name: Tyrannosaurus Skeleton
creatures:
  - 1: Tyrannosaurus Skeleton
```
