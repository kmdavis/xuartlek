---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arms Dealer"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Arms Dealer"
level: 2
source: "NPC Core"
aon_id: "creature-3506"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3506"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Arms Dealer"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (11 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +7, Deception +7, Diplomacy +7, Firearm Lore +14, Intimidation +9, Society +9, Underworld Lore +9"
abilityMods: [0, 3, 0, 1, 3, 3]
abilities_top:
  - name: "Arms Dealing Specialist"
    desc: "For encounters involving the purchase of weapons, the arms dealer is a 5th-level challenge."
  - name: "Items"
    desc: "Flintlock Musket (20 rounds), Hand Cannon (20 rounds), sword cane"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +7; __Will__: +9"
hp: 28
health:
  - name: "HP"
    desc: "28 __You Call That a Gun?__ The arms dealer seems unaffected by your attempts to threaten them. The arms dealer gains a +2 circumstance bonus to their Will DC against Intimidation checks while they're holding a firearm."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sword cane +9 (Agile, Concealable, Finesse) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ flintlock musket +11 (Concussive, fatal d10, range increment 70 feet, reload 1) __Damage__ 1d6+3 piercing"
  - name: "Ranged"
    desc: "⬻ hand cannon +11 (modular B, or S; range increment 30 feet; reload 1) __Damage__ 1d6+3 modular"
abilities_bot:
  - name: "Take Stock"
    desc: "⬻ (Auditory, Concentrate, Linguistic, Mental) The arms dealer advises an ally on how to properly use a firearm. The arms dealer chooses an ally within 30 feet wielding a firearm. That ally can use a reaction to Interact to reload their firearm."
sourcebook: "_NPC Core_, page 76."
```

```encounter-table
name: Arms Dealer
creatures:
  - 1: Arms Dealer
```
