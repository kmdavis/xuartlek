---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ember Fox"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/small
statblock: inline
name: "Ember Fox"
level: 2
source: "Monster Core 2"
aon_id: "creature-4386"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4386"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ember Fox"
level: "Creature 2"
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "Pyric; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +5, Stealth +8"
abilityMods: [1, 4, 2, -2, 2, 1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +10; __Will__: +8"
hp: 35
health:
  - name: "HP"
    desc: "35; __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 5 __Cloak in Embers [reaction__ ]"
abilities_mid:
  - name: "Trigger"
    desc: "An adjacent ally is targeted by an effect that deals fire damage"
  - name: "Effect"
    desc: "The ember fox drapes itself across its ally, granting the ally fire resistance 10 against the incoming attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 (Agile, finesse) __Damage__ 1d4+3 piercing plus 1d4 persistent fire"
sourcebook: "_Monster Core 2_, page 148."
```

```encounter-table
name: Ember Fox
creatures:
  - 1: Ember Fox
```
