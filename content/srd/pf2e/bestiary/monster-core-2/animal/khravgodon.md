---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Khravgodon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Khravgodon"
level: 9
source: "Monster Core 2"
aon_id: "creature-4501"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4501"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Khravgodon"
level: "Creature 9"
size: "Huge"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +18"
abilityMods: [6, 3, 5, -4, 3, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +18; __Will__: +16 +2 circumstance to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]"
hp: 160
health:
  - name: "HP"
    desc: "160; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 10"
abilities_mid:
  - name: "Feign Death"
    desc: "⬲ The opossum is reduced below 70 HP"
  - name: "Effect"
    desc: "The khravgodon collapses. It is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] and can use actions that require only its mind, but any other action ends the ruse. A successful DC 18 [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] or [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] is required to determine that the animal is not, in fact, dead."
  - name: "Revived Retaliation"
    desc: "⬲"
  - name: "Trigger"
    desc: "The khravgodon is attacked or disturbed by a creature within reach while Feigning Death"
  - name: "Effect"
    desc: "The khravgodon Strikes the triggering creature."
speed: "30 feet, burrow 15 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d12]]) __Damage__ 2d12+9 piercing"
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d10+9 slashing"
  - name: "Melee"
    desc: "⬻ tail +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d6+9 bludgeoning plus Grab"
abilities_bot:
  - name: "Crush Chitin"
    desc: "⬻"
  - name: "Requirements"
    desc: "The khravgodon has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The khravgodon bites the creature, dealing 2d12+9 piercing damage (DC 28 [[srd/pf2e/books/player-core/chapter-7-spells/defenses#Basic Saving Throws|basic]] Fortitude save) that ignores the first 5 of the target's [[srd/pf2e/books/player-core/chapter-6-equipment/shields#Hardness|Hardness]] or resistance to physical damage. On a failed save, the target also takes a –2 circumstance penalty to AC for 1 round."
  - name: "Grasping Tail"
    desc: "A khravgodon can drag Large or smaller creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] with its tail along with it when it Strides. Tail Tales A Kellid legend holds that the khravgodon once had a beautiful tail covered with bright, thick fur. One night, the khravgodon fell asleep in the open, having danced all night showing off its beautiful tail. When it awoke, [[srd/pf2e/compendium/gm/creature-families/ankhrav|ankhravs]] had chewed all the hair off khravgodon's tail, leaving it with the bald appendage we see today. Khravgodons have been taking revenge on ankhravs ever since."
sourcebook: "_Monster Core 2_, page 244."
```

```encounter-table
name: Khravgodon
creatures:
  - 1: Khravgodon
```
