---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Werebear"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/large
statblock: inline
name: "Werebear"
level: 4
source: "Monster Core"
aon_id: "creature-3237"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3237"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Werebear"
level: "Creature 4"
size: "Large"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Uncommon"
trait_05: "Werecreature"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; bear empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +9, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [5, 2, 4, 1, 3, -1]
abilities_top:
  - name: "Bear Empathy"
    desc: "The werebear can communicate with ursine creatures."
  - name: "Items"
    desc: "Chain Shirt, Greataxe, Hatchet (8)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +10; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ silver 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d10+7 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ greataxe +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d12+7 slashing"
  - name: "Melee"
    desc: "⬻ hatchet +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ jaws +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d12+7 piercing plus curse of the werebear"
  - name: "Ranged"
    desc: "⬻ hatchet +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+7 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Medium human with fist +13 for 1d4+7 bludgeoning, or grizzly bear with Speed 35 feet."
  - name: "Curse of the Werebear"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Hunt Prey"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The werebear designates a single creature they can see and hear, or one they're [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Tracking]], as their prey. The werebear gains a +2 circumstance bonus to Perception checks when they [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] their prey and to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks when they Track their prey. The first time the werebear hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the werebear uses Hunt Prey again."
  - name: "Mauler"
    desc: "The werebear gains a +2 circumstance bonus to damage rolls against creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
  - name: "Moon Frenzy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
sourcebook: "_Monster Core_, page 346."
```

```encounter-table
name: Werebear
creatures:
  - 1: Werebear
```
