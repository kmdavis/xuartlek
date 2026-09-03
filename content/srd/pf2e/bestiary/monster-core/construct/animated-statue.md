---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Animated Statue"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/medium
statblock: inline
name: "Animated Statue"
level: 3
source: "Monster Core"
aon_id: "creature-2820"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2820"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Animated Statue"
level: "Creature 3"
size: "Medium"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +11"
abilityMods: [4, -2, 5, -5, 0, -5]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +12; __Ref__: +5; __Will__: +5 construct armor"
hp: 35
health:
  - name: "HP"
    desc: "35; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 6"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated statue has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated statue is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 15."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 (Magical) __Damage__ 1d8+6 bludgeoning plus Grab"
sourcebook: "_Monster Core_, page 19."
```

```encounter-table
name: Animated Statue
creatures:
  - 1: Animated Statue
```
