---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spark Moth"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/tiny
statblock: inline
name: "Spark Moth"
level: 2
source: "Monster Core 2"
aon_id: "creature-4378"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4378"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Spark Moth"
level: "Creature 2"
size: "Tiny"
trait_01: "Air"
trait_02: "Elemental"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [0, 3, 1, -4, 1, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +11; __Will__: +7"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "5 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wing +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d4+5 electricity"
abilities_bot:
  - name: "Arc Lightning"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The spark moth transforms into lightning that arcs to a large piece of metal within 100 feet, such as a suit of metal armor or metal weapon. The elemental then returns to its normal form in a space adjacent to the metal. This movement doesn't trigger reactions."
sourcebook: "_Monster Core 2_, page 144."
```

```encounter-table
name: Spark Moth
creatures:
  - 1: Spark Moth
```
