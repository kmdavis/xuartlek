---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Iguanodon"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Iguanodon"
level: 6
source: "Monster Core 2"
aon_id: "creature-4335"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4335"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Iguanodon"
level: "Creature 6"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [7, 4, 4, -4, 4, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +14"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ thumb spike +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+9 piercing"
  - name: "Melee"
    desc: "⬻ tail +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+9 bludgeoning"
abilities_bot:
  - name: "Gouging Lunge"
    desc: "⬺ The iguanodon makes a thumb spike Strike at an adjacent foe and then [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] up to 15 feet, dragging its thumb spike across the foe to gouge out a brutal wound. If this Strike hits, it deals an extra 1d8 slashing damage, and the following Stride doesn’t trigger reactions from the creature struck. This thumb spike Strike counts as two attacks when calculating the iguanodon’s multiple attack penalty."
sourcebook: "_Monster Core 2_, page 107."
```

```encounter-table
name: Iguanodon
creatures:
  - 1: Iguanodon
```
