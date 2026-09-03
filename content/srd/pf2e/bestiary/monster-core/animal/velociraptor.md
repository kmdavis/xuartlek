---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Velociraptor"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/small
statblock: inline
name: "Velociraptor"
level: 1
source: "Monster Core"
aon_id: "creature-2915"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2915"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Velociraptor"
level: "Creature 1"
size: "Small"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [0, 3, 2, -4, 1, 1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ talon +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4+3 slashing"
abilities_bot:
  - name: "Leaping Charge"
    desc: "⬻ The velociraptor Strides up to 10 feet, ignoring difficult terrain as it leaps over obstacles. It then makes a Strike with its talons, gaining a +1 circumstance bonus to its attack roll."
  - name: "Pack Attack"
    desc: "The velociraptor deals 1d4 extra damage to any creature that's within reach of at least two of the velociraptor's allies."
sourcebook: "_Monster Core_, page 96."
```

```encounter-table
name: Velociraptor
creatures:
  - 1: Velociraptor
```
