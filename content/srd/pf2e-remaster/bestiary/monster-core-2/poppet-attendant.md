---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Poppet Attendant"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/small
statblock: inline
name: "Poppet Attendant"
level: 0
source: "Monster Core 2"
aon_id: "creature-4514"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4514"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Poppet Attendant"
level: "Creature 0"
size: "Small"
trait_01: "Construct"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Common; one language their creator speaks"
skills:
  - name: "Skills"
    desc: "Crafting +6, Deception +5, Diplomacy +5, Stealth +6"
abilityMods: [2, 0, 2, 0, 1, 3]
abilities_top:
  - name: "Simple Doll"
    desc: "(concentrate) The poppet attendant looks like an ordinary doll, fooling others into leaving them alone. When they're in their place of business, the poppet attendant can Hide without cover or concealment. Once a creature realizes that the poppet attendant is alive, the attendant can't Hide from them in this way again."
  - name: "Items"
    desc: "Artisan's Toolkit, Repair Toolkit, Shears, Sling (10 sling bullets)"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +9; __Ref__: +3; __Will__: +6"
hp: 17
health:
  - name: "HP"
    desc: "17; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Weaknesses__ fire 2"
abilities_mid:
  - name: "Pincushion"
    desc: "⬲"
  - name: "Trigger"
    desc: "The poppet attendant would take piercing damage"
  - name: "Effect"
    desc: "The poppet directs the implement to a soft part of its body, gaining resistance 5 against the triggering piercing damage."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shears +8 (deadly d8, Finesse, versatile P) __Damage__ 1d4+2 slashing"
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +6 (Propulsive, range increment 50 feet) __Damage__ 1d6+ bludgeoning"
sourcebook: "_Monster Core 2_, page 256."
```

```encounter-table
name: Poppet Attendant
creatures:
  - 1: Poppet Attendant
```
