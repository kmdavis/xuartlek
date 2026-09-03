---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Eagle"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Eagle"
level: -1
source: "Monster Core"
aon_id: "creature-2968"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2968"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Eagle"
level: "Creature -1"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6"
abilityMods: [0, 3, 1, -4, 1, 1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +4; __Ref__: +6; __Will__: +2"
hp: 6
health:
  - name: "HP"
    desc: "6"
speed: "10 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6 piercing"
  - name: "Melee"
    desc: "⬻ talon +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4 slashing"
abilities_bot:
  - name: "Eagle Dive"
    desc: "⬺ The eagle Flies up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a talon Strike."
sourcebook: "_Monster Core_, page 137."
```

```encounter-table
name: Eagle
creatures:
  - 1: Eagle
```
