---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeletal Hulk"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Skeletal Hulk"
level: 7
source: "Monster Core"
aon_id: "creature-3197"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3197"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Skeletal Hulk"
level: "Creature 7"
size: "Huge"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15"
abilityMods: [7, 2, 4, -5, 2, 2]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +15; __Will__: +13"
hp: 105
health:
  - name: "HP"
    desc: "105 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5, piercing 5, slashing 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+11 slashing"
abilities_bot:
  - name: "Broad Swipe"
    desc: "⬺ As skeletal giant, but with its claw Strike."
  - name: "Massive Rush"
    desc: "⬺ The hulk Strides and makes a claw Strike with a +4 circumstance bonus to damage. If the Strike hits, the hulk automatically pushes the target 10 feet."
sourcebook: "_Monster Core_, page 313."
```

```encounter-table
name: Skeletal Hulk
creatures:
  - 1: Skeletal Hulk
```
