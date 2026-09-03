---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Icicle Snake"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/small
statblock: inline
name: "Icicle Snake"
level: 2
source: "Monster Core 2"
aon_id: "creature-4390"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4390"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Icicle Snake"
level: "Creature 2"
size: "Small"
trait_01: "Cold"
trait_02: "Elemental"
trait_03: "Water"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [1, 3, 2, -4, 1, 0]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +9; __Will__: +5"
hp: 35
health:
  - name: "HP"
    desc: "35; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
speed: "25 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 piercing plus 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent cold]]"
abilities_bot:
  - name: "Icicle"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until the next time it acts, the icicle snake appears to be an unassuming icicle. It has an automatic result of 27 on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as an icicle."
sourcebook: "_Monster Core 2_, page 150."
```

```encounter-table
name: Icicle Snake
creatures:
  - 1: Icicle Snake
```
