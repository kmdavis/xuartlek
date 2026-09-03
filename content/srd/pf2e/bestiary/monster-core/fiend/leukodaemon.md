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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +20, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [6, 5, 1, 3, 5, 3]
abilities_top:
  - name: "Plaguesense"
    desc: "A leukodaemon senses any creature with a [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], and they know the type and current stage of all diseases carried by any creature within range."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_ (50 arrows)"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +21; __Will__: +19 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Infectious Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]) 30 feet. Leukodaemons radiate infection. All creatures within 30 feet of a leukodaemon take a –2 status penalty to saves against [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]. If a creature within range contracts or progresses a disease, all adjacent creatures are exposed to the same disease, at the same DC."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d12+9 piercing plus daemonic pestilence"
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+9 slashing plus daemonic pestilence"
  - name: "Ranged"
    desc: "⬻ composite longbow +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+9 piercing plus daemonic pestilence"
abilities_bot:
  - name: "Daemonic Pestilence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) The leukodaemon can telepathically communicate with the afflicted creature at any distance on the same plane"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Stage 1"
    desc: "carrier (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 day)"
  - name: "Stage 3"
    desc: "drained 2 (1 day)"
  - name: "Stage 4"
    desc: "drained 2 (1 day)"
  - name: "Stage 5"
    desc: "drained 3 (1 week)"
  - name: "Stage 6"
    desc: "dead"
  - name: "Plague Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) The leukodaemon exhales a cloud of corpse-bloated, biting black flies in a 20-foot cone. Creatures within the cone take 4d8 piercing damage (DC 28 basic Reflex save). A creature that fails the save becomes [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (or sickened 2 on a critical failure)."
  - name: "Quicken Pestilence"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The leukodaemon coaxes a disease into full bloom. They choose a target in their aura of pestilence that's currently affected by a [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]. That creature must attempt a Fortitude save against the disease as if the interval for the disease's current stage had passed."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __4th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] (×2), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
sourcebook: "_Monster Core_, page 74."
```

```encounter-table
name: Leukodaemon
creatures:
  - 1: Leukodaemon
```
