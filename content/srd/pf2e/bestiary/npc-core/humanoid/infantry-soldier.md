---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Infantry Soldier"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Infantry Soldier"
level: 2
source: "NPC Core"
aon_id: "creature-3522"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3522"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Infantry Soldier"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +10, Intimidation +7, Warfare Lore +6"
abilityMods: [4, 0, 3, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "chainmail, Crossbow (10 bolts), Shortsword, Wooden Shield (Hardness 3, Hit Points 12, BT 6)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +6; __Will__: +6"
hp: 28
health:
  - name: "HP"
    desc: "28"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 (Agile, versatile S) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +6 (range increment 120 feet, reload 1) __Damage__ 1d8+2 piercing"
abilities_bot:
  - name: "Guardian Shield"
    desc: "⬻ The infantry soldier Raises their Shield, but grants the benefit to an adjacent ally and can Shield Block for that ally. Guardian Shield ends early if at any point the ally is no longer adjacent."
sourcebook: "_NPC Core_, page 88."
```

```encounter-table
name: Infantry Soldier
creatures:
  - 1: Infantry Soldier
```
