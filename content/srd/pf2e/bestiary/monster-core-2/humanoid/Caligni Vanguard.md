---
noteType: pf2eMonster
aliases: "Caligni Vanguard"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Caligni Vanguard"
level: 5
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4288"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Caligni Vanguard"
level: "Creature 5"
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; echolocation 60 feet, no vision"
languages: "Caligni, [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8"
abilityMods: [5, -1, 3, 1, 4, 1]
abilities_top:
  - name: "Echolocation"
    desc: "A caligni vanguard can use their hearing as a precise sense at the listed range."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/bow/Composite Longbow|Composite Longbow]] (40 arrows), [[srd/pf2e/compendium/equipment/Armor#Full Plate|Full Plate]] (see death blaze), [[srd/pf2e/compendium/equipment/weapons/sword/Greatsword|Greatsword]]"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +8; __Will__: +11"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]] 5 Resistances slashing 5"
abilities_mid:
  - name: "Death Blaze"
    desc: "When the vanguard dies, their body combusts in a blaze of fire and armor shrapnel. All creatures within a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] take 3d6 fire damage and 3d6 piercing damage (DC 19 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The vanguard's armor is destroyed in the blaze, but their other gear is unaffected and left in a pile where they died."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greatsword +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d12+8 slashing"
  - name: "Ranged"
    desc: "⬻ composite longbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "Call to Arms"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) Each [[srd/pf2e/compendium/rules-elements/traits/monster-core/Caligni|caligni]] within 30 feet of the vanguard gains the Reactive Strike reaction until the end of the vanguard's next turn. Once a caligni has used this Reactive Strike, that caligni is temporarily immune to the same vanguard's Call to Arms for 10 minutes."
  - name: "Shadowed Blade"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Darkness|Darkness]]) The vanguard makes a melee Strike, channeling shadowy essence into their weapon or unarmed attack to envelop the target. If the Strike hits, the target must succeed at a DC 19 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] until the end of its next turn. Vanguard Training As soon as a caligni vanguard is old enough to hold a weapon, they're immersed in an intensive training regimen that emphasizes austerity, asceticism, and heavy armor prowess. Though initially painful, the fusion of their armor to their bodies serves as a reminder of their responsibilities, and they eventually grow accustomed to the sensation."
sourcebook: "_Monster Core 2_, page 64."
```

```encounter-table
name: Caligni Vanguard
creatures:
  - 1: Caligni Vanguard
```
