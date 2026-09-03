---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brontosaurus"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Brontosaurus"
level: 10
source: "Monster Core"
aon_id: "creature-2922"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2922"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Brontosaurus"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +23"
abilityMods: [9, 0, 5, -4, 2, 1]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +21; __Ref__: +14; __Will__: +16"
hp: 220
health:
  - name: "HP"
    desc: "220"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +23 (Sweep, reach 20 feet) __Damage__ 2d10+13 bludgeoning plus Improved Knockdown"
  - name: "Melee"
    desc: "⬻ foot +23 (reach 15 feet) __Damage__ 2d8+13 bludgeoning"
abilities_bot:
  - name: "Tail Sweep"
    desc: "⬺ The brontosaurus makes a tail Strike and compares the attack roll to the AC of up to three foes, each of whom must be within its tail's melee reach and adjacent to at least one other target. It rolls damage only once and applies it to each creature hit. A Tail Sweep counts as two attacks for its multiple attack penalty."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 29"
sourcebook: "_Monster Core_, page 100."
```

```encounter-table
name: Brontosaurus
creatures:
  - 1: Brontosaurus
```
