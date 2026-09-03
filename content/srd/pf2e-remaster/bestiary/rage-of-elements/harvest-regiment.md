---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Harvest Regiment"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Harvest Regiment"
level: 8
source: "Rage of Elements"
aon_id: "creature-2683"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2683"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Harvest Regiment"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Troop"
trait_04: "Wood"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision"
languages: "Fey, Muan"
skills:
  - name: "Skills"
    desc: "Athletics +18, Survival +17"
abilityMods: [6, 1, 3, -1, 3, -2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +14; __Will__: +16"
hp: 135
health:
  - name: "HP"
    desc: "135 (16 squares); __Weaknesses__ area damage 8, fire 8, splash damage 8"
abilities_mid:
  - name: "Juice Shower"
    desc: "When a harvest regiment is critically hit or critically fails a save against a damaging effect, sticky fruit juices splash out. This affects all creatures in a 5-foot emanation. A splashed creature takes a –10-foot status penalty to its Speeds and everything is concealed to it. A creature can Interact to clear off the juice."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Raise Shells"
    desc: "⬻ The troop raises fragments of their shells shaped like shields to gain a +2 circumstance bonus to AC until the start of their next turn."
  - name: "Seed Volley"
    desc: "⬺ The harvest regiment spits an orderly volley of hard seeds drawn from within their bodies. This volley is a 10-foot burst within 120 feet that deals 2d10 bludgeoning damage (DC 23 basic Reflex save). When the harvest regiment is reduced to 8 or fewer squares, this area decreases to a 5-foot burst."
  - name: "Shell Smash"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The harvest regiment engages in a coordinated melee attack against each enemy in a 5-foot emanation, with a DC 23 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+3 bludgeoning damage ⬺ 2d8+9 bludgeoning damage ⬽ 2d8+12 bludgeoning damage Out of Season The harvest regiment stat block represents the troop when it's harvested at exactly the right time. A “green,” or unripe, regiment might be pressed into service before it's ready, and an overripe version could fall off the tree partially rotten. Both of these use the weak adjustments and have 126 HP with thresholds of 84 and 42 HP. A green regiment loses juice shower and weakness to fire, and a rotten regiment's juice shower makes the creature sickened 1 if it fails a DC 25 Fortitude save instead of the normal effect."
sourcebook: "_Rage of Elements_, page 214."
```

```encounter-table
name: Harvest Regiment
creatures:
  - 1: Harvest Regiment
```
