---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Martial Student"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Martial Student"
level: 3
source: "NPC Core"
aon_id: "creature-3500"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3500"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Martial Student"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10"
abilityMods: [4, 3, 2, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "handwraps"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +6"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Fancy Footwork"
    desc: "⬻ The martial student Steps and Strides in any order."
  - name: "Flurry of Blows"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The martial student makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses."
  - name: "Powerful Fists"
    desc: "The martial student's fist Strikes don't take penalties when making lethal attacks."
sourcebook: "_NPC Core_, page 72."
```

```encounter-table
name: Martial Student
creatures:
  - 1: Martial Student
```
