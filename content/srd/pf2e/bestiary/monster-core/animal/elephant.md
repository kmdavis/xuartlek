---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elephant"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Elephant"
level: 7
source: "Monster Core"
aon_id: "creature-2993"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2993"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elephant"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +17, Survival +15"
abilityMods: [7, 0, 4, -4, 2, -2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +18; __Ref__: +11; __Will__: +13"
hp: 130
health:
  - name: "HP"
    desc: "130"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusk +16 (reach 10 feet) __Damage__ 3d8+9 piercing"
  - name: "Melee"
    desc: "⬻ trunk +18 (reach 15 feet) __Damage__ grabbing trunk"
  - name: "Melee"
    desc: "⬻ foot +16 (reach 10 feet) __Damage__ 2d10+9 bludgeoning"
abilities_bot:
  - name: "Grabbing Trunk"
    desc: "A Medium or smaller creature hit by the elephant's trunk is grabbed. If the elephant moves, it can bring the grabbed creature along with it."
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 24"
sourcebook: "_Monster Core_, page 150."
```

```encounter-table
name: Elephant
creatures:
  - 1: Elephant
```
