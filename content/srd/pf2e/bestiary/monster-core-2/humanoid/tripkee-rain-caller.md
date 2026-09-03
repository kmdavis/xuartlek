---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tripkee Rain-Caller"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Rain-Caller"
level: 4
source: "Monster Core 2"
aon_id: "creature-4590"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4590"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tripkee Rain-Caller"
level: "Creature 4"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "Common, Tripkee"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +8, Jungle Lore +10, Nature +12, Stealth +10, Survival +12"
abilityMods: [1, 3, 2, 1, 5, 0]
abilities_top:
  - name: "Items"
    desc: "Dart (4), Staff"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +11; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet, climb 20 feet; jungle passage"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 (two-hand d8) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +12 (Agile, thrown 20 feet) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Prepared Primal Spells"
    desc: "DC 21, attack +14 - __Cantrips (2nd)__ Electric Arc, Guidance, Know the Way, Stabilize - __1st__ Gust of Wind, Hydraulic Push, Thunderstrike - __2nd__ Mist, Summon Elemental (water only), Water Walk"
  - name: "Druid Focus Spell"
    desc: "DC 21, 1 Focus Point - __2nd__ Tempest Surge"
  - name: "Jungle Passage"
    desc: "Tripkees ignore difficult terrain in forests and jungles."
sourcebook: "_Monster Core 2_, page 327."
```

```encounter-table
name: Tripkee Rain-Caller
creatures:
  - 1: Tripkee Rain-Caller
```
