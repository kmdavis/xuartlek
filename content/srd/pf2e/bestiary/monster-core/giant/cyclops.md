---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cyclops"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Cyclops"
level: 5
source: "Monster Core"
aon_id: "creature-2889"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2889"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cyclops"
level: "Creature 5"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "Common, Cyclops, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +14, Fortune-Telling Lore +13, Intimidation +10, Survival +12"
abilityMods: [5, -1, 2, 0, 3, -1]
abilities_top:
  - name: "Items"
    desc: "Greataxe, Heavy Crossbow (10 bolts), Hide Armor"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +8; __Will__: +12"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
  - name: "Flash of Insight"
    desc: "⭓ (fortune, occult"
  - name: "Frequency"
    desc: "once per day)"
  - name: "Trigger"
    desc: "The cyclops is about to roll a d20"
  - name: "Effect"
    desc: "The cyclops peers into an occluded spectrum of possible futures. They get a success (but not a critical success) on the roll instead of rolling."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +14 (reach 10 feet, Sweep) __Damage__ 1d12+9 slashing"
  - name: "Ranged"
    desc: "⬻ heavy crossbow +8 (range increment 120 feet, reload 2) __Damage__ 1d10+4 piercing"
abilities_bot:
  - name: "Swipe"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The cyclops makes a melee Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within their melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. A Swipe counts as two attacks for the cyclops's multiple attack penalty."
sourcebook: "_Monster Core_, page 70."
```

```encounter-table
name: Cyclops
creatures:
  - 1: Cyclops
```
