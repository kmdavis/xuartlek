---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tax Collector"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tax Collector"
level: -1
source: "NPC Core"
aon_id: "creature-3548"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3548"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tax Collector"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; (DC 19 against Stealing)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Deception +8, Diplomacy +8, Intimidation +8, Legal Lore +9, Mercantile Lore +10, Society +9, Thievery +6"
abilityMods: [0, 1, 0, 3, 2, 2]
abilities_top:
  - name: "Financial Specialist"
    desc: "When dealing with matters of taxes and finance, the tax collector is a 3rd-level challenge."
  - name: "Items"
    desc: "Crossbow (10 bolts), Dagger, collection of expired documents with intact seals, Merchant's Scale, Padded Armor, tax documents in scroll case"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +2; __Ref__: +3; __Will__: +8"
hp: 6
health:
  - name: "HP"
    desc: "6"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +5 (Agile, Finesse, versatile S) __Damage__ 1d4 piercing"
  - name: "Melee"
    desc: "⬻ fist +5 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +5 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing"
abilities_bot:
  - name: "Glittering Distraction"
    desc: "⬻ (Emotion, Mental) The tax collector Strides. At any point during this movement, they can Interact to hurl a handful of coins. If there are commoners about, this typically causes a scene. Crowds are usually difficult terrain and have other effects."
sourcebook: "_NPC Core_, page 109."
```

```encounter-table
name: Tax Collector
creatures:
  - 1: Tax Collector
```
