---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Striding Fire"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Striding Fire"
level: 6
source: "Monster Core 2"
aon_id: "creature-4388"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4388"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Striding Fire"
level: "Creature 6"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12"
abilityMods: [2, 5, 3, 0, 4, 1]
abilities_top:
  - name: "Smoke Vision"
    desc: "The striding fire ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +17; __Will__: +14"
hp: 115
health:
  - name: "HP"
    desc: "115; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d8+5 bludgeoning plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
abilities_bot:
  - name: "Burning Rush"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The striding fire stretches out its legs to an impossible length, propelling it forward. The striding fire Strides up to double its Speed in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]]. Its movement during this Stride doesn't trigger reactions. Any creature the striding fire was adjacent to at any point during this Stride must attempt a DC 24 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. If it critically fails, it's knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] by a wave of heated air. The striding fire can't use Burning Rush for 1d4 rounds."
sourcebook: "_Monster Core 2_, page 149."
```

```encounter-table
name: Striding Fire
creatures:
  - 1: Striding Fire
```
