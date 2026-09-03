---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Cockroach"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Giant Cockroach"
level: 1
source: "Monster Core 2"
aon_id: "creature-4300"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4300"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Cockroach"
level: "Creature 1"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [1, 3, 1, -5, 1, -1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +8; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Scurry"
    desc: "⬲"
  - name: "Trigger"
    desc: "The giant cockroach is targeted by a melee attack"
  - name: "Effect"
    desc: "The giant cockroach gains a +2 circumstance bonus to AC against the triggering attack. After the attack resolves, the cockroach [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climbs]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to 10 feet."
speed: "25 feet, climb 25 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6+1 piercing Cockroach Species Beyond the common giant cockroach, other flesh-eating cockroaches exist throughout the world. These variations include the giant hissing cockroach, the noxious venomroach, the huge spitting cockroach (which can incapacitate enemies from a distance), the aggressive sawback cockroach, and the mysterious and rare dragonroach."
sourcebook: "_Monster Core 2_, page 76."
```

```encounter-table
name: Giant Cockroach
creatures:
  - 1: Giant Cockroach
```
