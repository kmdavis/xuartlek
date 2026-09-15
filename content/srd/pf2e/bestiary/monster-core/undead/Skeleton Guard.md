---
noteType: pf2eMonster
aliases: "Skeleton Guard"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Skeleton Guard"
level: -1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3193"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Skeleton Guard"
level: "Creature -1"
size: "Medium"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 2
perception:
  - name: "Perception"
    desc: "+2; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +3"
abilityMods: [2, 4, 0, -5, 0, 0]
abilities_top:
  - name: "Items"
    desc: "Scimitar, Shortbow (20 arrows)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +2; __Ref__: +8; __Will__: +2"
hp: 4
health:
  - name: "HP"
    desc: "4 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 5, piercing 5, slashing 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d6+2 slashing"
  - name: "Melee"
    desc: "⬻ claw +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 1d4+2 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6 piercing"
sourcebook: "_Monster Core_, page 312."
```

```encounter-table
name: Skeleton Guard
creatures:
  - 1: Skeleton Guard
```
