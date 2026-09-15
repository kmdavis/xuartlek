---
noteType: pf2eMonster
aliases: "Young Cinder Dragon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/large
statblock: inline
name: "Young Cinder Dragon"
level: 10
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4345"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Cinder Dragon"
level: "Creature 10"
size: "Large"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
modifier: 20
perception:
  - name: "Perception"
    desc: "+20; darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +19, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +18, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +17"
abilityMods: [6, 1, 4, 1, 2, 3]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] condition from smoke."
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +17; __Will__: +19 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]"
hp: 210
health:
  - name: "HP"
    desc: "210; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 90 feet, DC 27"
  - name: "Boiling Blood"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]])"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon's superheated blood spills onto the attacker. The target takes 6d6 fire damage (DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
speed: "40 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+10 piercing plus 1d8 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent fire]]"
  - name: "Melee"
    desc: "⬻ horn +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d12+14 piercing"
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]) __Damage__ 2d10+10 slashing"
  - name: "Melee"
    desc: "⬻ tail +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d12+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d8+10 slashing"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
  - name: "Pyre Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The dragon breathes a blast of flame that deals 9d6 fire damage in a 40-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). Creatures that critically fail their save catch fire, taking 2d6 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent fire damage]]. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The dragon intensifies nearby fires. Every foe within 60 feet that is taking [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent fire damage]] takes 3d6 fire damage."
sourcebook: "_Monster Core 2_, page 118."
```

```encounter-table
name: Young Cinder Dragon
creatures:
  - 1: Young Cinder Dragon
```
