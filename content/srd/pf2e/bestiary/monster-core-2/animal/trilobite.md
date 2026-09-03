---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Trilobite"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/tiny
statblock: inline
name: "Trilobite"
level: -1
source: "Monster Core 2"
aon_id: "creature-4587"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4587"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Trilobite"
level: "Creature -1"
size: "Tiny"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, wavesense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +4, Stealth +5, Survival +4"
abilityMods: [1, 3, 2, -5, 2, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +4; __Ref__: +7; __Will__: +4"
hp: 7
health:
  - name: "HP"
    desc: "7"
abilities_mid:
  - name: "Curl Up"
    desc: "⬲"
  - name: "Trigger"
    desc: "The trilobite takes damage"
  - name: "Effect"
    desc: "The trilobite gains a +2 circumstance bonus to AC until the start of its next turn."
speed: "swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ gnathobase +7 (Agile, finesse) __Damage__ 1d4+1 slashing"
abilities_bot:
  - name: "Quick Escape"
    desc: "⬺ The trilobite Swims up to double its Speed and attempts to Hide."
sourcebook: "_Monster Core 2_, page 326."
```

```encounter-table
name: Trilobite
creatures:
  - 1: Trilobite
```
