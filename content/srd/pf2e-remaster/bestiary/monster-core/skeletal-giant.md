---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeletal Giant"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Skeletal Giant"
level: 3
source: "Monster Core"
aon_id: "creature-3196"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3196"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Skeletal Giant"
level: "Creature 3"
size: "Large"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +12, Intimidation +9"
abilityMods: [5, 1, 3, -5, 0, 2]
abilities_top:
  - name: "Items"
    desc: "Glaive, Half Plate"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +8; __Will__: +7"
hp: 50
health:
  - name: "HP"
    desc: "50 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 5, electricity 5, fire 5, piercing 5, slashing 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ glaive +12 (deadly d8, Forceful, reach 15 feet) __Damage__ 1d8+7 slashing"
  - name: "Melee"
    desc: "⬻ horns +12 (Agile) __Damage__ 1d10+5 piercing"
abilities_bot:
  - name: "Broad Swipe"
    desc: "⬺ The giant makes two Strikes with its glaive against two adjacent foes, both of whom are within its reach. Both attacks count toward the giant's multiple attack penalty, but the penalty doesn't increase until after both attacks."
  - name: "Terrifying Charge"
    desc: "⬺ The giant Strides and makes a horns Strike with a +4 circumstance bonus to damage. If the strike hits, the giant attempts to Demoralize the target."
sourcebook: "_Monster Core_, page 313."
```

```encounter-table
name: Skeletal Giant
creatures:
  - 1: Skeletal Giant
```
