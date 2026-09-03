---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cave Bear"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Cave Bear"
level: 6
source: "Monster Core"
aon_id: "creature-2851"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2851"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cave Bear"
level: "Creature 6"
size: "Large"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [6, 1, 6, -4, 1, -1]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +11; __Will__: +13"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 __Damage__ 2d10+6 piercing"
  - name: "Melee"
    desc: "⬻ claw +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+6 slashing plus Grab"
abilities_bot:
  - name: "Mauler"
    desc: "The bear gains a +4 circumstance bonus to damage rolls against creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
  - name: "Rush"
    desc: "⬺ The cave bear Strides and makes a Strike at the end of that movement. During the Stride, it gains a +10-foot circumstance bonus to its Speed."
sourcebook: "_Monster Core_, page 41."
```

```encounter-table
name: Cave Bear
creatures:
  - 1: Cave Bear
```
