---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hadrosaurid"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Hadrosaurid"
level: 4
source: "Monster Core"
aon_id: "creature-2918"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2918"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hadrosaurid"
level: "Creature 4"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [6, 2, 3, -4, 1, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +10; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d6+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ foot +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d4+8 bludgeoning"
abilities_bot:
  - name: "Sprint"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The hadrosaurid Strides twice. It has a +20-foot circumstance bonus to its Speed during these Strides."
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 21"
sourcebook: "_Monster Core_, page 98."
```

```encounter-table
name: Hadrosaurid
creatures:
  - 1: Hadrosaurid
```
