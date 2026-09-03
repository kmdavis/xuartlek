---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leukodaemon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Leukodaemon"
level: 9
source: "Monster Core"
aon_id: "creature-2893"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2893"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Leukodaemon"
level: "Creature 9"
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, plaguesense (imprecise) 60 feet"
languages: "Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Intimidation +18, Medicine +20, Religion +20, Stealth +18, Survival +16"
abilityMods: [6, 5, 1, 3, 5, 3]
abilities_top:
  - name: "Plaguesense"
    desc: "A leukodaemon senses any creature with a disease, and they know the type and current stage of all diseases carried by any creature within range."
  - name: "Items"
    desc: "_+1 striking composite longbow_ (50 arrows)"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +21; __Will__: +19 +1 status to all saves vs. magic"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ death effects, disease; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Infectious Aura"
    desc: "(aura, disease) 30 feet. Leukodaemons radiate infection. All creatures within 30 feet of a leukodaemon take a –2 status penalty to saves against disease. If a creature within range contracts or progresses a disease, all adjacent creatures are exposed to the same disease, at the same DC."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 (Disease, Magical, reach 10 feet, Unholy) __Damage__ 2d12+9 piercing plus daemonic pestilence"
  - name: "Melee"
    desc: "⬻ claw +21 (Agile, Disease, Magical, reach 10 feet, Unholy) __Damage__ 2d8+9 slashing plus daemonic pestilence"
  - name: "Ranged"
    desc: "⬻ composite longbow +21 (deadly d10, Disease, Magical, Propulsive, range increment 100 feet, reload 0, volley 30 feet, Unholy) __Damage__ 2d8+9 piercing plus daemonic pestilence"
abilities_bot:
  - name: "Daemonic Pestilence"
    desc: "(Disease) The leukodaemon can telepathically communicate with the afflicted creature at any distance on the same plane"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Stage 1"
    desc: "carrier (1 day)"
  - name: "Stage 2"
    desc: "drained 1 (1 day)"
  - name: "Stage 3"
    desc: "drained 2 (1 day)"
  - name: "Stage 4"
    desc: "drained 2 (1 day)"
  - name: "Stage 5"
    desc: "drained 3 (1 week)"
  - name: "Stage 6"
    desc: "dead"
  - name: "Plague Breath"
    desc: "⬺ (Divine, Unholy) The leukodaemon exhales a cloud of corpse-bloated, biting black flies in a 20-foot cone. Creatures within the cone take 4d8 piercing damage (DC 28 basic Reflex save). A creature that fails the save becomes sickened 1 (or sickened 2 on a critical failure)."
  - name: "Quicken Pestilence"
    desc: "⬻ (Divine, Manipulate) The leukodaemon coaxes a disease into full bloom. They choose a target in their aura of pestilence that's currently affected by a disease. That creature must attempt a Fortitude save against the disease as if the interval for the disease's current stage had passed."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __4th__ Dispel Magic (×2), Translocate (at will) - __5th__ Translocate"
sourcebook: "_Monster Core_, page 74."
```

```encounter-table
name: Leukodaemon
creatures:
  - 1: Leukodaemon
```
