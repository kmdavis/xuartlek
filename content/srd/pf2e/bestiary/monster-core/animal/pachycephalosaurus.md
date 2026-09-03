---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pachycephalosaurus"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/large
statblock: inline
name: "Pachycephalosaurus"
level: 3
source: "Monster Core"
aon_id: "creature-2917"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2917"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pachycephalosaurus"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +7"
abilityMods: [4, 3, 4, -4, 3, 0]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +12; __Ref__: +11; __Will__: +7"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ skull +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+6 bludgeoning"
abilities_bot:
  - name: "Clobbering Charge"
    desc: "⬺ The pachycephalosaurus Strides up to its Speed. If it ends its movement within melee reach of a target, it can make a skull Strike against that target. If the pachycephalosaurus critically hits with this Strike, the creature hit is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]]."
  - name: "Sudden Shove"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Trigger"
    desc: "The pachycephalosaurus damages a Medium or smaller foe with its skull Strike"
  - name: "Effect"
    desc: "The pachycephalosaurus digs in and flings its head up, shoving its foe away. It attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the target's Fortitude DC."
  - name: "Critical Success"
    desc: "The pachycephalosaurus pushes the opponent up to 10 feet away from itself and knocks the target [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Success"
    desc: "The pachycephalosaurus pushes the opponent back 5 feet."
  - name: "Failure"
    desc: "The pachycephalosaurus fails to push the opponent."
  - name: "Critical Failure"
    desc: "As failure, but the failed attempt leaves the pachycephalosaurus [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] for 1 round."
sourcebook: "_Monster Core_, page 97."
```

```encounter-table
name: Pachycephalosaurus
creatures:
  - 1: Pachycephalosaurus
```
