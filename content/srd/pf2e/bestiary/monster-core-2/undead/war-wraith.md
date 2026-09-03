---
obsidianUIMode: preview
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
aon_id: "creature-4618"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4618"
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
    desc: "Perception +19; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
abilityMods: [-5, 6, 3, 3, 4, 6]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +21 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]"
hp: 130
health:
  - name: "HP"
    desc: "130 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ all damage 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]], [[srd/pf2e/compendium/equipment/runes/ghost-touch|_ghost touch_]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]; double resistance vs. non-magical"
abilities_mid:
  - name: "Draining Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) 10 feet. A living creature that enters the aura must succeed at a DC 26 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1. It recovers after it has been out of the aura for 1 minute. A creature that succeeds at its save is temporarily immune to draining presence for 24 hours."
  - name: "Sunlight Powerlessness"
    desc: "While in sunlight, a war wraith is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wraith touch +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) __Damage__ 2d12+6 void"
abilities_bot:
  - name: "Absorb Wraith"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The war wraith extends their hand toward another wraith creature within 100 feet. The target wraith dissolves and streaks toward the war wraith in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]], dealing 3d10 void damage to each creature along the line with a DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save. The war wraith absorbs the essence of the target wraith, becoming [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] for 1 minute. They can use their extra action only to [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] or Strike. An unwilling target can resist being absorbed if it succeeds at a DC 28 Will save."
  - name: "Grip of Fear"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]]) The wraith reaches into an adjacent creature's chest, gripping its heart. The target takes 9d6 mental damage with a DC 28 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save. On a critical failure, the creature is also [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] until the start of the wraith's next turn."
  - name: "Robes of Welcome"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The wraith wraps their robes around an adjacent living creature, exposing it to void's embrace. If any creature is cursed by the wraith's void's embrace, the wraith can't impose void's embrace on another creature."
  - name: "Void's Embrace"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) If the victim succeeds at a saving throw against this curse while in sunlight, the curse ends. While a creature has this curse, it bypasses the resistance of the wraith that cursed it"
  - name: "Saving Throw"
    desc: "DC 28 Will"
  - name: "Stage 1"
    desc: "the victim is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] in any light (1 hour)"
  - name: "Stage 2"
    desc: "the victim gains lifesense 30 feet but is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] in any light (1 hour)"
  - name: "Stage 3"
    desc: "as stage 2, but the creature also has void healing (1 hour)"
  - name: "Stage 4"
    desc: "the victim becomes [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] and can't awaken (1 day)"
  - name: "Stage 5"
    desc: "the creature dies and becomes a wraith under the command of the war wraith, its body crumbling to ash War Wraith Origins Not every war wraith was once an individual. Many of them coalesce over time, merging from multiple wraiths where lost souls accumulate and have their spirits and consciousnesses shorn apart or undermined in some way. These war wraiths tend to think and communicate not as one potent being, but as a riot of voices—often conflicting but truly bone-chilling when they agree to work in unison. In locations where void energy focuses, such as in the Void or on the Isle of Terror, war wraiths form in this way frequently."
sourcebook: "_Monster Core 2_, page 356."
```

```encounter-table
name: War Wraith
creatures:
  - 1: War Wraith
```
