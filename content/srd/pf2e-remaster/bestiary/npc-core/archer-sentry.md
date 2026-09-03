---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Archer Sentry"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Archer Sentry"
level: 2
source: "NPC Core"
aon_id: "creature-3552"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3552"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Archer Sentry"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +6, Intimidation +4, Legal Lore +4"
abilityMods: [2, 4, 1, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (100 arrows), Leather Armor, Shortsword, Signal Whistle"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 (Agile, Finesse, versatile S) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite longbow +10 (deadly d10, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Sentry's Aim"
    desc: "⬺ (Concentrate) The archer sentry aims carefully and fires. They make a ranged weapon Strike with a +1 circumstance bonus. The Strike ignores the concealed condition, lesser cover, and standard cover, and reduces greater cover to standard cover."
sourcebook: "_NPC Core_, page 111."
```

```encounter-table
name: Archer Sentry
creatures:
  - 1: Archer Sentry
```
