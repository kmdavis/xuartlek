---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dwarf Smith"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Dwarf Smith"
level: 0
source: "NPC Core"
aon_id: "creature-3626"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3626"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Dwarf Smith"
level: "Creature 0"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Common, Dwarven"
skills:
  - name: "Skills"
    desc: "Athletics +6, Crafting +12, Society +6"
abilityMods: [2, 1, 2, 3, 1, -1]
abilities_top:
  - name: "Blacksmithing Specialist"
    desc: "For encounters involving blacksmithing, the dwarf smith is a 5th-level challenge."
  - name: "Temper Armament"
    desc: "(downtime) The smith spends 1 day tempering a single suit of metallic armor, metallic shield, or metallic weapon. Tempering armor or a shield increases its Hardness by 1. Tempering a weapon grants the weapon a +1 circumstance bonus to damage rolls. Regardless of the item, the tempering remains for 3 days, after which item is temporarily immune to further tempering for 1 week as the technique would otherwise damage it."
  - name: "Items"
    desc: "Artisan's Toolkit (blacksmithing), Clan Dagger, leather apron (functions as padded armor), Light Hammer"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +6; __Ref__: +3; __Will__: +5"
hp: 12
health:
  - name: "HP"
    desc: "12; __Resistances__ fire 1"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light hammer +6 (Agile) __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ clan dagger +6 (Agile, Parry, versatile B) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ light hammer +4 (Agile, thrown 20 feet) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Crack the Shell"
    desc: "⬺ The dwarf smith makes a Strike to break a creature's defenses. If the Strike hits and the creature is wearing armor with Hardness 9 or lower, the armor is broken. This Strike doesn't further damage armor that's already broken."
sourcebook: "_NPC Core_, page 174."
```

```encounter-table
name: Dwarf Smith
creatures:
  - 1: Dwarf Smith
```
