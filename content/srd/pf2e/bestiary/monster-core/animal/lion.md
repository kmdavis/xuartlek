---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lion"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Lion"
level: 3
source: "Monster Core"
aon_id: "creature-2866"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2866"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lion"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet Skills Acrobatics 8, Athletics 9, Stealth 10"
abilityMods: [4, 3, 2, -4, 2, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +10; __Will__: +7"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d10+6 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d8+6 slashing"
abilities_bot:
  - name: "Pack Attack"
    desc: "The lion deals 1d4 extra damage to any creature that's within reach of at least two of the lion's allies."
  - name: "Pounce"
    desc: "⬻ The lion Strides and makes a Strike at the end of that movement. If the lion began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after the ability's Strike."
  - name: "Sneak Attack"
    desc: "The lion deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 50."
```

```encounter-table
name: Lion
creatures:
  - 1: Lion
```
