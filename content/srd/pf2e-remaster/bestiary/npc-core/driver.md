---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Driver"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Driver"
level: 2
source: "NPC Core"
aon_id: "creature-3458"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3458"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Driver"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +7, Deception +7, Driving Lore +8, Engineering Lore +8, Intimidation +7, Piloting Lore +8, Stealth +8"
abilityMods: [1, 4, 0, 2, 2, 1]
abilities_top:
  - name: "Driving Specialist"
    desc: "For encounters involving driving, the driver is an 8th-level challenge. Rules for vehicles appear here."
  - name: "Express Driver"
    desc: "A driver can attempt a Driving Lore check to increase a vehicle's travel Speed when calculating the value for a day. The DC is determined by the GM but is typically based on the vehicle's piloting DC or the difficulty of traversing the environment, whichever is harder. On a success, increase the vehicle's travel Speed by half."
  - name: "Skilled Driver"
    desc: "The driver gains a +10 circumstance bonus to any skill check involved in driving a vehicle, and is considered a master in the skill for such checks. This bonus also applies to any initiative roll while the driver is piloting a vehicle."
  - name: "Items"
    desc: "crowbar (functions as a pick), Hand Crossbow (10 bolts), Leather Armor"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +8; __Will__: +6 +6 status to all defenses while driving"
hp: 28
health:
  - name: "HP"
    desc: "28"
abilities_mid:
  - name: "Vehicle Block"
    desc: "⬲"
  - name: "Requirements"
    desc: "The driver is driving a vehicle"
  - name: "Trigger"
    desc: "The driver would take damage from an attack or from a damaging effect that requires a Reflex save"
  - name: "Effect"
    desc: "With swift steering, the driver puts the bulk of the vehicle in between themself and the problem, causing the vehicle to take the damage instead of the driver."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ crowbar +7 (fatal d10) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Sideswipe"
    desc: "⬲"
  - name: "Requirements"
    desc: "The driver is taking a Drive action with a vehicle and moves the vehicle adjacent to a creature"
  - name: "Effect"
    desc: "All creatures adjacent to the vehicle take the vehicle's collision damage with a basic Reflex save against the vehicle's collision DC. The vehicle continues to move normally after the Sideswipe. Aviator Not all drivers limit themselves to the earth. Aviators are drivers who specialize in driving mechanical flying machines. Many see such drivers as being reckless, as they are often unsatisfied with simply flying from point A to point B. Instead, they take full advantage of the freedom of the sky to find the most exciting path available, which often involves dubiously named stunts."
sourcebook: "_NPC Core_, page 43."
```

```encounter-table
name: Driver
creatures:
  - 1: Driver
```
