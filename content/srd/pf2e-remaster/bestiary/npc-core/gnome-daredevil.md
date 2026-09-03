---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnome Daredevil"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Gnome Daredevil"
level: 2
source: "NPC Core"
aon_id: "creature-3637"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3637"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gnome Daredevil"
level: "Creature 2"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; low-light vision"
languages: "Common, Gnomish"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +7, Performance +8, Thievery +7"
abilityMods: [3, 4, 1, 1, 1, 3]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Gnome Flickmace"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +12; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ gnome flickmace +11 (Reach, Sweep) __Damage__ 1d6+3 bludgeoning plus Knockdown"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +9 (deadly d10, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Daredevil Strike"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The gnome daredevil Strides up to their Speed, makes a melee Strike, then Steps."
sourcebook: "_NPC Core_, page 183."
```

```encounter-table
name: Gnome Daredevil
creatures:
  - 1: Gnome Daredevil
```
