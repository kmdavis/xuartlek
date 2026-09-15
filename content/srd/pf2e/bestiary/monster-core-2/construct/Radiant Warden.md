---
noteType: pf2eMonster
aliases: "Radiant Warden"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Radiant Warden"
level: 17
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4526"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Radiant Warden"
level: "Creature 17"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "+30; darkvision"
languages: "any one ancient language (such as Jistkan)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +32, [[srd/pf2e/compendium/rules-elements/skills/Lore|Astronomy Lore]] +36, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +32"
abilityMods: [9, 6, 5, 6, 5, 0]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +32; __Ref__: +29; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], disease, [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Damage Rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Resistances__ mental 15, physical 15 (except [[srd/pf2e/compendium/equipment/materials/Adamantine|adamantine]])"
abilities_mid:
  - name: "Gatekeeper Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) 60 feet. A creature that uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] ability within the aura's [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] or enters it via a teleportation ability must succeed a DC 38 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 and have its destination changed to a point of the radiant warden's choosing within the aura. On a successful save, the creature arrives as intended but is still sickened 1."
speed: "30 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hammer +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|shove]]) __Damage__ 3d12+15 bludgeoning plus radiant blow"
  - name: "Ranged"
    desc: "⬻ radiant beam +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Force|Force]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], range increment 30 feet) __Damage__ 4d10+6 force"
abilities_bot:
  - name: "Orrery"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) Until it acts, the radiant warden appears to be an orrery (or similar large mechanical contraption, such as a telescope). It has an automatic result of 53 on [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] checks and DCs to convincingly pass as such a machine."
  - name: "Radiant Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Force|Force]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) The radiant warden releases a 50-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of bright energy that deals 10d12 force damage (DC 38 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Reflex save). The radiant warden can't use Radiant Blast for 1d4 rounds."
  - name: "Radiant Blow"
    desc: "When a creature is hit by the radiant warden's hammer Strike, a flash of radiant energy attempts to anchor the creature in place. The creature must attempt a DC 38 Will save; on a failure, the creature can't use any [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]] effects for 1 minute. On a critical failure, the creature is also permanently [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]]. Ancient Intellects Each radiant warden's animating force consists of raw vitality energy fused to the soul of a willing sacrifice—usually an astronomer or scholar near the end of their natural life. Focused now on protecting a site from any intrusion— including by curious archaeologists or adventurers—a radiant warden might pause before an attack if approached peacefully. Unfortunately, these constructs are prone to speaking in vague riddles or complex mathematical diatribes that can be as confusing as they are intriguing. Often, discussions break down as frustration mounts on either side (or both)."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 38 - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Planar Seal|Planar Seal]], [[srd/pf2e/compendium/spells/rank-6/Wall of Force|Wall of Force]] - __8th__ [[srd/pf2e/compendium/spells/rank-6/Collective Transposition|Collective Transposition]] (×3), [[srd/pf2e/compendium/spells/rank-8/Pinpoint|Pinpoint]] - __9th__ [[srd/pf2e/compendium/spells/rank-6/Teleport|Teleport]]"
sourcebook: "_Monster Core 2_, page 266."
```

```encounter-table
name: Radiant Warden
creatures:
  - 1: Radiant Warden
```
