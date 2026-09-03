---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Athamaru Hunter"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/athamaru
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/locathah
statblock: inline
name: "Athamaru Hunter"
level: 3
source: "Monster Core"
aon_id: "creature-2837"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2837"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Athamaru Hunter"
level: "Creature 3"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Athamaru"
trait_03: "Humanoid"
trait_04: "Locathah"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision"
languages: "Common, Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +11, Diplomacy +5, Nature +7, Stealth +8, Survival +7"
abilityMods: [4, 3, 0, 1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Crossbow (12 fan bolts), Longspear, Scale Mail"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +7; __Ref__: +10; __Will__: +9"
hp: 38
health:
  - name: "HP"
    desc: "38"
speed: "10 feet, swim 40 feet; smooth swimmer"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +11 (reach 10 feet) __Damage__ 1d8+4 piercing"
  - name: "Melee"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing plus fan bolt"
abilities_bot:
  - name: "Cooperative Hunting"
    desc: "After the hunter attempts a Strike at a Large or larger target (regardless of success or failure), the next Strike one of the hunter's allies makes against the same target gains a +2 circumstance bonus to the attack roll."
  - name: "Fan Bolt"
    desc: "The hunter prepares their hooked crossbow bolts with carefully woven seaweed. On a successful crossbow Strike, the bolt embeds and the seaweed fan deploys. The target takes a –10-foot status penalty to its swim Speed. A creature can Interact to attempt a DC Athletics check, removing the bolt on a success."
  - name: "Hunt Prey"
    desc: "⬻ (Concentrate) The athamaru hunter designates a single creature they can see and hear, or one they're Tracking, as their prey. The hunter gains a +2 circumstance bonus to Perception checks to Seek the prey and to Survival checks to Track the prey. The first time the athamaru hits their designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the hunter uses Hunt Prey again."
  - name: "Pack Attack"
    desc: "The hunter's Strikes deal an additional 1d8 damage to creatures within reach of at least two of the hunter's allies."
  - name: "Smooth Swimmer"
    desc: "The athamaru hunter ignores difficult terrain caused by aquatic terrain features."
sourcebook: "_Monster Core_, page 30."
```

```encounter-table
name: Athamaru Hunter
creatures:
  - 1: Athamaru Hunter
```
