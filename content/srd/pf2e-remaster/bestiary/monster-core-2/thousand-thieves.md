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
languages: "Aklo, Common, Sakvroth, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Deception +28, Occultism +26, Society +28, Stealth +32, Thievery +32, Underworld Lore +30"
abilityMods: [4, 8, 7, 6, 5, 4]
abilities_top:
  - name: "Items"
    desc: "_+2 greater striking dagger_, sterling thieves' toolkit"
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +25; __Ref__: +31; __Will__: +27"
hp: 220
health:
  - name: "HP"
    desc: "220; __Immunities__ precision, swarm mind; __Resistances__ physical 15, poison 15; __Weaknesses__ area damage 15, splash damage 15"
abilities_mid:
  - name: "Discorporate"
    desc: "When the thousand thieves is reduced to 0 HP, their constituent creatures collapse, scattering on the ground under their space and each adjacent square. If even one of the creatures gets away, the thousand thieves can eventually re-form over 1d10 days (potentially longer in areas where there are few invertebrates). The scattered invertebrates must be destroyed within 1 round to destroy the thousand thieves permanently. The invertebrates have a collective pool of HP, typically equal to 55 HP, and the same AC, saves, immunities, resistances, and weaknesses as the thousand thieves. The invertebrates can't take actions but they escape automatically once the round elapses. At the GM's discretion, clever means of trapping or eliminating the creatures might be sufficient to destroy the thousand thieves."
speed: "35 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +32 (Agile, finesse, versatile S) __Damage__ 3d4+10 piercing plus clinging remnants and liquid delirium"
  - name: "Melee"
    desc: "⬻ fist +32 (Agile, finesse, nonlethal, unarmed) __Damage__ 1d4+10 bludgeoning plus clinging remnants and liquid delirium"
  - name: "Ranged"
    desc: "⬻ _dagger_ +32 (Agile, thrown 10 feet, versatile S) __Damage__ 3d4+10 piercing plus clinging remnants and liquid delirium"
  - name: "Ranged"
    desc: "⬻ vermin dart +30 (range increment 40 feet) __Damage__ 3d8+10 piercing plus clinging remnants and liquid delirium"
abilities_bot:
  - name: "Clinging Remnants"
    desc: "A thousand thieves's melee Strikes and ranged Strikes made against targets within their weapon's first range increment deposit biting vermin on the target, dealing 4d4 persistent piercing damage."
  - name: "Draw Bugs"
    desc: "⬻ (Healing) The thousand thieves draws more arthropods from the environment around them to reconstitute some of their damaged body. They regain 20 HP. At the GM's discretion, the thousand thieves doesn't recover HP in areas where there aren't enough arthropods to call to themselves."
  - name: "Liquid Delirium"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 37 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "4d6 poison and stupefied 1 (1 round)"
  - name: "Stage 2"
    desc: "4d6 poison and stupefied 2 (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison, stupefied 2, and fascinated by a random object (1 round)"
  - name: "Stage 4"
    desc: "unconscious with no Perception check to wake up (1 round)"
  - name: "Scuttling Shift"
    desc: "⬺ The thousand thieves reverts to a swarm using Swarm Getaway, Sneaks up to their Speed, coalesces into their normal form, and Hides. This movement doesn't trigger reactions."
  - name: "Sneak Attack"
    desc: "The thousand thieves deals an additional 3d6 precision damage to off-guard creatures."
  - name: "Squirming Injection"
    desc: "⬻ The thousand thieves Strides. If they end their movement sharing a space with a creature, they deal dealing 6d6 piercing damage (DC 37 basic Reflex save) and exposing the target to liquid delirium. The thousand thieves can Climb instead of Striding."
  - name: "Swarm Getaway"
    desc: "⬻ (Concentrate) The thousand thieves collapses into a shapeless swarm of their constituent creatures. They drops all items in their possession but up to 3 Bulk of held, worn, or carried objects. In this form, the thousand thieves can't use attack actions and can't cast spells, but they can move through areas small enough for their constituent creatures to fit without having to Squeeze. As the swarm moves, the thousand thieves carries their objects if they can fit through the spaces the swarm moves through. The thousand thieves automatically dons any of the objects they desire when they reform. If the thousand thieves is hidden, Swarm Getaway doesn't reveal their location. They can use the same action to coalesce from their swarm shape back into their normal form."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 37 - __Cantrips (6th)__ Detect Magic, Know the Way, Read Aura, Telekinetic Hand - __3rd__ Illusory Disguise (at will) - __6th__ Detect Scrying, Invisibility, Knock"
sourcebook: "_Monster Core 2_, page 313."
```

```encounter-table
name: Thousand Thieves
creatures:
  - 1: Thousand Thieves
```
