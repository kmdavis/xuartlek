---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ascendant Griffon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Ascendant Griffon"
level: 11
source: "Howl of the Wild"
aon_id: "creature-3287"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3287"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Ascendant Griffon"
level: "Creature 11"
size: "Huge"
trait_01: "Animal"
trait_02: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, scent (imprecise) 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +22"
abilityMods: [7, 6, 5, -4, 3, 7]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +24; __Will__: +18"
hp: 210
health:
  - name: "HP"
    desc: "210"
abilities_mid:
  - name: "Dread Gaze"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature ends a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action within 30 feet of the ascendant griffon"
  - name: "Effect"
    desc: "The ascendant griffon turns its head to stare down the triggering creature, and attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] it. This use of Demoralize has the [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]] trait rather than the [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] trait, and the griffon does not take a penalty on its check for not sharing a language."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +24 __Damage__ 4d8+10 piercing"
  - name: "Melee"
    desc: "⬻ talon +24 __Damage__ 4d6+10 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ wing +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 4d6+10 slashing"
  - name: "Ranged"
    desc: "⬻ feather +25 (range 60 feet) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Carry Off"
    desc: "An ascendant griffon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at full speed with a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in its talons, moving that creature along with it."
  - name: "Disembowel"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ascendant griffon has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in its talons"
  - name: "Effect"
    desc: "The griffon makes a beak Strike to rip at the flesh of its prey. If the Strike hits, that creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (or increases its drained value by 1, to a maximum of 4)."
  - name: "Terrifying Screech"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The ascendant griffon unleashes a fearsome cry that strikes terror into its prey. Each creature within 100 feet must attempt a DC 30 Will save. Regardless of the result, creatures are temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "The creature is frightened 2 and [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] for 1 round."
  - name: "Razor-Edged Flight"
    desc: "⬺ The ascendant griffon glides violently forward, [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flying]] twice. It makes a wing Strike at any point during the movement against up to two different targets; if either of these attacks is a critical hit, the target also takes 2d6 persistent bleed damage."
sourcebook: "_Howl of the Wild_, page 157."
```

```encounter-table
name: Ascendant Griffon
creatures:
  - 1: Ascendant Griffon
```
