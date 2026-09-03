---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Dragonfly"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Dragonfly"
level: 4
source: "Monster Core 2"
aon_id: "creature-4372"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4372"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Dragonfly"
level: "Creature 4"
size: "Medium"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, wavesense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +10, Stealth +12"
abilityMods: [4, 4, 2, -5, 3, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +14; __Will__: +9"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "20 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +14 __Damage__ 1d12+7 piercing plus Grab"
abilities_bot:
  - name: "Clutch"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant dragonfly has a Medium or smaller creature grabbed in its mandibles"
  - name: "Effect"
    desc: "The dragonfly tries to transfer the grabbed creature to be clutched by its legs. The giant dragonfly attempts an Athletics check against the creature's Reflex DC. On a success, it transfers the creature (which remains grabbed) to its legs, freeing its mandibles to attack. The dragonfly can have only one creature clutched at a time."
  - name: "Snatch"
    desc: "The giant dragonfly can Fly at half Speed while it has a creature grabbed or restrained by Clutch, carrying that creature along with it."
  - name: "Swoop"
    desc: "⬺ The giant dragonfly Flies up to its Speed and makes one mandible Strike at any point during that movement."
sourcebook: "_Monster Core 2_, page 138."
```

```encounter-table
name: Giant Dragonfly
creatures:
  - 1: Giant Dragonfly
```
