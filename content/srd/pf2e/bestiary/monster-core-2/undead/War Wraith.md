---
noteType: pf2eMonster
aliases: "War Wraith"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/wraith
  - pf2e/creature/trait/medium
statblock: inline
name: "War Wraith"
level: 9
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4618"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "War Wraith"
level: "Creature 9"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Wraith"
modifier: 19
perception:
  - name: "Perception"
    desc: "+19; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +19"
abilityMods: [-5, 6, 3, 3, 4, 6]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +21 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]"
hp: 130
health:
  - name: "HP"
    desc: "130 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]; __Resistances__ all damage 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]; double resistance vs. non-magical"
abilities_mid:
  - name: "Draining Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) 10 feet. A living creature that enters the aura must succeed at a DC 26 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 1. It recovers after it has been out of the aura for 1 minute. A creature that succeeds at its save is temporarily immune to draining presence for 24 hours."
  - name: "Sunlight Powerlessness"
    desc: "While in sunlight, a war wraith is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]] 2."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wraith touch +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) __Damage__ 2d12+6 void"
abilities_bot:
  - name: "Absorb Wraith"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The war wraith extends their hand toward another wraith creature within 100 feet. The target wraith dissolves and streaks toward the war wraith in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Line|line]], dealing 3d10 void damage to each creature along the line with a DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save. The war wraith absorbs the essence of the target wraith, becoming [[srd/pf2e/compendium/rules-elements/Conditions#Quickened|quickened]] for 1 minute. They can use their extra action only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] or Strike. An unwilling target can resist being absorbed if it succeeds at a DC 28 Will save."
  - name: "Grip of Fear"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]]) The wraith reaches into an adjacent creature's chest, gripping its heart. The target takes 9d6 mental damage with a DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Will save. On a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] until the start of the wraith's next turn."
  - name: "Robes of Welcome"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The wraith wraps their robes around an adjacent living creature, exposing it to void's embrace. If any creature is cursed by the wraith's void's embrace, the wraith can't impose void's embrace on another creature."
  - name: "Void's Embrace"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]) If the victim succeeds at a saving throw against this curse while in sunlight, the curse ends. While a creature has this curse, it bypasses the resistance of the wraith that cursed it"
  - name: "Saving Throw"
    desc: "DC 28 Will"
  - name: "Stage 1"
    desc: "the victim is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] in any light (1 hour)"
  - name: "Stage 2"
    desc: "the victim gains lifesense 30 feet but is [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] in any light (1 hour)"
  - name: "Stage 3"
    desc: "as stage 2, but the creature also has void healing (1 hour)"
  - name: "Stage 4"
    desc: "the victim becomes [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] and can't awaken (1 day)"
  - name: "Stage 5"
    desc: "the creature dies and becomes a wraith under the command of the war wraith, its body crumbling to ash War Wraith Origins Not every war wraith was once an individual. Many of them coalesce over time, merging from multiple wraiths where lost souls accumulate and have their spirits and consciousnesses shorn apart or undermined in some way. These war wraiths tend to think and communicate not as one potent being, but as a riot of voices—often conflicting but truly bone-chilling when they agree to work in unison. In locations where void energy focuses, such as in the Void or on the Isle of Terror, war wraiths form in this way frequently."
sourcebook: "_Monster Core 2_, page 356."
```

```encounter-table
name: War Wraith
creatures:
  - 1: War Wraith
```
