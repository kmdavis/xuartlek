---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hippogriff"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Hippogriff"
level: 2
source: "Monster Core"
aon_id: "creature-3052"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3052"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hippogriff"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +7, Survival +6"
abilityMods: [3, 3, 2, -4, 2, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +6"
hp: 32
health:
  - name: "HP"
    desc: "32"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 17"
speed: "30 feet, fly 65 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +9 __Damage__ 1d10+3 piercing"
  - name: "Melee"
    desc: "⬻ talon +9 (Agile) __Damage__ 1d6+3 slashing"
  - name: "Melee"
    desc: "⬻ wing +9 (reach 10 feet) __Damage__ 1d6+3 bludgeoning"
abilities_bot:
  - name: "Flying Strafe"
    desc: "⬺ The hippogriff Fliesup to its fly speed and makes two talon Strikes at any point during that movement. Each Strike must target a different creature. The attacks take the normal multiple attack penalty."
sourcebook: "_Monster Core_, page 197."
```

```encounter-table
name: Hippogriff
creatures:
  - 1: Hippogriff
```
