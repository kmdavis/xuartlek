---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wyrwood Sneak"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/wyrwood
  - pf2e/creature/trait/small
statblock: inline
name: "Wyrwood Sneak"
level: 1
source: "Monster Core 2"
aon_id: "creature-4619"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4619"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wyrwood Sneak"
level: "Creature 1"
size: "Small"
trait_01: "Construct"
trait_02: "Rare"
trait_03: "Wyrwood"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Common; plus one regional language"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Arcana +5, Deception +7, Society +5, Stealth +7"
abilityMods: [0, 4, 0, 2, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Buckler (Hardness 3, HP 6, BT 3), Shortsword"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +9; __Will__: +8"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ bleed"
abilities_mid:
  - name: "Living Machine"
    desc: "Though their body is an organic construct, a wyrwood is a living creature. They're not immediately destroyed when reduced to 0 HP, but rather fall unconscious and eventually die. They don't need to eat or drink. They can be targeted by effects that target living creatures or that target constructs."
  - name: "No Breath"
    desc: "A wyrwood doesn't breathe and is immune to effects that require breathing (such as an inhaled poison)."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +9 (Agile, finesse, versatile S) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The wyrwood's Strikes deal an additional 1d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core 2_, page 357."
```

```encounter-table
name: Wyrwood Sneak
creatures:
  - 1: Wyrwood Sneak
```
