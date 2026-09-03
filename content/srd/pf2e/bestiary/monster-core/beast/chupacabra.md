---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Chupacabra"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/small
statblock: inline
name: "Chupacabra"
level: 3
source: "Monster Core"
aon_id: "creature-2880"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2880"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Chupacabra"
level: "Creature 3"
size: "Small"
trait_01: "Beast"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9"
abilityMods: [3, 4, 2, -3, 2, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +11; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d10+5 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+5 slashing"
abilities_bot:
  - name: "Pounce"
    desc: "⬻ The chupacabra Strides and makes a Strike at the end of that movement. If the chupacabra began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after this ability's Strike."
  - name: "Suck Blood"
    desc: "⬻"
  - name: "Requirements"
    desc: "The chupacabra has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The chupacabra sucks blood from the grabbed creature. The chupacabra gains the [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] condition for 1 minute and can use the extra action only for Strike and Stride actions. A chupacabra can't Suck Blood again while it is quickened in this way. A creature that has its blood drained by a chupacabra is [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] until it receives healing (of any kind or amount). Winged Chupacabras Some chupacabras are mutants with large reptilian wings and have been known to carry off goats or even children. A winged chupacabra has a fly Speed of 50 feet. Other chupacabras grow much larger, up to Medium sized, and can stand eye to eye with a full-grown human. These chupacabras have elite adjustments to their statistics."
sourcebook: "_Monster Core_, page 63."
```

```encounter-table
name: Chupacabra
creatures:
  - 1: Chupacabra
```
