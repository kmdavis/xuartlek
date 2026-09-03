---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Platecarpus"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Platecarpus"
level: 3
source: "Monster Core 2"
aon_id: "creature-4479"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4479"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Platecarpus"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +9, Stealth +11"
abilityMods: [5, 4, 3, -4, 2, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "A platecarpus can hold its breath for 2 hours."
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +11; __Will__: +7"
hp: 46
health:
  - name: "HP"
    desc: "46"
speed: "5 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 __Damage__ 1d12+5 piercing plus Grab"
abilities_bot:
  - name: "Aquatic Drag"
    desc: "⬻"
  - name: "Requirements"
    desc: "The platecarpus has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The platecarpus Swims up to half its Speed, carrying the grabbed or restrained creature with it."
  - name: "Strafing Chomp"
    desc: "⬻ The platecarpus Swims up to its Speed, making one jaws Strike at any point along the way. The Strike deals half damage."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Medium, 1d6+2 bludgeoning, Rupture 10"
sourcebook: "_Monster Core 2_, page 227."
```

```encounter-table
name: Platecarpus
creatures:
  - 1: Platecarpus
```
