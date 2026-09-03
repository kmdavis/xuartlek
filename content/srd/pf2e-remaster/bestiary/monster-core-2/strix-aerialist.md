---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Strix Aerialist"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/strix
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Strix Aerialist"
level: 9
source: "Monster Core 2"
aon_id: "creature-4568"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4568"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Strix Aerialist"
level: "Creature 9"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Strix"
trait_03: "Uncommon"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision"
languages: "Common, Strix"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +20, Deception +18, Performance +20, Society +16, Stealth +20, Thievery +18"
abilityMods: [3, 5, 2, 1, 2, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 striking dagger_ (2), _+1 leather armor_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +18; __Ref__: +21; __Will__: +15"
hp: 120
health:
  - name: "HP"
    desc: "120"
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +21 (Agile, finesse, magical, versatile S) __Damage__ 2d4+7 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +21 (Agile, magical, thrown 10 feet, versatile S) __Damage__ 2d4+7 piercing"
abilities_bot:
  - name: "Aerial Feint"
    desc: "⬻ (Mental) The aerialist chooses a creature within 20 feet and attempts an Acrobatics check against the target's Perception DC. On a success, the target is off-guard against the aerialist's Strikes for 1 round."
  - name: "Dive Bomb"
    desc: "⬺ The strix aerialist Flies up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a melee Strike."
  - name: "Sneak Attack"
    desc: "The strix aerialist's Strikes deal an additional 2d6 precision damage to off-guard creatures."
sourcebook: "_Monster Core 2_, page 307."
```

```encounter-table
name: Strix Aerialist
creatures:
  - 1: Strix Aerialist
```
