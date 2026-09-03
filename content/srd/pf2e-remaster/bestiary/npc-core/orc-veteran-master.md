---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Veteran Master"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Veteran Master"
level: 10
source: "NPC Core"
aon_id: "creature-3666"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3666"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Orc Veteran Master"
level: "Creature 10"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +23, Diplomacy +15, Intimidation +20, Warfare Lore +18, Stealth +20"
abilityMods: [5, 4, 3, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 striking bo staff_, _+1 breastplate_, _+1 striking composite longbow_ (20 arrows)"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +19; __Ref__: +20; __Will__: +18"
hp: 175
health:
  - name: "HP"
    desc: "175"
abilities_mid:
  - name: "Fly Through Battle"
    desc: "The veteran master gains an additional reaction each round that can be used only to make a Reactive Pursuit."
  - name: "Reactive Pursuit"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy within reach attempts to move away"
  - name: "Effect"
    desc: "The veteran master Strides up to their Speed, following the enemy and keeping it in reach throughout its movement until it stops moving or the master has moved their full Speed."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bo staff_ +24 (Magical, Parry, Reach, Trip) __Damage__ 2d8+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, Nonlethal, Unarmed) __Damage__ 2d4+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +23 (deadly d10, Magical, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Staff Swipe"
    desc: "⬺ The veteran master extends their reach to smash multiple creatures with their bo. They attempt a bo staff Strike against each enemy in a 15-foot cone. This counts as two attacks toward their multiple attack penalty, but the penalty doesn't increase until after all the attacks."
  - name: "Reshape the Battle"
    desc: "⬻ The veteran master attempts a bo staff Strike. If it hits a creature of the master's size or smaller, the master can automatically Reposition it to any space within the bo staff's reach."
sourcebook: "_NPC Core_, page 208."
```

```encounter-table
name: Orc Veteran Master
creatures:
  - 1: Orc Veteran Master
```
