---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Dragon"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Clockwork Dragon"
level: 16
source: "Monster Core 2"
aon_id: "creature-4297"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4297"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Dragon"
level: "Creature 16"
size: "Huge"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Rare"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +29, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33"
abilityMods: [9, 5, 5, -5, 4, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "1 week, DC 35, standby"
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +30; __Ref__: +28; __Will__: +25"
hp: 265
health:
  - name: "HP"
    desc: "265; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Nonlethal|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 15 (except [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]] or [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 15, [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]] 15"
abilities_mid:
  - name: "Self-Destruct"
    desc: "⬲ A clockwork dragon must use this reaction unless specifically programmed otherwise by its creator"
  - name: "Trigger"
    desc: "The clockwork dragon is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The dragon screeches to a stop and emits a steady, loud ticking sound. At the beginning of what would have been its next turn, the dragon explodes, dealing 12d10 piercing damage in a 40-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 37 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). An adjacent creature can cancel the self-destruct sequence by succeeding at a DC 37 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disable a Device|Disable a Device]]."
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ adamantine jaws +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+17 piercing"
  - name: "Melee"
    desc: "⬻ adamantine claw +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+15 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+15 piercing"
abilities_bot:
  - name: "Breathe Oil"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]])"
  - name: "Effect"
    desc: "The clockwork dragon breathes a spray of flaming oil that deals 16d6 fire damage in a 40-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] with a DC 37 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. Creatures that fail their saves are covered in burning oil and take 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]]. The clockwork dragon can't Breathe Oil again for 2 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The clockwork dragon makes two adamantine claw Strikes and one wing Strike in any order."
  - name: "Spearing Tail"
    desc: "⬺ The clockwork dragon attacks with the sharp point of its tail. It makes a tail Strike against each creature in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]], rolling the attack roll once and applying the result to each target. Any creature that takes damage also takes 4d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] (doubled on a critical hit). This counts as two attacks for the dragon's multiple attack penalty."
sourcebook: "_Monster Core 2_, page 72."
```

```encounter-table
name: Clockwork Dragon
creatures:
  - 1: Clockwork Dragon
```
