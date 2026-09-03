---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Servant"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Servant"
level: -1
source: "NPC Core"
aon_id: "creature-3489"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3489"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Servant"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Diplomacy +4, Lore +6, Society +2"
abilityMods: [1, 3, 1, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "cutlery, servant's uniform, serving platter"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +7; __Will__: +3"
hp: 7
health:
  - name: "HP"
    desc: "7"
abilities_mid:
  - name: "Quick Catch"
    desc: "⬲"
  - name: "Trigger"
    desc: "An object the servant could hold in one hand is dropped within the servant's reach"
  - name: "Requirements"
    desc: "The servant has at least one hand free"
  - name: "Effect"
    desc: "The servant catches the dropped object before it hits the floor or leaves their reach."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ cutlery +6 (Agile, Finesse, versatile S) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ cutlery +6 (Agile, thrown 15 feet, versatile S) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Protective Platter"
    desc: "The servant can raise their serving platter using the Raise a Shield action. The platter has the same statistics as a buckler but requires a hand to hold."
sourcebook: "_NPC Core_, page 66."
```

```encounter-table
name: Servant
creatures:
  - 1: Servant
```
