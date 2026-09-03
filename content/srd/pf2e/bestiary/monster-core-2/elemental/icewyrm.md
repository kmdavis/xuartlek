---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Icewyrm"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Icewyrm"
level: 10
source: "Monster Core 2"
aon_id: "creature-4393"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4393"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Icewyrm"
level: "Creature 10"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Cold"
trait_03: "Elemental"
trait_04: "Water"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21"
abilityMods: [7, 7, 5, -1, 5, 3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +20; __Ref__: +21; __Will__: +17"
hp: 185
health:
  - name: "HP"
    desc: "185; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Explosion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]) When the icewyrm dies, it explodes, dealing 8d6 cold damage to each creature in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 27 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
speed: "25 feet, ice burrow 20 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d12+13 piercing"
  - name: "Melee"
    desc: "⬻ tail +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d6+13 slashing plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent cold]]"
  - name: "Ranged"
    desc: "⬻ ice shard +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], range increment 60 feet) __Damage__ 1d6+13 piercing plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent cold]]"
abilities_bot:
  - name: "Breathe Ice Shards"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The icewyrm breathes a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] of freezing shards of razor-sharp ice, dealing 3d12 cold damage and 3d12 piercing damage to every creature in the line (DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The icewyrm can't use Breathe Ice Shards again for 1d4 rounds."
  - name: "Ice Burrow"
    desc: "The icewyrm can Burrow through ice or snow with a Speed of 20 feet. It moves at its full burrow Speed, leaving no tunnels or signs of its passing."
sourcebook: "_Monster Core 2_, page 151."
```

```encounter-table
name: Icewyrm
creatures:
  - 1: Icewyrm
```
