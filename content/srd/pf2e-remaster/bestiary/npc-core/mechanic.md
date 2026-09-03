---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mechanic"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mechanic"
level: 1
source: "NPC Core"
aon_id: "creature-3457"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3457"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mechanic"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
skills:
  - name: "Skills"
    desc: "Athletics +7, Crafting +16, Engineering Lore +16, Thievery +6"
abilityMods: [4, 1, 1, 3, 0, 0]
abilities_top:
  - name: "Mechanical Repair"
    desc: "The mechanic is trained in Crafting, but a master in Crafting for mechanical devices, siege weapons, and vehicles. They can Repair in 1 minute instead of 10 minutes, or in 3 actions for a mechanical device, siege weapon, or vehicle."
  - name: "Mechanical Specialist"
    desc: "For encounters involving mechanical repair, the mechanic is an 8th-level challenge."
  - name: "Items"
    desc: "Arbalest (20 bolts), heavy wrench, Repair Toolkit"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +8; __Ref__: +6; __Will__: +3"
hp: 22
health:
  - name: "HP"
    desc: "22"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ heavy wrench +7 (Shove) __Damage__ 1d6+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ arbalest +8 (Backstabber, range increment 110 feet, reload 1) __Damage__ 1d10 piercing"
abilities_bot:
  - name: "Risky Upgrade"
    desc: "⬺ (Concentrate, Manipulate) The mechanic pushes a mechanical device, siege weapon, or vehicle pasts its regular limits with a temporary upgrade chosen from the list below. An item can have only one risky upgrade at a time. If an item has an upgrade at the start of the mechanic's turn, the mechanic must attempt a DC 5 flat check. (These flat checks continue even if the mechanic is dead or otherwise can't take turns.) On a failure, the item explodes, dealing damage equal to the item's level to all adjacent creatures and ending the upgrade."
  - name: "Overheat Weapons"
    desc: "If the item would deal damage, it deals an additional 1d6 fire damage. This increases to 2d6 if the item is 8th level or higher."
  - name: "Pressured Plating"
    desc: "The item gains a +3 status bonus to its Hardness and gains temporary Hit Points equal to double its level that last for 10 minutes."
  - name: "Propelled Boost"
    desc: "If the item has a Speed, the item gains a +15-foot status bonus to Speed."
sourcebook: "_NPC Core_, page 42."
```

```encounter-table
name: Mechanic
creatures:
  - 1: Mechanic
```
