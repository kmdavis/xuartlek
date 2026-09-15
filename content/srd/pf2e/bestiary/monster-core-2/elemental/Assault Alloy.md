---
noteType: pf2eMonster
aliases: "Assault Alloy"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/small
statblock: inline
name: "Assault Alloy"
level: 13
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4084"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Assault Alloy"
level: "Creature 13"
size: "Small"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +23, [[srd/pf2e/compendium/rules-elements/skills/Lore|Metal Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/Lore|Plane of Metal Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +24"
abilityMods: [4, 7, 5, 8, 6, 4]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +20; __Ref__: +26; __Will__: +23"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 10"
abilities_mid:
  - name: "Metal Manipulation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Metal|metal]]) 30 feet. An assault alloy has control over all unattended metal within the emanation and can use any of this metal as the origin point for their metal needle ranged Strikes."
  - name: "Instinctive Alloy"
    desc: "⬲"
  - name: "Trigger"
    desc: "The assault alloy is hit by an attack with a metal weapon or metal spell or effect"
  - name: "Effect"
    desc: "The physical damage from the triggering weapon, spell, or effect instead restores the assault alloy's Hit Points as they seamlessly incorporate some of the metal used into their body. If already at full Hit Points, the assault alloy gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Temporary Hit Points|temporary Hit Points]] that last for 1 round instead. If a metal weapon triggers this, the weapon's die size decreases by one step to a minimum die size of d4 for 1 minute, and that weapon can't trigger Instinctive Alloy again during this time."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]]) __Damage__ 3d10+11 slashing"
  - name: "Ranged"
    desc: "⬻ metal needle +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range increment 60 feet) __Damage__ 3d8+11 piercing plus idle transmutation"
abilities_bot:
  - name: "Idle Transmutation"
    desc: "An assault alloy has full alchemical control over the properties of their metal. Each time they make a metal needle Strike or [[srd/pf2e/books/gm-core/chapter-5-treasure-trove/Activating Items#Cast a Spell|Cast a Spell]] with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Metal|metal]] trait, they choose whether the metal they use is [[srd/pf2e/compendium/equipment/materials/Adamantine|adamantine]], [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]], [[srd/pf2e/compendium/equipment/materials/Dawnsilver|dawnsilver]], or any other solid precious metal."
  - name: "Metal Blink"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Move|Move]])"
  - name: "Requirements"
    desc: "The assault alloy is adjacent to metal of at least 1 bulk"
  - name: "Effect"
    desc: "An assault alloy can liquefy the metals of their body and travel up to their Speed through spaces with contiguous metal, even if it's not uniformly connected (as in a scrap heap or a pile of treasure). This movement doesn't trigger reactions. The Hoarder's Scourge Assault alloys are constantly in search of ever greater sources of metal to use in their experiments. Bankers, armorers, smiths, scrap dealers, and even dragons are all wary of an assault alloy settling in among their assets. They often handsomely pay any adventurers capable of rooting out the dangerous pests."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Metal|Detect Metal]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Rust Cloud|Rust Cloud]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Impaling Spike|Impaling Spike]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/Wall of Metal|Wall of Metal]]"
sourcebook: "_Monster Core 2_, page 41."
```

```encounter-table
name: Assault Alloy
creatures:
  - 1: Assault Alloy
```
