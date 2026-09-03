---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Girtablilu Sentry"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/girtablilu
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Girtablilu Sentry"
level: 8
source: "Monster Core 2"
aon_id: "creature-4413"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4413"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Girtablilu Sentry"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Girtablilu"
trait_03: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, tremorsense (imprecise) 60 feet"
languages: "Common, Girtablilu"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +17, Religion +16, Survival +17"
abilityMods: [6, 4, 6, 3, 4, 3]
abilities_top:
  - name: "Items"
    desc: "Hide Armor, _+1 striking longspear_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +16; __Will__: +12"
hp: 160
health:
  - name: "HP"
    desc: "160"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +21 (Magical, reach 15 feet) __Damage__ 2d8+9 piercing"
  - name: "Melee"
    desc: "⬻ pincer +20 (Agile, unarmed) __Damage__ 2d8+9 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +20 (reach 10 feet, unarmed) __Damage__ 2d6+9 piercing plus girtablilu venom"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d8+6 bludgeoning, DC 24"
  - name: "Desert Passage"
    desc: "A girtablilu ignores natural difficult terrain in the desert."
  - name: "Girtablilu Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 3"
    desc: "3d6 poison damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core 2_, page 166."
```

```encounter-table
name: Girtablilu Sentry
creatures:
  - 1: Girtablilu Sentry
```
