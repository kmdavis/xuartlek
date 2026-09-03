---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tracker"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tracker"
level: 3
source: "NPC Core"
aon_id: "creature-3471"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3471"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tracker"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Forest Lore +5, Nature +11, Stealth +9, Survival +13"
abilityMods: [2, 4, 2, 0, 4, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using Survival to Subsist, if the tracker rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and eight additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Master Tracker"
    desc: "The tracker can Track while moving at full speed."
  - name: "Items"
    desc: "Composite Longbow (60 arrows), Dagger, Leather Armor"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +11; __Will__: +9"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +11 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +11 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Ranged"
    desc: "⬻ composite longbow +11 (deadly 1d10, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "On the Hunt"
    desc: "⬻ (Concentrate) The tracker designates one creature they're observing or tracking as their prey. The tracker gains a +2 circumstance bonus to Perception checks to Seek the prey and to Survival checks to Track the prey. The first time the tracker hits the designated prey in a round, they deal an additional 1d4 precision damage. These effects last until the tracker uses On the Hunt again."
sourcebook: "_NPC Core_, page 54."
```

```encounter-table
name: Tracker
creatures:
  - 1: Tracker
```
