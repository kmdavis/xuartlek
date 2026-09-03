---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gutter Ooze"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/tiny
statblock: inline
name: "Gutter Ooze"
level: -1
source: "Monster Core 2"
aon_id: "creature-4494"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4494"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Gutter Ooze"
level: "Creature -1"
size: "Tiny"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 2
perception:
  - name: "Perception"
    desc: "Perception +2; motion sense 30 feet, no vision"
skills:
  - name: "Skills"
    desc: "Athletics +5, Stealth +2"
abilityMods: [0, 3, 4, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A gutter ooze can sense nearby creatures through vibration and air or water movement."
ac: 7
armorclass:
  - name: "AC"
    desc: "7; __Fort__: +8; __Ref__: +3; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ acid, bleed, critical hits, mental, precision, unconscious, visual"
abilities_mid:
  - name: "Slip Up"
    desc: "⬲"
  - name: "Trigger"
    desc: "An adjacent creature damages the gutter ooze with a melee Strike"
  - name: "Effect"
    desc: "Some of the gutter ooze's watery protoplasm gushes out beneath the triggering creature's feet. They must succeed at a DC 15 Reflex save or fall prone."
speed: "10 feet, swim 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +8 (Agile, finesse, reach 5 feet) __Damage__ 1d4 bludgeoning, slashing, or piercing plus 1 acid; see detritus"
abilities_bot:
  - name: "Detritus"
    desc: "Due to all the random trash that collects in a city's gutters, whenever a gutter ooze makes a pseudopod Strike, the type of damage is chosen randomly between bludgeoning, slashing, and piercing."
  - name: "Weak Acid"
    desc: "A gutter ooze's acid damages only organic material—not metal, stone, or other inorganic substances."
sourcebook: "_Monster Core 2_, page 240."
```

```encounter-table
name: Gutter Ooze
creatures:
  - 1: Gutter Ooze
```
