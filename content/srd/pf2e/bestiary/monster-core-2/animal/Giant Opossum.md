---
noteType: pf2eMonster
aliases: "Giant Opossum"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Opossum"
level: 2
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4500"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Opossum"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +6"
abilityMods: [4, 2, 3, -4, 2, 0]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +8; __Will__: +5 +2 circumstance to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
hp: 35
health:
  - name: "HP"
    desc: "35; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 3"
abilities_mid:
  - name: "Feign Death"
    desc: "⬲"
  - name: "Trigger"
    desc: "The opossum is reduced below 15 HP"
  - name: "Effect"
    desc: "The opossum collapses. It is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] and can use actions that require only its mind, but any other action ends the ruse. A successful DC 18 [[srd/pf2e/books/player-core/chapter-1-introduction/Character Creation#Perception|Perception]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] or [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] is required to determine that the animal is not, in fact, dead."
  - name: "Revived Retaliation"
    desc: "⬲"
  - name: "Trigger"
    desc: "The opossum is attacked or disturbed by a creature within reach while Feigning Death"
  - name: "Effect"
    desc: "The opossum Strikes the triggering creature."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|]]) __Damage__ 1d10+4 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d6+4 slashing"
  - name: "Melee"
    desc: "⬻ tail +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 1d4+4 bludgeoning plus Grab"
abilities_bot:
  - name: "Grasping Tail"
    desc: "A giant opossum can drag a Small or Tiny creature it has [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] with its tail along with it when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]]."
sourcebook: "_Monster Core 2_, page 244."
```

```encounter-table
name: Giant Opossum
creatures:
  - 1: Giant Opossum
```
