---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Messenger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Messenger"
level: 1
source: "NPC Core"
aon_id: "creature-3497"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3497"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Messenger"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +5, Diplomacy +6, Society +7, Survival +4"
abilityMods: [0, 3, 4, 0, 1, 1]
abilities_top:
  - name: "Don't Shoot the Messenger"
    desc: "Messengers get a +2 circumstance bonus to Diplomacy checks to convince another creature not to blame them for any news they deliver."
  - name: "Road Runner"
    desc: "Messengers can use Society in place of Survival to Sense Direction when they're on a road."
  - name: "Items"
    desc: "Dagger, satchel of mail, Sling (10 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +10; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 (Agile, Finesse, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +8 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +8 (range increment 50 feet, Propulsive) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Express Messenger"
    desc: "Allies traveling with the messenger gain a +5-foot circumstance bonus to travel Speed, to a maximum of the messenger's travel Speed. If they use the Hustle activity, they can Hustle for a minimum of 1 hour instead of the usual amount."
  - name: "Special Delivery"
    desc: "⬺ The messenger Interacts to take an item of light Bulk or less held by a willing ally within reach, Strides, then delivers the item to a willing ally in reach at their new location."
sourcebook: "_NPC Core_, page 70."
```

```encounter-table
name: Messenger
creatures:
  - 1: Messenger
```
