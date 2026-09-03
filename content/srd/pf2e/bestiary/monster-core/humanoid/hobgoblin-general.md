---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin General"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hobgoblin General"
level: 6
source: "Monster Core"
aon_id: "creature-3055"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3055"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hobgoblin General"
level: "Creature 6"
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +15, Intimidation +14, Stealth +12"
abilityMods: [4, 3, 2, 0, 1, 2]
abilities_top:
  - name: "General's Cry"
    desc: "When a hobgoblin general rolls initiative, as long as they can perceive at least one foe, they can yell a mighty battle cry. The hobgoblin general attempts an Intimidation check to Demoralize a single foe within 60 feet as a free action. If successful, any ally can, as its first action on its first turn of the combat, Stride up to double its speed as a single action."
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), _+1 glaive_, Half Plate"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +12; __Ref__: +15; __Will__: +13"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Formation"
    desc: "When they're adjacent to at least two other allies, the hobgoblin general gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _glaive_ +17 (deadly d8, Forceful, Reach) __Damage__ 1d8+10 slashing"
  - name: "Ranged"
    desc: "⬻ composite shortbow +15 (Brutal, deadly d10, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Polearm Critical Specialization"
    desc: "On a critical hit, the target of the critical hit is moved 5 feet in a direction of the hobgoblin general's choice."
sourcebook: "_Monster Core_, page 199."
```

```encounter-table
name: Hobgoblin General
creatures:
  - 1: Hobgoblin General
```
