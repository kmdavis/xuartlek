---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warg"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/medium
statblock: inline
name: "Warg"
level: 2
source: "Monster Core"
aon_id: "creature-3230"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3230"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Warg"
level: "Creature 2"
size: "Medium"
trait_01: "Beast"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "Common, Goblin, Orcish"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +8, Deception +6, Intimidation +6, Stealth +7, Survival +8"
abilityMods: [4, 3, 3, -1, 2, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +9; __Will__: +6"
hp: 36
health:
  - name: "HP"
    desc: "36"
abilities_mid:
  - name: "Avenging Bite"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the warg's jaws attacks one of the warg's allies"
  - name: "Effect"
    desc: "The warg makes a jaws Strike against the triggering creature."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d8+4 piercing plus Grab"
abilities_bot:
  - name: "Pack Attack"
    desc: "The warg's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the warg's allies."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Small, 1d6+2 bludgeoning, Rupture 9"
sourcebook: "_Monster Core_, page 341."
```

```encounter-table
name: Warg
creatures:
  - 1: Warg
```
