---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Magma Scorpion"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/large
statblock: inline
name: "Magma Scorpion"
level: 8
source: "Monster Core 2"
aon_id: "creature-4389"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4389"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Magma Scorpion"
level: "Creature 8"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, smoke vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16"
abilityMods: [6, 3, 5, -4, 4, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The magma scorpion ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +14; __Will__: +16"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
speed: "40 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+9 bludgeoning plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]] and Grab"
  - name: "Melee"
    desc: "⬻ tail sting +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+9 piercing plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]] and magma scorpion venom"
  - name: "Ranged"
    desc: "⬻ magma spit +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], range increment 40 feet) __Damage__ 1d6+9 fire plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
abilities_bot:
  - name: "Magma Scorpion Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/injury|injury]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 fire damage (1 round) and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1"
  - name: "Stage 2"
    desc: "3d6 fire damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core 2_, page 149."
```

```encounter-table
name: Magma Scorpion
creatures:
  - 1: Magma Scorpion
```
