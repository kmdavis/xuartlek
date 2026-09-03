---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zombie Brute"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/large
statblock: inline
name: "Zombie Brute"
level: 2
source: "Monster Core"
aon_id: "creature-3251"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3251"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zombie Brute"
level: "Creature 2"
size: "Large"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +11"
abilityMods: [5, -3, 4, -5, 0, -2]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently slowed 1 and can't use reactions."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +10; __Ref__: +3; __Will__: +6"
hp: 70
health:
  - name: "HP"
    desc: "70 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Weaknesses__ slashing 10, vitality 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 (reach 10 feet) __Damage__ 1d12+5 bludgeoning plus Improved Push 5 feet"
sourcebook: "_Monster Core_, page 357."
```

```encounter-table
name: Zombie Brute
creatures:
  - 1: Zombie Brute
```
