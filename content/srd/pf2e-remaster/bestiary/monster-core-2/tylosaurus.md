---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tylosaurus"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tylosaurus"
level: 8
source: "Monster Core 2"
aon_id: "creature-4480"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4480"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tylosaurus"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +16, Stealth +19"
abilityMods: [7, 5, 5, -4, 4, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "A tylosaurus can hold its breath for 2 hours."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +19; __Will__: +14"
hp: 137
health:
  - name: "HP"
    desc: "137"
speed: "5 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 __Damage__ 2d12+10 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +18 __Damage__ 2d6+10 bludgeoning"
abilities_bot:
  - name: "Aquatic Drag"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tylosaurus has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The platecarpus Swims up to half its Speed, carrying the grabbed or restrained creature with it."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Large, 2d6+5 bludgeoning, Rupture 18"
  - name: "Vicious Strafe"
    desc: "⬺ The tylosaurus Swims up to its Speed. It can make one jaws Strike and one tail Strike at any point during its movement, each attacking a different target."
sourcebook: "_Monster Core 2_, page 227."
```

```encounter-table
name: Tylosaurus
creatures:
  - 1: Tylosaurus
```
