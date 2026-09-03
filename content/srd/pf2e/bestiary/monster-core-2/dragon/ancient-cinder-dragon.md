---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Cinder Dragon"
tags:
  - pf2e/creature/level/19
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Cinder Dragon"
level: 19
source: "Monster Core 2"
aon_id: "creature-4347"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4347"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Cinder Dragon"
level: "Creature 19"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: "Uncommon"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +38, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +35, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +37, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +36, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +37"
abilityMods: [10, 4, 8, 5, 6, 7]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +34; __Ref__: +30; __Will__: +32 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20"
abilities_mid:
  - name: "Dragon Heat"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 5 feet, 4d6 fire damage (DC 37 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)"
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 37"
  - name: "Boiling Blood"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]])"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon's superheated blood spills onto the attacker. The target takes 10d6 fire damage (DC 41 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d12+12 piercing plus 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
  - name: "Melee"
    desc: "⬻ horn +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+16 piercing"
  - name: "Melee"
    desc: "⬻ claw +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d10+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 25 feet]]) __Damage__ 4d8+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 4d8+12 slashing"
abilities_bot:
  - name: "All Becomes Flame"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The dragon curses a creature within 60 feet to have its magic replaced with primordial flames. The creature must attempt a DC 39 Will save. Regardless of the result, the target becomes temporarily immune for 1 day."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/traits/gm-core/cursed|cursed]] for 1 round. While cursed, any damage the cursed creature would deal by any means becomes fire damage, regardless of the original damage type. The cursed creature can temporarily suppress the curse for 1 round as an action."
  - name: "Failure"
    desc: "As success, but the curse's duration is 1 hour."
  - name: "Critical Failure"
    desc: "As success, but the curse's duration is 1 day."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
  - name: "Pyre Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The dragon breathes a blast of flame that deals 18d6 fire damage in a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 41 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Creatures that critically fail their save catch fire, taking 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]]. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The dragon intensifies nearby fires. Every foe within 60 feet that is taking [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]] takes 5d6 fire damage."
sourcebook: "_Monster Core 2_, page 119."
```

```encounter-table
name: Ancient Cinder Dragon
creatures:
  - 1: Ancient Cinder Dragon
```
