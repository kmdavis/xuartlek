---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Terror Shrike"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Terror Shrike"
level: 4
source: "Monster Core 2"
aon_id: "creature-4579"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4579"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Terror Shrike"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12"
abilityMods: [5, 4, 3, -4, 1, 0]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +12; __Will__: +7"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+5 piercing plus tearing clutch"
  - name: "Melee"
    desc: "⬻ talon +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+5 piercing plus Knockdown"
abilities_bot:
  - name: "Sprint"
    desc: "Frequency__ once per minute__ ⬺"
  - name: "Effect"
    desc: "The terror shrike Strides three times in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]]."
  - name: "Tearing Clutch"
    desc: "The terror shrike's powerful beak can tear through flesh. On a successful beak Strike, the target takes 1 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]. This bleed damage increases to 1d8 on a critical hit."
sourcebook: "_Monster Core 2_, page 318."
```

```encounter-table
name: Terror Shrike
creatures:
  - 1: Terror Shrike
```
