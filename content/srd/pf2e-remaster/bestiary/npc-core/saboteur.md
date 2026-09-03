---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Saboteur"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Saboteur"
level: 2
source: "NPC Core"
aon_id: "creature-3608"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3608"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Saboteur"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; (10 to find traps)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +5, Crafting +6, Deception +7, Diplomacy +5, Engineering Lore +8, Intimidation +5, Society +6, Stealth +9, Survival +6, Thievery +9, Underworld Lore +6"
abilityMods: [1, 3, 1, 2, 2, 1]
abilities_top:
  - name: "Snare Crafting"
    desc: "The saboteur can Craft snares and has the supplies to make up to two caltrop snares and up to two hampering snares. Snare rules can be found here."
  - name: "Items"
    desc: "Artisan's Toolkit (snare toolkit), Crowbar, Disguise Kit, Hand Crossbow (10 bolts), Sap, Thieves' Toolkit"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +9 (+11 vs. traps); __Will__: +8"
hp: 28
health:
  - name: "HP"
    desc: "28"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sap +7 (Agile, Nonlethal) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The saboteur deals an extra 1d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 153."
```

```encounter-table
name: Saboteur
creatures:
  - 1: Saboteur
```
