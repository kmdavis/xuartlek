---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Prophet"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Prophet"
level: 2
source: "NPC Core"
aon_id: "creature-3442"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3442"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Prophet"
level: "Creature 2"
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
    desc: "Diplomacy +8, Performance +8, Religion +7, Survival +7"
abilityMods: [2, 1, 0, 1, 3, 4]
abilities_top:
  - name: "Items"
    desc: "Flail, manifesto (functions as a religious text), pouch of rocks, robes"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +7; __Will__: +11"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flail +8 (Disarm, Sweep, Trip) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +7 (thrown 10 feet) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 18, 1 Focus Point - __1st__ Read Fate"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ Daze, Detect Magic, Guidance, Know the Way, Light, Read Aura - __1st__ Bless, Enfeeble, Heal, Sanctuary (4 slots)"
sourcebook: "_NPC Core_, page 30."
```

```encounter-table
name: Prophet
creatures:
  - 1: Prophet
```
