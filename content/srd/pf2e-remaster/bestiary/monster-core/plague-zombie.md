---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Plague Zombie"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/zombie
  - pf2e/creature/trait/medium
statblock: inline
name: "Plague Zombie"
level: 1
source: "Monster Core"
aon_id: "creature-3250"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3250"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Plague Zombie"
level: "Creature 1"
size: "Medium"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +9"
abilityMods: [4, -2, 3, -5, 0, -2]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently slowed 1 and can't use reactions."
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +6; __Ref__: +3; __Will__: +4"
hp: 50
health:
  - name: "HP"
    desc: "50 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Weaknesses__ slashing 10, vitality 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +9 __Damage__ 1d8+4 bludgeoning plus Grab and zombie rot"
abilities_bot:
  - name: "Zombie Bite"
    desc: "⬻"
  - name: "Requirements"
    desc: "The zombie has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The zombie makes a jaws unarmed melee Strike against that creature with an attack modifier of +9 that deals 1d12+4 piercing damage and exposes the creature to zombie rot."
  - name: "Zombie Rot"
    desc: "(Disease, Divine, Void) An infected creature can't heal damage it takes from zombie rot until it has been cured of the disease"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "1d6 void damage (1 day)"
  - name: "Stage 3"
    desc: "1d6 void damage (1 day)"
  - name: "Stage 4"
    desc: "1d6 void damage (1 day)"
  - name: "Stage 5"
    desc: "dead, rising as a plague zombie immediately"
sourcebook: "_Monster Core_, page 356."
```

```encounter-table
name: Plague Zombie
creatures:
  - 1: Plague Zombie
```
