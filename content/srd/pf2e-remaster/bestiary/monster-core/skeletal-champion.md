---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeletal Champion"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Skeletal Champion"
level: 2
source: "Monster Core"
aon_id: "creature-3194"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3194"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Skeletal Champion"
level: "Creature 2"
size: "Medium"
trait_01: "Skeleton"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +8, Intimidation +7"
abilityMods: [4, 4, 1, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Chain Mail, Lance, Longsword, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +5; __Ref__: +10; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 5, electricity 5, fire 5, piercing 5, slashing 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longsword +10 (versatile P) __Damage__ 1d8+4 slashing"
  - name: "Melee"
    desc: "⬻ claw +10 (Agile) __Damage__ 1d6+4 slashing"
  - name: "Melee"
    desc: "⬻ lance +10 (deadly d8, jousting d6, reach 10 feet) __Damage__ 1d8+4 piercing"
sourcebook: "_Monster Core_, page 312."
```

```encounter-table
name: Skeletal Champion
creatures:
  - 1: Skeletal Champion
```
