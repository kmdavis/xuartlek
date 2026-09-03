---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dromaar Mountaineer"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/dromaar
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/half-orc
statblock: inline
name: "Dromaar Mountaineer"
level: 2
source: "Monster Core"
aon_id: "creature-3131"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3131"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dromaar Mountaineer"
level: "Creature 2"
size: "Medium"
trait_01: "Dromaar"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Orc"
trait_05: "Half-Orc"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Athletics +7, Acrobatics +7, Survival +8"
abilityMods: [3, 3, 1, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Pick, Hide Armor, Rope (50 feet), Bola (6)"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +9; __Will__: +8"
hp: 28
health:
  - name: "HP"
    desc: "28"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pick +9 (fatal d10) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Shove) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ bola +9 (Nonlethal, Ranged Trip, thrown 20 feet) __Damage__ 1d6+3 bludgeoning"
abilities_bot:
  - name: "Tangle Prey"
    desc: "⬻ The dromaar draws a bola and Strikes a target within 20 feet. On a success, the dromaar immediately rolls an Athletics check against the target's Fortitude DC to Trip them."
sourcebook: "_Monster Core_, page 259."
```

```encounter-table
name: Dromaar Mountaineer
creatures:
  - 1: Dromaar Mountaineer
```
