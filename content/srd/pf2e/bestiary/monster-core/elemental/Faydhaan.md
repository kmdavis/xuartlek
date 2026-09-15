---
noteType: pf2eMonster
aliases: "Faydhaan"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Faydhaan"
level: 9
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3005"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Faydhaan"
level: "Creature 9"
size: "Large"
trait_01: "Elemental"
trait_02: "Genie"
trait_03: "Water"
modifier: 16
perception:
  - name: "Perception"
    desc: "+16; (18 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) darkvision, wavesense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]], [[srd/pf2e/compendium/rules-elements/Languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/Languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +16, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +18, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +20, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +18"
abilityMods: [4, 5, 2, 1, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/Trident|trident]]_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +18; __Will__: +18"
hp: 145
health:
  - name: "HP"
    desc: "145; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10"
abilities_mid:
  - name: "Turbulent Seas"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]]) 40 feet. Water in the aura that is also in the same body of water as the faydhaan is difficult terrain for [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swimming]]creatures. Creatures with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]] trait are immune."
speed: "25 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d8+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _trident_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The faydhaan transforms into a Small or Medium [[srd/pf2e/compendium/gm/creature-families/Elemental, Water|water elemental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Aquatic|aquatic]] [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Gift of Hospitality"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The faydhaan gives another willing creature a magical gift or an agreeable conversation. The creature gains a +2 status bonus to [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] and [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] checks. A creature can't have more than one gift at a time, and a faydhaan can't grant more than one gift at a time. The gift ends if the target acts hostile, or if the faydhaan renounces the recipient (a single action)."
  - name: "Skewer"
    desc: "⬻ The faydhaan makes a trident Strike, dealing an extra 2d6 persistent bleed damage on a hit (4d6 on a critical hit). Faydhaan Shuyookhs Faydhaan shuyookhs grant wishes in ways that please the most people possible. They add the following innate spells: __7th__ [[srd/pf2e/compendium/spells/rank-4/Hydraulic Torrent|_hydraulic torrent_]], [[srd/pf2e/compendium/spells/rank-7/Planar Palace|_planar palace_]], [[srd/pf2e/compendium/spells/rank-2/Summon Elemental|_summon elemental_]]; __5th__ [[srd/pf2e/compendium/spells/rank-5/Howling Blizzard|_howling blizzard_]] (at will), [[srd/pf2e/compendium/spells/rank-2/Illusory Creature|_illusory creature_]] (×2), [[srd/pf2e/compendium/spells/rank-4/Mirage|_mirage_]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]] (at will); __4th__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|_invisibility_]] (×2), [[srd/pf2e/compendium/spells/rank-4/Vapor Form|_vapor form_]]; __2nd__ [[srd/pf2e/compendium/spells/rank-1/Create Water|_create water_]] (at will), [[srd/pf2e/compendium/spells/rank-2/Invisibility|_invisibility_]] (at will), [[srd/pf2e/compendium/spells/rank-2/See the Unseen|_see the unseen_]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/Create Water|Create Water]] (at will), [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×2), [[srd/pf2e/compendium/spells/rank-2/Water Breathing|Water Breathing]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|Hydraulic Push]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]] (at will), [[srd/pf2e/compendium/spells/rank-4/Hydraulic Torrent|Hydraulic Torrent]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/equipment/runes/Astral|Astral Plane]]; Elemental Planes; or [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 158."
```

```encounter-table
name: Faydhaan
creatures:
  - 1: Faydhaan
```
