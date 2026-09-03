---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skymetal Striker"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/large
statblock: inline
name: "Skymetal Striker"
level: 7
source: "Rage of Elements"
aon_id: "creature-2650"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2650"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Skymetal Striker"
level: "Creature 7"
size: "Large"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Talican"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Stealth +17"
abilityMods: [2, 6, 4, 2, 2, 2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +15; __Ref__: +17; __Will__: +13"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ inubrix fangs +17 (Finesse, reach 10 feet) __Damage__ 2d10+6 slashing plus phase blade"
  - name: "Melee"
    desc: "⬻ orichalcum fangs +17 (Finesse, reach 10 feet) __Damage__ 2d12+6 slashing plus temporal stutter"
abilities_bot:
  - name: "Phase Blade"
    desc: "A skymetal striker's inubrix fangs Strike ignores damage resistance from metal armor's armor specialization effects and the circumstance bonus to AC from metal shields, and it doesn't trigger the Shield Block reaction from a metal shield."
  - name: "Temporal Stutter"
    desc: "A creature not already affected by temporal stutter that takes damage from a skymetal striker's orichalcum fangs Strike must attempt a DC 25 Fortitude save."
  - name: "Success"
    desc: "The target is quickened until the end of its next turn."
  - name: "Failure"
    desc: "The target is slowed 1 until the end of its next turn."
  - name: "Critical Failure"
    desc: "The target is slowed 2 until the end of its next turn."
  - name: "Two-Headed Assault"
    desc: "⬺ The skymetal striker makes one inubrix fangs Strike and one orichalcum fangs Strike, each against a different creature. Its multiple attack penalty increases only after all the attacks are made. Strange Metals Inubrix and orichalcum are types of skymetal—a collective term used in the Universe to refer to exceedingly rare metals, most possessing magical properties, found on distant planets and fallen stars. Skymetal can be found in abundance on the Plane of Metal, however, and many metal elementals contain at least a bit of one type or another. Inubrix, colloquially called ghost iron, is prized for its ability to phase through other metals, while orichalcum's mystical properties can warp the very flow of time around it."
sourcebook: "_Rage of Elements_, page 156."
```

```encounter-table
name: Skymetal Striker
creatures:
  - 1: Skymetal Striker
```
