---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Maggot"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Maggot"
level: 0
source: "Monster Core 2"
aon_id: "creature-4401"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4401"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Maggot"
level: "Creature 0"
size: "Medium"
trait_01: "Animal"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; no vision, tremorsense 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6"
abilityMods: [2, -1, 3, -5, 1, -5]
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +9; __Ref__: +3; __Will__: +3"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Regurgitation"
    desc: "⬲"
  - name: "Trigger"
    desc: "The giant maggot takes damage"
  - name: "Effect"
    desc: "The giant maggot regurgitates its rancid, foul meal. All creatures in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must succeed at a DC 16 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (or sickened 2 on a critical failure). The giant maggot can't use Regurgitation again until it spends at least an hour feeding on a corpse."
speed: "10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +6 __Damage__ 1d8+2 piercing plus Grab"
abilities_bot:
  - name: "Gnaw Flesh"
    desc: "⬻"
  - name: "Requirements"
    desc: "The giant maggot has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] a creature"
  - name: "Effect"
    desc: "The giant maggot deals 1d8+2 slashing damage to the grabbed creature as it chews the creature's flesh (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
sourcebook: "_Monster Core 2_, page 157."
```

```encounter-table
name: Giant Maggot
creatures:
  - 1: Giant Maggot
```
