---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urveth"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Urveth"
level: 18
source: "Monster Core 2"
aon_id: "creature-4312"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4312"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urveth"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; greater darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +29, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +35, [[srd/pf2e/compendium/rules-elements/skills/lore|Netherworld Lore]] +31, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +32, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +31, [[srd/pf2e/compendium/rules-elements/skills/lore|Void Lore]] +31"
abilityMods: [10, 5, 8, 5, 6, 6]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +32; __Ref__: +29; __Will__: +34"
hp: 460
health:
  - name: "HP"
    desc: "460 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], disease, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15, [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]] 15"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) 60 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 5d6 void damage with a DC 38 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save. If it fails, it's also [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 as long as it remains in the sunlight."
  - name: "Reactive Strike"
    desc: "⬲ claw only. An urveth gains 3 extra reactions each round that they can use only to make Reactive Strikes."
speed: "25 feet, burrow 60 feet, fly"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+14 slashing plus 2d10 cold and Improved Grab"
  - name: "Melee"
    desc: "⬻ claw +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d6+14 slashing plus 2d10 cold"
  - name: "Melee"
    desc: "⬻ stinger +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d6+14 piercing plus 2d10 cold and urveth venom"
abilities_bot:
  - name: "Frenzy"
    desc: "⬺ The urveth makes two claw Strikes and one stinger Strike in any order."
  - name: "Swallow Whole"
    desc: "⬻ Huge, 2d10+5 bludgeoning, Rupture 35. A living creature that ends its turn swallowed whole by an urveth becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 or increases its drained condition by 1, and the urveth gains 10 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]]. A creature whose drained condition increases to 5 in this way dies."
  - name: "Urveth Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) Saving Throw DC 37 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 void damage and 2d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "3d6 void damage, 2d6 poison damage, and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 2 (1 round)"
  - name: "Stage 3"
    desc: "3d6 void damage, 2d6 poison damage, and enfeebled 4 (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×3), [[srd/pf2e/compendium/spells/rank-7/eclipse-burst|Eclipse Burst]], [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]]; [[srd/pf2e/compendium/gm/planes#The Void|the Void]]; or [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]] only), [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-4/fly|Fly]]"
sourcebook: "_Monster Core 2_, page 86."
```

```encounter-table
name: Urveth
creatures:
  - 1: Urveth
```
