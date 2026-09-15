---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3237"
socialImage: og-image.png
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
    desc: "+11; low-light vision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; bear empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +9, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +11"
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
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 1d10+7 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ greataxe +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d12+7 slashing"
  - name: "Melee"
    desc: "⬻ hatchet +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ jaws +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 1d12+7 piercing plus curse of the werebear"
  - name: "Ranged"
    desc: "⬻ hatchet +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d6+7 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) Medium human with fist +13 for 1d4+7 bludgeoning, or grizzly bear with Speed 35 feet."
  - name: "Curse of the Werebear"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]])"
  - name: "Saving Throw"
    desc: "DC 18 Fortitude"
  - name: "Hunt Prey"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The werebear designates a single creature they can see and hear, or one they're [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Tracking]], as their prey. The werebear gains a +2 circumstance bonus to Perception checks when they [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] their prey and to [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] checks when they Track their prey. The first time the werebear hits the designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the werebear uses Hunt Prey again."
  - name: "Mauler"
    desc: "The werebear gains a +2 circumstance bonus to damage rolls against creatures it has [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]]."
  - name: "Moon Frenzy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]])"
sourcebook: "_Monster Core_, page 346."
```

```encounter-table
name: Werebear
creatures:
  - 1: Werebear
```
