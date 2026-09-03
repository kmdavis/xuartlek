---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Blizzardborn"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Blizzardborn"
level: 6
source: "Monster Core 2"
aon_id: "creature-4392"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4392"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Blizzardborn"
level: "Creature 6"
size: "Medium"
trait_01: "Cold"
trait_02: "Elemental"
trait_03: "Water"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, snow vision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +15, Stealth +14"
abilityMods: [5, 2, 4, 0, 4, 0]
abilities_top:
  - name: "Snow Vision"
    desc: "The blizzardborn ignores the concealed condition from falling snow."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +14"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ bleed, cold, paralyzed, poison, sleep; __Weaknesses__ fire 5"
abilities_mid:
  - name: "Shattering Ice"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy hits the blizzardborn with an attack that deals physical damage"
  - name: "Effect"
    desc: "A portion of the blizzardborn's body shatters into an explosion of razor-sharp ice crystals and blinding snow that deals 2d6 piercing damage to opponents in a 5-foot emanation (DC 24 basic Reflex save). Anyone who fails is also blinded for 1 round (3 rounds on a critical failure)."
speed: "25 feet, ice burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ice claw +17 (versatile B) __Damage__ 2d6+8 slashing plus 1d6 persistent cold"
abilities_bot:
  - name: "Ice Burrow"
    desc: "The blizzardborn can Burrow through ice or snow with a Speed of 20 feet. It moves at its full burrow Speed, leaving no tunnels or signs of its passing."
sourcebook: "_Monster Core 2_, page 151."
```

```encounter-table
name: Blizzardborn
creatures:
  - 1: Blizzardborn
```
