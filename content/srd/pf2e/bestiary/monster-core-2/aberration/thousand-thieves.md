---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thousand Thieves"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Thousand Thieves"
level: 16
source: "Monster Core 2"
aon_id: "creature-4573"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4573"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Thousand Thieves"
level: "Creature 16"
size: "Medium"
trait_01: "Aberration"
trait_02: "Swarm"
trait_03: "Uncommon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +26, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +28, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +32, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +32, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +30"
abilityMods: [4, 8, 7, 6, 5, 4]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+2 greater striking]] [[srd/pf2e/compendium/equipment/weapons/knife/dagger|dagger]]_, [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|sterling thieves' toolkit]]"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +25; __Ref__: +31; __Will__: +27"
hp: 220
health:
  - name: "HP"
    desc: "220; __Immunities__ precision, swarm mind; __Resistances__ physical 15, poison 15; __Weaknesses__ area damage 15, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 15"
abilities_mid:
  - name: "Discorporate"
    desc: "When the thousand thieves is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the thousand thieves can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the thousand thieves permanently. The invertebrates have a collective pool of HP, typically equal to 55 HP, and the same AC, saves, immunities, resistances, and weaknesses as the thousand thieves. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the thousand thieves."
speed: "35 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 3d4+10 piercing plus clinging remnants and liquid delirium"
  - name: "Melee"
    desc: "⬻ fist +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 1d4+10 bludgeoning plus clinging remnants and liquid delirium"
  - name: "Ranged"
    desc: "⬻ _dagger_ +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 3d4+10 piercing plus clinging remnants and liquid delirium"
  - name: "Ranged"
    desc: "⬻ vermin dart +30 (range increment 40 feet) __Damage__ 3d8+10 piercing plus clinging remnants and liquid delirium"
abilities_bot:
  - name: "Clinging Remnants"
    desc: "A thousand thieves's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 4d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent piercing damage]]."
  - name: "Draw Bugs"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|Healing]]) The thousand thieves draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 20 HP. At the GM's discretion, the thousand thieves doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Liquid Delirium"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 37 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "4d6 poison and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (1 round)"
  - name: "Stage 2"
    desc: "4d6 poison and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison, stupefied 2, and [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by a random object (1 round)"
  - name: "Stage 4"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] with no [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] check to wake up (1 round)"
  - name: "Scuttling Shift"
    desc: "⬺ The thousand thieves reverts to a swarm using Swarm Getaway, [[srd/pf2e/compendium/rules-elements/actions/player-core#Sneak|Sneaks]] up to their Speed, coalesces into their normal form, and [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hides]]. This movement doesn't trigger reactions."
  - name: "Sneak Attack"
    desc: "The thousand thieves deals an additional 3d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Squirming Injection"
    desc: "⬻ The thousand thieves [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]]. If they end their movement sharing a space with a creature, they deal dealing 6d6 piercing damage (DC 37 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) and exposing the target to liquid delirium. The thousand thieves can [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climb]] instead of Striding."
  - name: "Swarm Getaway"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The thousand thieves collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession but up to 3 Bulk of held, worn, or carried objects. In this form, the thousand thieves can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]]. As the swarm moves, the thousand thieves carries their objects if they can fit through the spaces the swarm moves through. The thousand thieves automatically dons any of the objects they desire when they reform. If the thousand thieves is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], Swarm Getaway doesn't reveal their location. They can use the same action to coalesce from their swarm shape back into their normal form."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/know-the-way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-4/detect-scrying|Detect Scrying]], [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/knock|Knock]]"
sourcebook: "_Monster Core 2_, page 313."
```

```encounter-table
name: Thousand Thieves
creatures:
  - 1: Thousand Thieves
```
