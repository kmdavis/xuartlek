---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grizzly Bear"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Grizzly Bear"
level: 3
source: "Monster Core"
aon_id: "creature-2850"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2850"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Grizzly Bear"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [4, 1, 5, -4, 1, -2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +12; __Ref__: +6; __Will__: +8"
hp: 59
health:
  - name: "HP"
    desc: "59"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 2d8+4 piercing"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d10+4 slashing plus Grab"
abilities_bot:
  - name: "Mauler"
    desc: "The grizzly bear gains a +2 circumstance bonus to damage rolls against creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
  - name: "Rush"
    desc: "⬺ The grizzly bear Strides and makes a Strike at the end of that movement. During the Stride, the grizzly bear gains a +10-foot circumstance bonus to its Speed. Loaded for Bear A bear den can contain valuable treasures, such as the remains of less fortunate adventurers who stumbled onto a hungry bear's path. Bear furs themselves are valued as rugs, while their claws and fangs make for impressive jewelry or adornments for armor. Bear hide is an excellent resource for [[srd/pf2e/compendium/equipment/armor#Hide Armor|hide armor]]."
sourcebook: "_Monster Core_, page 41."
```

```encounter-table
name: Grizzly Bear
creatures:
  - 1: Grizzly Bear
```
