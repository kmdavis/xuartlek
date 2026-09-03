---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Twigjack"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/tiny
statblock: inline
name: "Twigjack"
level: 3
source: "Monster Core"
aon_id: "creature-3222"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3222"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Twigjack"
level: "Creature 3"
size: "Tiny"
trait_01: "Fey"
trait_02: "Plant"
trait_03: "Wood"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +9, Nature +7, Stealth +11"
abilityMods: [2, 4, 2, 0, 2, 1]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +11; __Will__: +7"
hp: 50
health:
  - name: "HP"
    desc: "50; __Weaknesses__ axes 5, fire 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +11 (Agile, Finesse, reach 0 feet) __Damage__ 1d10+4 slashing"
  - name: "Ranged"
    desc: "⬻ splinter +11 (deadly 1d6, range increment 30 feet) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Bramble Jump"
    desc: "⬽ (Plant, Primal, Teleportation, Wood)"
  - name: "Requirements"
    desc: "The twigjack is in undergrowth"
  - name: "Effect"
    desc: "The twigjack scrambles into the undergrowth and instantly teleports to a square of undergrowth within 60 feet. This movement doesn't trigger reactions."
  - name: "Splinter Spray"
    desc: "⬺ The twigjack sprays a barrage of splinters and brambles from its body in a 15-foot cone, dealing 4d6 piercing damage (DC 20 basic Reflex save). It can't use Splinter Spray again for 1d4 rounds."
sourcebook: "_Monster Core_, page 332."
```

```encounter-table
name: Twigjack
creatures:
  - 1: Twigjack
```
