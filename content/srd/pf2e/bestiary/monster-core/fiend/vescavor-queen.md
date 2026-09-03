---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vescavor Queen"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Vescavor Queen"
level: 9
source: "Monster Core"
aon_id: "creature-3228"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3228"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vescavor Queen"
level: "Creature 9"
size: "Large"
trait_01: "Fiend"
trait_02: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Chthonian"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +18, Religion +16, Stealth +20, Survival +16"
abilityMods: [6, 5, 5, 1, 3, 2]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +19; __Will__: +15"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ acid 10; __Weaknesses__ cold iron 10, holy 10"
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (Magical, Unholy) __Damage__ 1d10+13 piercing plus 1d10 acid"
  - name: "Melee"
    desc: "⬻ claw +20 (Agile, Magical, reach 10 feet, Unholy) __Damage__ 2d10+8 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +20 (Magical, reach 15 feet, Unholy) __Damage__ 2d4 piercing plus 2d10 acid"
  - name: "Ranged"
    desc: "⬻ spit +19 (Acid, Magical, range increment 30 feet) __Damage__ 2d8 acid plus rage pheromones"
abilities_bot:
  - name: "Chaotic Spawning"
    desc: "⬽ The vescavor queen strengthens her swarms. All vescavor swarms within 100 feet become Huge and quickened for 1 minute. Vescavor swarms can only use the extra action each round for the Ravenous Bites action."
  - name: "Feeding Time"
    desc: "⬻ The vescavor queen causes any number of vescavor swarms within 100 feet to immediately use their reaction to perform the Ravenous Bites action."
  - name: "Opportune Snack"
    desc: "⬻ The vescavor queen pulls a creature it has grabbed or restrained into a space adjacent to it and makes a jaws Strike with a +2 circumstance bonus."
  - name: "Rage Pheromones"
    desc: "If the vescavor queen's spit Strike damages a creature, it takes a –2 status penalty to all saving throws imposed by vescavor swarms for 1 minute."
sourcebook: "_Monster Core_, page 339."
```

```encounter-table
name: Vescavor Queen
creatures:
  - 1: Vescavor Queen
```
