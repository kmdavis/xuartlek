---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Electric Eel"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/small
statblock: inline
name: "Electric Eel"
level: 1
source: "Monster Core"
aon_id: "creature-2970"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2970"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Electric Eel"
level: "Creature 1"
size: "Small"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [1, 2, 2, -5, 1, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +7; __Will__: +4"
hp: 18
health:
  - name: "HP"
    desc: "18; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 7"
speed: "5 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +6 __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ tail +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+1 bludgeoning plus 1d4 electricity and stunning shock"
abilities_bot:
  - name: "Stunning Shock"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]]) A creature critically hit by the electric eel's tail must attempt a DC 17 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]."
  - name: "Failure"
    desc: "The creature is stunned 2."
  - name: "Critical Failure"
    desc: "The creature is stunned 3. Electric Eel Hide Hide harvested from electric eels can be used to create armor or items that provide protection from electricity."
sourcebook: "_Monster Core_, page 138."
```

```encounter-table
name: Electric Eel
creatures:
  - 1: Electric Eel
```
