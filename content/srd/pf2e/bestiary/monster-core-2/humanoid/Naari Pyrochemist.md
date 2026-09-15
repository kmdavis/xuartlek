---
noteType: pf2eMonster
aliases: "Naari Pyrochemist"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/naari
  - pf2e/creature/trait/medium
statblock: inline
name: "Naari Pyrochemist"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4507"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Naari Pyrochemist"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Naari"
modifier: 3
perception:
  - name: "Perception"
    desc: "+3"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +3, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +3, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +6"
abilityMods: [0, 3, 2, 3, 0, 1]
abilities_top:
  - name: "Alchemical Items"
    desc: "A naari pyrochemist carries 5 [[srd/pf2e/compendium/equipment/alchemical-items/Alchemist's Fire|lesser alchemist's fires]], 2 [[srd/pf2e/compendium/equipment/alchemical-items/Elixir of Life|minor elixirs of life]] (GM Core 247), and a [[srd/pf2e/compendium/equipment/alchemical-items/Smoke Ball|lesser smoke ball]]. The pyrochemist replenishes these each day using alchemical reagents during their daily preparations."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Alchemist's Toolkit|Alchemist's Toolkit]], Dagger, Flint and Steel, formula book, studded leather"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +6; __Will__: +3"
hp: 18
health:
  - name: "HP"
    desc: "18; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 1"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4 piercing"
  - name: "Ranged"
    desc: "⬻ lesser alchemist's fire +8 (range increment 30 feet) __Damage__ 1d8 fire plus 1 persistent fire damage and 1 fire [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage"
abilities_bot:
  - name: "Quick Bomber"
    desc: "⬻ The naari pyrochemist draws an alchemist's fire with an Interact action and throws it as a ranged Strike. Geniekin Parentage Planar scions from the elemental planes are known as geniekin because they're overwhelmingly born from couplings between mortals and genies: naaris are born of ifrit, oreads of jabalis, sulis of jann, sylphs of jaathoom, and undines of faydhaans. Despite this distinguished ancestry, geniekin do not display most of their parents' exceptional talents."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]]"
sourcebook: "_Monster Core 2_, page 250."
```

```encounter-table
name: Naari Pyrochemist
creatures:
  - 1: Naari Pyrochemist
```
