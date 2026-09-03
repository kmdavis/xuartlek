---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nasurgeth"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Nasurgeth"
level: 20
source: "Monster Core 2"
aon_id: "creature-4313"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4313"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nasurgeth"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Darvakka"
trait_03: "Shadow"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; greater darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +36, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +39, [[srd/pf2e/compendium/rules-elements/skills/lore|Netherworld Lore]] +36, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +36, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +34, [[srd/pf2e/compendium/rules-elements/skills/lore|Void Lore]] +36"
abilityMods: [11, 6, 7, 8, 8, 7]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +35; __Ref__: +32; __Will__: +36"
hp: 510
health:
  - name: "HP"
    desc: "510 (void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15, [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]] 15"
abilities_mid:
  - name: "Midnight Depths"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|darkness]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]) 60 feet. A nasurgeth's entropy grows even stronger underwater. All water within the aura is completely dark (as 4th-rank [[srd/pf2e/compendium/spells/rank-2/darkness|_darkness_]]). Magical light with a [[srd/pf2e/books/player-core/chapter-7-spells/counteracting|counteract]] rank of 4th or lower and magical light cantrips are suppressed. A living creature entering or starting its turn in the aura takes 4d6 void damage, and the creature also takes an additional 2d10 cold damage if it's in water (DC 39 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save). If it fails, it's also [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 for 1 minute and pulled 10 feet toward the nasurgeth."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 2 and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 as long as it remains in the sunlight."
  - name: "Spray Black Bile"
    desc: "⬲"
  - name: "Trigger"
    desc: "The nasurgeth takes slashing or piercing damage from a critical hit, or a swallowed creature cuts itself free"
  - name: "Effect"
    desc: "Darkness and death energy spill out from the nasurgeth's wound, dealing 8d8 void damage to creatures in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] with a DC 40 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save."
speed: "fly 60 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+19 piercing plus 2d10 cold and Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d6+19 bludgeoning plus 2d10 cold"
abilities_bot:
  - name: "Broken Barb"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in the nasurgeth's jaws"
  - name: "Effect"
    desc: "The nasurgeth breaks a tooth off in the target, who takes 3d10 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] and is no longer grabbed or restrained. If the target is adjacent to a surface, the tooth also pins it in place, making it immobilized ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 45)."
  - name: "Ravenous Void"
    desc: "⬽ The nasurgeth barrels forward with their mouth open, [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swimming]] twice in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] and moving through the spaces of Huge or smaller creatures. The nasurgeth deals the damage of their jaws Strike to each creature whose space they enter (DC 45 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Any creature that critically fails is automatically Swallowed Whole."
  - name: "Swallow Whole"
    desc: "⬻ Huge, 2d10+9 bludgeoning, Rupture 40. A living creature that ends its turn swallowed whole by a nasurgeth becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 or increases its drained condition by 1, and the nasurgeth gains 20 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Temporary Hit Points|temporary Hit Points]] that last for 10 minutes . A creature whose drained condition increases to 5 in this way dies."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 43 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]]; [[srd/pf2e/compendium/gm/planes#The Void|the Void]]; or [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]] only), [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]] - __8th__ [[srd/pf2e/compendium/spells/rank-7/eclipse-burst|Eclipse Burst]] (×3), [[srd/pf2e/compendium/spells/rank-1/harm|Harm]] (×3)"
sourcebook: "_Monster Core 2_, page 87."
```

```encounter-table
name: Nasurgeth
creatures:
  - 1: Nasurgeth
```
