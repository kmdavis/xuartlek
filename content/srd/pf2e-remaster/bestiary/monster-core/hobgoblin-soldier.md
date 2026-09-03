---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin Soldier"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hobgoblin Soldier"
level: 1
source: "Monster Core"
aon_id: "creature-3053"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3053"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hobgoblin Soldier"
level: "Creature 1"
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Athletics +6, Stealth +6"
abilityMods: [3, 3, 2, 0, 2, -1]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Longsword, Shortbow (10 arrows), Wooden Shield (Hardness 3, HP 12, BT 6)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +6; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Formation"
    desc: "When they're adjacent to at least two other allies, the hobgoblin soldier gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longsword +8 (versatile P) __Damage__ 1d8+3 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +8 (deadly d10, range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
sourcebook: "_Monster Core_, page 198."
```

```encounter-table
name: Hobgoblin Soldier
creatures:
  - 1: Hobgoblin Soldier
```
