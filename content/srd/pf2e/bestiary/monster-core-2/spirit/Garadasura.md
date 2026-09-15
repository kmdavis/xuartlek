---
noteType: pf2eMonster
aliases: "Garadasura"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/asura
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Garadasura"
level: 11
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4087"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Garadasura"
level: "Creature 11"
size: "Huge"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]]; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +21, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +21, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +23"
abilityMods: [6, 3, 6, 0, 2, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/Scimitar|scimitar]]_ (2), Breastplate"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +20; __Will__: +19"
hp: 200
health:
  - name: "HP"
    desc: "200 (fast healing 5); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curses]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 10"
abilities_mid:
  - name: "Encircling Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 50 feet. A garadasura exudes a 50-foot aura whenever it remains motionless for at least 1 round. If the garadasura has the [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] trait, all allied creatures within the area gain a +1 status bonus to AC and saving throws. If the garadasura has the [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] trait, all unallied creatures that enter this area must succeed at a DC 30 Will save or spend their next action to move toward the garadasura's location. If the garadasura moves, the effect ends for all currently affected creatures."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+9 slashing plus 2d6 persistent poison and 1d6 spirit"
  - name: "Melee"
    desc: "⬻ fangs +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+9 piercing plus butchering venom and 1d6 spirit"
  - name: "Melee"
    desc: "⬻ tail +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+9 bludgeoning plus 1d6 spirit and Grab"
  - name: "Ranged"
    desc: "⬻ venom spit +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], range 60 feet) __Damage__ 2d6+6 poison plus butchering venom"
abilities_bot:
  - name: "Butchering Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 30 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 2"
    desc: "4d6 poison damage and slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "6d6 damage and [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] for 1 hour"
  - name: "Constrict"
    desc: "⬻ 2d6+7 bludgeoning, DC 30"
  - name: "Glorious Visage"
    desc: "⬻ The asura sanctifies themselves as either [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]], gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 10 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Slither"
    desc: "⬻ The garadasura [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swims]] up to half its Speed, pulling any creatures it has [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] with it."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]]) Large, 2d10+9 bludgeoning, Rupture 30"
sourcebook: "_Monster Core 2_, page 44."
```

```encounter-table
name: Garadasura
creatures:
  - 1: Garadasura
```
