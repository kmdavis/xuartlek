---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pteranodon"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Pteranodon"
level: 2
source: "Monster Core"
aon_id: "creature-3151"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3151"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pteranodon"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7"
abilityMods: [3, 4, 1, -4, 2, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +10; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "10 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +10 __Damage__ 1d10+3 piercing"
abilities_bot:
  - name: "Swoop"
    desc: "⬺ The pteranodon [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to its Speed and makes one beak Strike at any point during that movement."
sourcebook: "_Monster Core_, page 278."
```

```encounter-table
name: Pteranodon
creatures:
  - 1: Pteranodon
```
