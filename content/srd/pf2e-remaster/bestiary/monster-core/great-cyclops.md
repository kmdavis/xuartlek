---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Great Cyclops"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/mutant
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Great Cyclops"
level: 12
source: "Monster Core"
aon_id: "creature-2890"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2890"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Great Cyclops"
level: "Creature 12"
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Mutant"
trait_04: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; low-light vision"
languages: "Common, Cyclops, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +25, any one Lore +18, Survival +22"
abilityMods: [7, 1, 6, -2, 4, -1]
abilities_top:
  - name: "Items"
    desc: "Greatclub, Hide Armor"
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +25; __Ref__: +19; __Will__: +22"
hp: 235
health:
  - name: "HP"
    desc: "235"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
  - name: "Flash of Brutality"
    desc: "⭓ (fortune, occult)"
  - name: "Frequency"
    desc: "once per day, and recharges when the great cyclops uses Ferocity"
  - name: "Trigger"
    desc: "The great cyclops succeeds at an attack roll"
  - name: "Effect"
    desc: "The attack becomes a critical success."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatclub +25 (Backswing, reach 15 feet, Shove) __Damage__ 3d10+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +25 (reach 15 feet) __Damage__ 2d10+13 piercing"
  - name: "Melee"
    desc: "⬻ fist +25 (Agile, reach 15 feet) __Damage__ 3d4+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +23 (Brutal, range increment 120 feet) __Damage__ 4d6+7 bludgeoning"
abilities_bot:
  - name: "Powerful Charge"
    desc: "⬺ The great cyclops Strides twice and makes a horn Strike. If they moved at least 20 feet away from their starting position, the Strike's damage is increased to 3d10+20."
  - name: "Throw Rock"
    desc: "⬻ Cyclops Seers Great cyclopes are traditionally violent creatures, but some retain fragments of the old ways that lull them into periods of calm. During such times, they can be incredible sources of information, but one must take care to be well away from the great cyclops's lair before its bestial rage wakens once more."
sourcebook: "_Monster Core_, page 71."
```

```encounter-table
name: Great Cyclops
creatures:
  - 1: Great Cyclops
```
