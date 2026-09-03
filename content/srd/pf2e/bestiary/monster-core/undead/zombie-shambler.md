---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zombie Shambler"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/medium
statblock: inline
name: "Zombie Shambler"
level: -1
source: "Monster Core"
aon_id: "creature-3249"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3249"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zombie Shambler"
level: "Creature -1"
size: "Medium"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
modifier: 0
perception:
  - name: "Perception"
    desc: "Perception +0; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +7"
abilityMods: [3, -2, 2, -5, 0, -2]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently slowed 1 and can't use reactions."
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +6; __Ref__: +0; __Will__: +2"
hp: 20
health:
  - name: "HP"
    desc: "20 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Weaknesses__ slashing 5, vitality 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +7 __Damage__ 1d6+3 bludgeoning plus Grab"
abilities_bot:
  - name: "Zombie Bite"
    desc: "⬻"
  - name: "Requirements"
    desc: "The zombie has a creature __grabbed__ or restrained"
  - name: "Effect"
    desc: "The zombie makes a jaws unarmed melee Strike against that creature with an attack modifier of +7 that deals 1d8+3 piercing damage."
sourcebook: "_Monster Core_, page 356."
```

```encounter-table
name: Zombie Shambler
creatures:
  - 1: Zombie Shambler
```
