---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Terror Bird"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Terror Bird"
level: 2
source: "Monster Core 2"
aon_id: "creature-4578"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4578"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Terror Bird"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8"
abilityMods: [4, 3, 3, -4, 0, 0]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +9; __Will__: +4"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+4 piercing plus tearing clutch"
  - name: "Melee"
    desc: "⬻ talon +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+4 piercing plus Knockdown"
abilities_bot:
  - name: "Sprint"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The terror bird [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] three times in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]]."
  - name: "Tearing Clutch"
    desc: "The terror bird's powerful beak can tear through flesh. On a successful beak Strike, the target takes 1 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]. This bleed damage increases to 1d4 on a critical hit."
sourcebook: "_Monster Core 2_, page 318."
```

```encounter-table
name: Terror Bird
creatures:
  - 1: Terror Bird
```
