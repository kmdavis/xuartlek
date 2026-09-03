---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Druid Initiate"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Druid Initiate"
level: 1
source: "NPC Core"
aon_id: "creature-3580"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3580"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Druid Initiate"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common, Wildsong"
skills:
  - name: "Skills"
    desc: "Diplomacy +3, Medicine +7, Nature +7, Stealth +4, Survival +7"
abilityMods: [2, 1, 2, 0, 4, 0]
abilities_top:
  - name: "Items"
    desc: "Healer's Toolkit, Leather Armor, Primal Symbol, Sling (10 bullets), Staff"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +4; __Will__: +9"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +7 (two-hand d8) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +6 (Propulsive, range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Spells Primal Spellcasting"
    desc: "DC 17 - __Cantrips (1st)__ Detect Magic, Ignition, Know the Way, Light, Tangle Vine - __1st__ Heal, Thunderstrike"
  - name: "Druid Order Spells"
    desc: "DC 17, 1 Focus Point - __1st__ Cornucopia"
sourcebook: "_NPC Core_, page 547."
```

```encounter-table
name: Druid Initiate
creatures:
  - 1: Druid Initiate
```
