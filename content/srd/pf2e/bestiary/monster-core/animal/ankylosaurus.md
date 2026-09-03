---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ankylosaurus"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Ankylosaurus"
level: 6
source: "Monster Core"
aon_id: "creature-2919"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2919"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ankylosaurus"
level: "Creature 6"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17"
abilityMods: [7, 0, 4, -4, 2, -1]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +10; __Will__: +12"
hp: 90
health:
  - name: "HP"
    desc: "90"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/backswing|Backswing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+7 bludgeoning plus punishing tail"
  - name: "Melee"
    desc: "⬻ foot +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+7 bludgeoning"
abilities_bot:
  - name: "Punishing Tail"
    desc: "A creature struck by the ankylosaurus's tail must attempt a DC 24 Fortitude save. On a failure, it's [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]; on a critical failure, it's stunned 3."
  - name: "Trample"
    desc: "⬽ Medium or smaller, foot, DC 24"
sourcebook: "_Monster Core_, page 98."
```

```encounter-table
name: Ankylosaurus
creatures:
  - 1: Ankylosaurus
```
