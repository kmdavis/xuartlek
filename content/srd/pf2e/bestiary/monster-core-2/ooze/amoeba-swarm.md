---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Amoeba Swarm"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Amoeba Swarm"
level: 1
source: "Monster Core 2"
aon_id: "creature-4495"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4495"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Amoeba Swarm"
level: "Creature 1"
size: "Large"
trait_01: "Amphibious"
trait_02: "Mindless"
trait_03: "Ooze"
trait_04: "Swarm"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; motion sense 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Stealth +1"
abilityMods: [0, -2, 3, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "An amoeba swarm can sense nearby creatures through vibration and air or water movement."
ac: 9
armorclass:
  - name: "AC"
    desc: "9; __Fort__: +8; __Ref__: +1; __Will__: +3"
hp: 35
health:
  - name: "HP"
    desc: "35; __Immunities__ acid, bleed, critical hits, mental, precision, unconscious, visual; __Resistances__ slashing 4, piercing 4; __Weaknesses__ area 3, fire 3, splash damage 3"
speed: "5 feet, climb 5 feet, swim 10 feet"
abilities_bot:
  - name: "Swarming Slither"
    desc: "⬻ The amoeba swarm slithers over each creature in its space, dealing 1d6 acid damage (DC 14 basic Reflex save). A creature that critically fails is sickened 1."
  - name: "Weak Acid"
    desc: "An amoeba swarm's acid damages only organic material—not metal, stone, or other inorganic substances. Amoebas Large And Small Giant amoebas and amoeba swarms are usually found near each other, as the two oozes are part of the same life cycle. When a giant amoeba grows large enough, it can spontaneously split apart into two separate amoeba swarms, and when an amoeba swarm feeds enough, its individual components can fuse together into a single creature."
sourcebook: "_Monster Core 2_, page 240."
```

```encounter-table
name: Amoeba Swarm
creatures:
  - 1: Amoeba Swarm
```
