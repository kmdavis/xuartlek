---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Larval Ofalth"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Larval Ofalth"
level: 4
source: "Monster Core"
aon_id: "creature-3116"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3116"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Larval Ofalth"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +9"
abilityMods: [5, 1, 3, -2, 1, -2]
abilities_top:
  - name: "Hide in Filth"
    desc: "A larval ofalth can hide in any pile of filth or trash that is its size or larger, allowing it to use Stealth for initiative. If it rolls Stealth for initiative, on the first round of combat, creatures that haven't acted yet are off-guard to it."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +9; __Will__: +9"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ disease, poison"
abilities_mid:
  - name: "Stench"
    desc: "(aura, olfactory) 30 feet, DC 19"
  - name: "Shield Block"
    desc: "⬲ The larval ofalth's trash shield has a hardness of 5 and 20 Hit Points."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 __Damage__ 2d8+5 slashing plus wretched weeps"
  - name: "Ranged"
    desc: "⬻ leachate +11 (range 20 feet) __Damage__ 3d8 acid plus wretched weeps"
abilities_bot:
  - name: "Wretched Weeps"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "2d4 persistent bleed every hour and enfeebled 1 (1 day)"
  - name: "Stage 3"
    desc: "2d6 persistent bleed every hour and enfeebled 2 (1 day)"
sourcebook: "_Monster Core_, page 249."
```

```encounter-table
name: Larval Ofalth
creatures:
  - 1: Larval Ofalth
```
