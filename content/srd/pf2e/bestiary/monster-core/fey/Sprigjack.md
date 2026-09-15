---
noteType: pf2eMonster
aliases: "Sprigjack"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/tiny
statblock: inline
name: "Sprigjack"
level: -1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3221"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sprigjack"
level: "Creature -1"
size: "Tiny"
trait_01: "Fey"
trait_02: "Plant"
trait_03: "Wood"
modifier: 5
perception:
  - name: "Perception"
    desc: "+5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +3, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +5"
abilityMods: [1, 3, 2, -1, 1, 1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +7; __Will__: +3"
hp: 10
health:
  - name: "HP"
    desc: "10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/Weapon Groups#Axe|axes]] 2, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 2"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 0 feet]]) __Damage__ 1d4+1 slashing"
  - name: "Ranged"
    desc: "⬻ splinter +7 (range increment 30 feet) __Damage__ 1d4 piercing"
abilities_bot:
  - name: "Bramble Jump"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|Teleportation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Wood|Wood]])"
  - name: "Requirements"
    desc: "The twigjack is in undergrowth"
  - name: "Effect"
    desc: "The twigjack scrambles into the undergrowth and instantly teleports to a square of undergrowth within 60 feet. This movement doesn't trigger reactions."
sourcebook: "_Monster Core_, page 332."
```

```encounter-table
name: Sprigjack
creatures:
  - 1: Sprigjack
```
