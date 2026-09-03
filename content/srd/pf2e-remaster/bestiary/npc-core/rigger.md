---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rigger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Rigger"
level: 1
source: "NPC Core"
aon_id: "creature-3597"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3597"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Rigger"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +7, Sailing Lore +6"
abilityMods: [3, 4, 1, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Dagger (2), Rope (50 feet)"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +10; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Death from Above"
    desc: "The rigger deals an additional 1d4 precision damage to any creature at a lower elevation than themself."
  - name: "Practiced Climber"
    desc: "The rigger requires only one hand free to Climb and is not off-guard when Climbing."
  - name: "Rope Tension Spring"
    desc: "⬺ (Manipulate, Move)"
  - name: "Requirements"
    desc: "The rigger is adjacent to a vertical rope on board a ship and is wielding a dagger"
  - name: "Effect"
    desc: "The rigger loops the rope around one arm and severs the rope with their dagger. Counterweight and tension pull the rigger 20 feet straight up."
sourcebook: "_NPC Core_, page 146."
```

```encounter-table
name: Rigger
creatures:
  - 1: Rigger
```
