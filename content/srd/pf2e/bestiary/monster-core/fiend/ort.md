---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ort"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ort"
level: 0
source: "Monster Core"
aon_id: "creature-2905"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2905"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ort"
level: "Creature 0"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Mindless"
trait_04: "Unholy"
modifier: 0
perception:
  - name: "Perception"
    desc: "Perception +0; greater darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +6"
abilityMods: [2, 0, 3, -5, 0, -3]
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +9; __Ref__: +6; __Will__: +2"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ fire, mental; __Resistances__ physical 3 (except silver), poison 5; __Weaknesses__ holy 3"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +8 (Agile, Magical, Unholy) __Damage__ 1d4+2 slashing"
abilities_bot:
  - name: "Subservience"
    desc: "Orts have little drive of their own, but other devils can take command of them. A non-ort devil can issue a command to all orts within 60 feet of it with a single action, which has the auditory and concentrate traits. The devil picks one of the following orders orts can understand, and the orts follow that order. The command and its effects end once the commander is out of the ort's sight, when a new command is issued by the same or another devil, or when the ort dies."
  - name: "Kill"
    desc: "The ort attacks one target the commander singles out and gains a +1 circumstance bonus to attack rolls against the target."
  - name: "Defend"
    desc: "The ort circles the commander and attacks any creature that comes near. It gains a +1 circumstance bonus to AC and saves."
  - name: "Fetch"
    desc: "The ort gains a +10–foot circumstance bonus to its Speed and attempts to get an object or person the commander singles out. It attacks anyone and anything that gets in the way."
  - name: "Work"
    desc: "The ort performs drudge work dictated by the commander."
sourcebook: "_Monster Core_, page 86."
```

```encounter-table
name: Ort
creatures:
  - 1: Ort
```
