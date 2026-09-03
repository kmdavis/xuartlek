---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Whipping Willow"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/medium
statblock: inline
name: "Whipping Willow"
level: 4
source: "Rage of Elements"
aon_id: "creature-2673"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2673"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Whipping Willow"
level: "Creature 4"
size: "Medium"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "Arboreal, Muan"
skills:
  - name: "Skills"
    desc: "Athletics +12"
abilityMods: [2, 5, 2, 0, 1, 2]
abilities_top:
  - name: "Grounded"
    desc: "When saving against an effect attempting to knock them prone, a whipping willow achieves one degree of success better than what they rolled. Additionally, the willow doesn't fall prone on a critical failure to Trip an opponent."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +8; __Will__: +14"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ axes 5, fire 5"
speed: "30 feet, climb 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +11 (Finesse, reach 15 feet, Trip) __Damage__ 2d8+5 bludgeoning plus strangling vines"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d4+5 bludgeoning, DC 21"
  - name: "Strangling Vines"
    desc: "When a whipping willow hits a creature with their whip Strike, they can choose to Grab and begin strangling the creature. The target is suffocating and can't speak as long as it's strangled."
  - name: "Unseating Sweep"
    desc: "⬺ The whipping willow attempts to Trip all creatures within a 15-foot cone, making a single Athletics check against all targets' Reflex DCs."
sourcebook: "_Rage of Elements_, page 207."
```

```encounter-table
name: Whipping Willow
creatures:
  - 1: Whipping Willow
```
