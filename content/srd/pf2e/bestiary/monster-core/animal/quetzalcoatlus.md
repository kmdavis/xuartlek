---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Quetzalcoatlus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Quetzalcoatlus"
level: 7
source: "Monster Core"
aon_id: "creature-3152"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3152"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Quetzalcoatlus"
level: "Creature 7"
size: "Huge"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17"
abilityMods: [6, 4, 3, -4, 2, -1]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +16; __Ref__: +17; __Will__: +12"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "15 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+10 piercing plus 1d8 persistent bleed"
  - name: "Melee"
    desc: "⬻ talon +17 __Damage__ 2d8+10 piercing plus Grab"
abilities_bot:
  - name: "Carry"
    desc: "A quetzalcoatlus can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at half Speed while it has a single creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]. Both its talons are occupied while it does this."
  - name: "Swoop"
    desc: "⬺ The quetzalcoatlus [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to its Speed and makes one beak or talon Strike at any point during that movement."
sourcebook: "_Monster Core_, page 278."
```

```encounter-table
name: Quetzalcoatlus
creatures:
  - 1: Quetzalcoatlus
```
