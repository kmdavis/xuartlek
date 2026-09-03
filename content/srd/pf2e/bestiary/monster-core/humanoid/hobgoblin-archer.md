---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hobgoblin Archer"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/hobgoblin
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Hobgoblin Archer"
level: 4
source: "Monster Core"
aon_id: "creature-3054"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3054"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hobgoblin Archer"
level: "Creature 4"
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +8, Stealth +10"
abilityMods: [2, 4, 2, 0, 2, -1]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Scale Mail, Shortsword"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +10; __Ref__: +12; __Will__: +8"
hp: 50
health:
  - name: "HP"
    desc: "50"
abilities_mid:
  - name: "Formation"
    desc: "When they're adjacent to at least two other allies, the hobgoblin archer gains a +1 circumstance bonus to AC and saving throws. This bonus increases to +2 to Reflex saves against area effects."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +12 (Agile, versatile S) __Damage__ 1d6+4 piercing"
  - name: "Ranged"
    desc: "⬻ crossbow +14 (range increment 120 feet, reload 1) __Damage__ 1d8+2 piercing plus crossbow precision"
abilities_bot:
  - name: "Crossbow Precision"
    desc: "The first time the archer hits with a crossbow attack in a round, it deals 1d8 extra precision damage."
  - name: "Perfect Aim"
    desc: "The hobgoblin archer ignores the concealed condition. Their targets don't benefit from lesser cover, and they reduce the AC bonus from standard cover by 2 against the hobgoblin archer's attack."
  - name: "Running Reload"
    desc: "⬻ The archer Strides, Steps, or Sneaks, then Interacts to reload."
sourcebook: "_Monster Core_, page 199."
```

```encounter-table
name: Hobgoblin Archer
creatures:
  - 1: Hobgoblin Archer
```
