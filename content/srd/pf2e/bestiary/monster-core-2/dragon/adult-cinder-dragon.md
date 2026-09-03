---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Cinder Dragon"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Cinder Dragon"
level: 14
source: "Monster Core 2"
aon_id: "creature-4346"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4346"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Cinder Dragon"
level: "Creature 14"
size: "Huge"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +27, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +23"
abilityMods: [8, 2, 6, 3, 4, 5]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +27; __Ref__: +23; __Will__: +25 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 310
health:
  - name: "HP"
    desc: "310; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15"
abilities_mid:
  - name: "Dragon Heat"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 5 feet, 3d6 fire damage (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)"
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 32"
  - name: "Boiling Blood"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]])"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon's superheated blood spills onto the attacker. The target takes 8d6 fire damage (DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Reactive Strike"
    desc: "⬲ Jaws only"
speed: "50 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+12 piercing plus 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
  - name: "Melee"
    desc: "⬻ horn +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+16 piercing"
  - name: "Melee"
    desc: "⬻ claw +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d12+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ wing +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
  - name: "Pyre Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The dragon breathes a blast of flame that deals 13d6 fire damage in a 50-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 34 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Creatures that critically fail their save catch fire, taking 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]]. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The dragon intensifies nearby fires. Every foe within 60 feet that is taking [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]] takes 4d6 fire damage."
sourcebook: "_Monster Core 2_, page 118."
```

```encounter-table
name: Adult Cinder Dragon
creatures:
  - 1: Adult Cinder Dragon
```
