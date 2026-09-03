---
obsidianUIMode: preview
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
aon_id: "creature-3005"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3005"
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
    desc: "Perception +16; (18 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) darkvision, wavesense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]], [[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +18, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +20, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18"
abilityMods: [4, 5, 2, 1, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/spear/trident|trident]]_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +18; __Will__: +18"
hp: 145
health:
  - name: "HP"
    desc: "145; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Turbulent Seas"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) 40 feet. Water in the aura that is also in the same body of water as the faydhaan is difficult terrain for [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swimming]]creatures. Creatures with the [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] trait are immune."
speed: "25 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _trident_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The faydhaan transforms into a Small or Medium [[srd/pf2e/compendium/gm/creature-families/elemental-water|water elemental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aquatic|aquatic]] [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animal]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]]. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Gift of Hospitality"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The faydhaan gives another willing creature a magical gift or an agreeable conversation. The creature gains a +2 status bonus to [[srd/pf2e/compendium/rules-elements/skills/society|Society]] and [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks. A creature can't have more than one gift at a time, and a faydhaan can't grant more than one gift at a time. The gift ends if the target acts hostile, or if the faydhaan renounces the recipient (a single action)."
  - name: "Skewer"
    desc: "⬻ The faydhaan makes a trident Strike, dealing an extra 2d6 persistent bleed damage on a hit (4d6 on a critical hit). Faydhaan Shuyookhs Faydhaan shuyookhs grant wishes in ways that please the most people possible. They add the following innate spells: __7th__ [[srd/pf2e/compendium/spells/rank-4/hydraulic-torrent|_hydraulic torrent_]], [[srd/pf2e/compendium/spells/rank-7/planar-palace|_planar palace_]], [[srd/pf2e/compendium/spells/rank-2/summon-elemental|_summon elemental_]]; __5th__ [[srd/pf2e/compendium/spells/rank-5/howling-blizzard|_howling blizzard_]] (at will), [[srd/pf2e/compendium/spells/rank-2/illusory-creature|_illusory creature_]] (×2), [[srd/pf2e/compendium/spells/rank-4/mirage|_mirage_]], [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]] (at will); __4th__ [[srd/pf2e/compendium/spells/rank-2/invisibility|_invisibility_]] (×2), [[srd/pf2e/compendium/spells/rank-4/vapor-form|_vapor form_]]; __2nd__ [[srd/pf2e/compendium/spells/rank-1/create-water|_create water_]] (at will), [[srd/pf2e/compendium/spells/rank-2/invisibility|_invisibility_]] (at will), [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|_see the unseen_]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __2nd__ [[srd/pf2e/compendium/spells/rank-1/create-water|Create Water]] (at will), [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (×2), [[srd/pf2e/compendium/spells/rank-2/water-breathing|Water Breathing]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/hydraulic-push|Hydraulic Push]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]] (at will), [[srd/pf2e/compendium/spells/rank-4/hydraulic-torrent|Hydraulic Torrent]], [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/equipment/runes/astral-greater|Astral Plane]]; Elemental Planes; or [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core_, page 158."
```

```encounter-table
name: Faydhaan
creatures:
  - 1: Faydhaan
```
