---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bottlenose Dolphin"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Bottlenose Dolphin"
level: 0
source: "Monster Core"
aon_id: "creature-2926"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2926"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bottlenose Dolphin"
level: "Creature 0"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; aquatic echolocation 120 feet, low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6"
abilityMods: [2, 3, 2, -4, 3, 0]
abilities_top:
  - name: "Aquatic Echolocation"
    desc: "A bottlenose dolphin can use its hearing as a precise sense at the listed range, but only underwater."
  - name: "Deep Breath"
    desc: "A bottlenose dolphin can hold its breath for 2 hours."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +7; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16"
speed: "swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ snout +6 __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +6 __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Ramming Speed"
    desc: "⬺ The bottlenose dolphin Swims twice and then makes a snout Strike. As long as it moved at least 20 feet, it gains a +1 circumstance bonus to its attack roll. A Large or smaller creature hit by this attack must succeed at a DC 16 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round."
sourcebook: "_Monster Core_, page 103."
```

```encounter-table
name: Bottlenose Dolphin
creatures:
  - 1: Bottlenose Dolphin
```
