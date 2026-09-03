---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Tar"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/huge
statblock: inline
name: "Living Tar"
level: 7
source: "Monster Core"
aon_id: "creature-3128"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3128"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Living Tar"
level: "Creature 7"
size: "Huge"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; motion sense (precise) 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Athletics +18"
abilityMods: [7, -5, 7, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A living tar can feel nearby motion through vibration and air movement."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +18; __Ref__: +6; __Will__: +11"
hp: 165
health:
  - name: "HP"
    desc: "165; __Immunities__ acid, bleed, bludgeoning, critical hits, mental, precision, unconscious, visual"
abilities_mid:
  - name: "Adhesive Mass"
    desc: "A weapon that hits the living tar is stuck to the ooze. Removing it requires a successful DC 23 Athletics check to Break Open. The living tar can have any number of objects or creatures stuck to it at a time. It can release a stuck object with an Interact action, and the adhesive dissolves 1 minute after the ooze dies, releasing all stuck objects and creatures."
speed: "20 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +18 (reach 10 feet) __Damage__ 2d8+7 bludgeoning plus 2d6 acid and Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d8+7 bludgeoning plus 1d6 acid, DC 26"
  - name: "Engulf"
    desc: "⬽ DC 22, 4d6 acid, Escape DC 22, Rupture 15"
sourcebook: "_Monster Core_, page 257."
```

```encounter-table
name: Living Tar
creatures:
  - 1: Living Tar
```
