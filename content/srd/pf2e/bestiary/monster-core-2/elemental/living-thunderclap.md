---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Thunderclap"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/medium
statblock: inline
name: "Living Thunderclap"
level: 4
source: "Monster Core 2"
aon_id: "creature-4379"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4379"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Living Thunderclap"
level: "Creature 4"
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [3, 4, 2, -3, 1, 0]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +12; __Will__: +9"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]]"
speed: "fly 50 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ gust +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d6+6 bludgeoning plus Push"
  - name: "Ranged"
    desc: "⬻ lightning bolt +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], range increment 50 feet) __Damage__ 2d12 electricity"
abilities_bot:
  - name: "Swiftness"
    desc: "The living thunderclap doesn't trigger reactions when it moves."
  - name: "Thunderbolt"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/monster-core/oni|sonic]]) The living thunderclap emits a bolt of lightning that crashes with deafening thunder. The living thunderclap makes a lightning bolt Strike that deals 1d12 electricity damage. If it hits, the target and any creatures within a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] around the target take 2d6 sonic damage (DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save). Any creature that fails its save is also [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]] for 1d4 rounds."
sourcebook: "_Monster Core 2_, page 144."
```

```encounter-table
name: Living Thunderclap
creatures:
  - 1: Living Thunderclap
```
