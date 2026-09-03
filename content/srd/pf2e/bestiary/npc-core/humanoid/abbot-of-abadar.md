---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Abbot of Abadar"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Abbot of Abadar"
level: 1
source: "NPC Core"
aon_id: "creature-3439"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3439"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Abbot of Abadar"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common, Empyrean, Utopian"
skills:
  - name: "Skills"
    desc: "Deception +6, Diplomacy +8, Religion +21, Society +7"
abilityMods: [1, 1, -2, 2, 4, 3]
abilities_top:
  - name: "Religious Specialist"
    desc: "For encounters involving religious debates or conflicts of doctrine, the abbot is a 9th-level challenge."
  - name: "True Faith"
    desc: "The abbot uses lessons from scripture to foil others trying to deceive them. They can use their Religion modifier to Sense Motive instead of Perception, and their Religion DC instead of their Perception DC against attempts to Lie to them."
  - name: "Items"
    desc: "Crossbow (10 bolts), griffon cane (functions as a staff), religious symbol of Abadar"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +3; __Ref__: +4; __Will__: +11"
hp: 15
health:
  - name: "HP"
    desc: "15"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ griffon cane +6 (two-hand d8) __Damage__ 1d4+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +6 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ crossbow +6 (range increment 120 feet, reload 1) __Damage__ 1d8+2 piercing"
abilities_bot:
  - name: "Divine Protection"
    desc: "⬺ (Concentrate)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The abbot beseeches their deity to protect someone in their charge, attempting a DC 25 Religion check. If it succeeds, a divine _sanctuary_ spell affects one of the abbot's allies within 60 feet. The Will DC is 17"
sourcebook: "_NPC Core_, page 28."
```

```encounter-table
name: Abbot of Abadar
creatures:
  - 1: Abbot of Abadar
```
