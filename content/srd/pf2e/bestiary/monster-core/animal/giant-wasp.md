---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Wasp"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Wasp"
level: 3
source: "Monster Core"
aon_id: "creature-3233"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3233"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Wasp"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9"
abilityMods: [4, 4, 4, -5, 1, 1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +11; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stinger +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) __Damage__ 1d12+4 piercing plus giant wasp venom"
abilities_bot:
  - name: "Implant Eggs"
    desc: "⬻ The giant wasp lays eggs in an adjacent creature that is [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] or [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], exposing it to wasp larva disease."
  - name: "Giant Wasp Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds; Stage 1 no effect (1 round)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 2]] (1 round)"
  - name: "Stage 3"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] (1 round)"
  - name: "Wasp Larva"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1d6 days)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1d4 days)"
  - name: "Stage 3"
    desc: "5d6 damage, larva emerges (disease ends)"
sourcebook: "_Monster Core_, page 343."
```

```encounter-table
name: Giant Wasp
creatures:
  - 1: Giant Wasp
```
