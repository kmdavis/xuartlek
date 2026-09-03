---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mjolgat"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Mjolgat"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3302"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3302"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Mjolgat"
level: "Creature 4"
size: "Small"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, orescent (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [5, 2, 4, -3, 2, -2]
abilities_top:
  - name: "Orescent"
    desc: "A mjolgat can detect the ores of unrefined precious metals with its powerful nose. Common earth and stone do not impede the mjolgat from smelling ores deep within the ground."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +8; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Head On"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature the mjolgat can see targets the mjolgat with an attack"
  - name: "Effect"
    desc: "The mjolgat swings its crest in the direction of the danger, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bone crest +10 __Damage__ 2d10+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ hoof +12 __Damage__ 2d6+4 bludgeoning"
abilities_bot:
  - name: "Hammerhead"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) The mjolgat rears upon its hind leg to crush an enemy with its jagged crest of bone. The mjolgat makes a bone crest Strike; on a hit, the mjolgat deals an extra die of damage. This counts as two attacks when calculating the mjolgat's multiple attack penalty."
  - name: "Punch-Drunk"
    desc: "If the mjolgat critically fails a bone crest Strike, it becomes [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned 1]] and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] for 1 round."
  - name: "Rockbreaker"
    desc: "When the mjolgat deals damage to an object (such as a shield or an ore deposit), it deals double damage."
  - name: "Shrieking Slam"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The mjolgat lets out a terrifying screech before bashing its head into the ground. Creatures within 30 feet of the mjolgat must attempt a DC 21 Will save. Regardless of the result of the save, they are then immune to Shrieking Slam."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The target is frightened 2."
  - name: "Critical Failure"
    desc: "The target is frightened 3 and [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] for 1 round."
sourcebook: "_Howl of the Wild_, page 175."
```

```encounter-table
name: Mjolgat
creatures:
  - 1: Mjolgat
```
