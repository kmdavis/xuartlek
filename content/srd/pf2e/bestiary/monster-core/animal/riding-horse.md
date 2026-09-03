---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Riding Horse"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Riding Horse"
level: 1
source: "Monster Core"
aon_id: "creature-3058"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3058"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Riding Horse"
level: "Creature 1"
size: "Large"
trait_01: "Animal"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7"
abilityMods: [4, 3, 4, -4, 2, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +6; __Will__: +5"
hp: 22
health:
  - name: "HP"
    desc: "22"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 16"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hoof +7 __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Gallop"
    desc: "⬺ The riding horse Strides twice. It has a +10-foot circumstance bonus to its Speed during these Strides."
sourcebook: "_Monster Core_, page 201."
```

```encounter-table
name: Riding Horse
creatures:
  - 1: Riding Horse
```
