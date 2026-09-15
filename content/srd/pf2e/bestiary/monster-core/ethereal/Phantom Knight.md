---
noteType: pf2eMonster
aliases: "Phantom Knight"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/phantom
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Phantom Knight"
level: 4
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3135"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Phantom Knight"
level: "Creature 4"
size: "Medium"
trait_01: "Ethereal"
trait_02: "Incorporeal"
trait_03: "Phantom"
trait_04: "Spirit"
trait_05: "Uncommon"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +12"
abilityMods: [-5, 4, 0, 0, 5, 4]
abilities_top:
  - name: "Walk the Ethereal Line"
    desc: "⬺ The phantom walks the thin line between the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]] and [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] in order to exist on both planes simultaneously. They can shift back to solely the Ethereal Plane by using this ability again."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +12; __Will__: +13 –1 status penalty to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], precision; __Resistances__ all damage 3 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]], [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]]; double resistance vs. non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]])"
abilities_mid:
  - name: "Susceptible to Death"
    desc: "Though phantoms aren't alive, neither are they [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]], and they are uniquely vulnerable to the effects of death. A phantom whose Hit Points are reduced to 0 as a result of a [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effect (such as from a spell like [[srd/pf2e/compendium/spells/rank-7/Execute|_execute_]]) is immediately whisked away to the River of Souls, where their soul resumes the usual path to the afterlife."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ phantom sword +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d8+7 slashing"
  - name: "Ranged"
    desc: "⬻ phantom bow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range increment 120 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "Phantom Touch"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) Each time they make a Strike, a phantom can choose to deal [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] damage instead of the normal physical damage type."
sourcebook: "_Monster Core_, page 262."
```

```encounter-table
name: Phantom Knight
creatures:
  - 1: Phantom Knight
```
