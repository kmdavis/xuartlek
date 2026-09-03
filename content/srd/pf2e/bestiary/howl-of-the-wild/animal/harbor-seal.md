---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Harbor Seal"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Harbor Seal"
level: 2
source: "Howl of the Wild"
aon_id: "creature-3305"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3305"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Harbor Seal"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision, scent (imprecise) 20 feet, whisker sense 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [4, 3, 3, -4, 1, 3]
abilities_top:
  - name: "Deep Breath"
    desc: "A harbor seal can hold its breath for 30 minutes."
  - name: "Whisker Sense"
    desc: "A harbor seal can use its whiskers to sense vibrations as a precise sense at the listed range, but only underwater."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +11; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "15 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 1d8+4 piercing plus Grab"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 40 feet"
  - name: "Aquatic Feast"
    desc: "⬻"
  - name: "Requirements"
    desc: "The harbor seal has a Medium or smaller creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in its jaws"
  - name: "Effect"
    desc: "The harbor seal Swims up to 10 feet, carrying its grabbed creature along with it dealing 1d8 slashing damage (DC 18 basic Fortitude save)."
sourcebook: "_Howl of the Wild_, page 178."
```

```encounter-table
name: Harbor Seal
creatures:
  - 1: Harbor Seal
```
