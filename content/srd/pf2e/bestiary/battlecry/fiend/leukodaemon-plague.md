---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leukodaemon Plague"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Leukodaemon Plague"
level: 14
source: "Battlecry!"
aon_id: "creature-3925"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3925"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Leukodaemon Plague"
level: "Creature 14"
size: "Gargantuan"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Troop"
trait_04: "Unholy"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, plaguesense (imprecise) 60 feet"
languages: "Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Intimidation +25, Medicine +28, Religion +28, Stealth +25, Survival +23"
abilityMods: [7, 5, 1, 3, 5, 3]
abilities_top:
  - name: "Plaguesense"
    desc: "A leukodaemon plague senses any creature with a disease, and knows the type and current stage of all diseases carried by any creature within range."
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +22; __Ref__: +25; __Will__: +28"
hp: 255
health:
  - name: "HP"
    desc: "255 (4 segments); __Immunities__ death effects, disease; __Weaknesses__ area damage 15, holy 15, splash damage 15"
abilities_mid:
  - name: "Infectious Aura"
    desc: "(aura, disease) 30 feet. Leukodaemons radiate infection. All creatures within 30 feet of a leukodaemon plague take a –2 status penalty to saves against disease. If a creature within range contracts or progresses a disease, all adjacent creatures are exposed to the same disease, at the same DC."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, fly 40 feet; troop movement"
abilities_bot:
  - name: "Daemonic Pestilence"
    desc: "(Disease) The leukodaemon plague can telepathically communicate with the afflicted creature at any distance on the same plane"
  - name: "Saving Throw"
    desc: "DC 34 Fortitude"
  - name: "Stage 1"
    desc: "carrier (1 day)"
  - name: "Stage 2"
    desc: "drained 1 (1 day)"
  - name: "Stage 3"
    desc: "drained 2 (1 day)"
  - name: "Stage 4"
    desc: "drained 2 (1 day)"
  - name: "Stage 5"
    desc: "drained 3 (1 week); Stage 6 dead"
  - name: "Infected Jaws and Claws"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The leukodaemons unleash an onslaught of blows against each enemy in a 10-foot emanation (DC 31 basic Reflex save). The damage depends on the number of actions. ⬻ 1d10+3 piercing or slashing damage plus daemonic pestilence ⬺ 3d10+9 piercing or slashing damage plus daemonic pestilence ⬽ 4d10+12 piercing or slashing damage plus daemonic pestilence"
  - name: "Pestilent Wheeze"
    desc: "⬺ (Divine, Unholy) The leukodaemons exhale a 30-foot cone of disease-ridden black flies that deal 5d8 piercing damage (DC 31 basic Reflex save). A creature that fails the save also becomes sickened 1 (or sickened 2 on a critical failure). When the leukodaemon plague is reduced to 2 segments, this area decreases to a 20-foot cone."
  - name: "Quicken Pestilence"
    desc: "⬻ (Divine, Manipulate) The leukodaemons coax a disease into full bloom. They choose a target within their infectious aura that's currently affected by a disease. That creature must attempt a Fortitude save against the disease as if the interval for the disease's current stage had passed."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __5th__ Translocate (at will) - __7th__ Dispel Magic"
sourcebook: "_Battlecry!_, page 184."
```

```encounter-table
name: Leukodaemon Plague
creatures:
  - 1: Leukodaemon Plague
```
