---
obsidianUIMode: preview
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
aon_id: "creature-4084"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4084"
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
    desc: "Perception +26; darkvision"
languages: "Common, Talican"
skills:
  - name: "Skills"
    desc: "Arcana +27, Athletics +23, Crafting +23, Metal Lore +29, Plane of Metal Lore +29, Stealth +22, Thievery +24"
abilityMods: [4, 7, 5, 8, 6, 4]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +20; __Ref__: +26; __Will__: +23"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ electricity 10"
abilities_mid:
  - name: "Metal Manipulation"
    desc: "(aura, metal) 30 feet. An assault alloy has control over all unattended metal within the emanation and can use any of this metal as the origin point for their metal needle ranged Strikes."
  - name: "Instinctive Alloy"
    desc: "⬲"
  - name: "Trigger"
    desc: "The assault alloy is hit by an attack with a metal weapon or metal spell or effect"
  - name: "Effect"
    desc: "The physical damage from the triggering weapon, spell, or effect instead restores the assault alloy's Hit Points as they seamlessly incorporate some of the metal used into their body. If already at full Hit Points, the assault alloy gains temporary Hit Points that last for 1 round instead. If a metal weapon triggers this, the weapon's die size decreases by one step to a minimum die size of d4 for 1 minute, and that weapon can't trigger Instinctive Alloy again during this time."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +27 (Agile, Finesse) __Damage__ 3d10+11 slashing"
  - name: "Ranged"
    desc: "⬻ metal needle +27 (Agile, Arcane, Magical, range increment 60 feet) __Damage__ 3d8+11 piercing plus idle transmutation"
abilities_bot:
  - name: "Idle Transmutation"
    desc: "An assault alloy has full alchemical control over the properties of their metal. Each time they make a metal needle Strike or Cast a Spell with the metal trait, they choose whether the metal they use is adamantine, cold iron, dawnsilver, or any other solid precious metal."
  - name: "Metal Blink"
    desc: "⬻ (Move)"
  - name: "Requirements"
    desc: "The assault alloy is adjacent to metal of at least 1 bulk"
  - name: "Effect"
    desc: "An assault alloy can liquefy the metals of their body and travel up to their Speed through spaces with contiguous metal, even if it's not uniformly connected (as in a scrap heap or a pile of treasure). This movement doesn't trigger reactions. The Hoarder's Scourge Assault alloys are constantly in search of ever greater sources of metal to use in their experiments. Bankers, armorers, smiths, scrap dealers, and even dragons are all wary of an assault alloy settling in among their assets. They often handsomely pay any adventurers capable of rooting out the dangerous pests."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33 - __Cantrips (3rd)__ Detect Metal - __4th__ Rust Cloud - __5th__ Impaling Spike - __6th__ Wall of Metal"
sourcebook: "_Monster Core 2_, page 41."
```

```encounter-table
name: Assault Alloy
creatures:
  - 1: Assault Alloy
```
