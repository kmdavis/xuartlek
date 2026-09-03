---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ogre Warrior"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Ogre Warrior"
level: 3
source: "Monster Core"
aon_id: "creature-3118"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3118"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ogre Warrior"
level: "Creature 3"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +12, Intimidation +9"
abilityMods: [5, -1, 4, -2, 0, -2]
abilities_top:
  - name: "Items"
    desc: "Hide Armor, javelins (6), Ogre Hook"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +6; __Will__: +5"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ogre hook +12 (deadly d10, reach 10 feet, Trip) __Damage__ 1d10+7 piercing"
  - name: "Ranged"
    desc: "⬻ javelin +6 (thrown 30 feet) __Damage__ 1d6+7 piercing"
sourcebook: "_Monster Core_, page 250."
```

```encounter-table
name: Ogre Warrior
creatures:
  - 1: Ogre Warrior
```
