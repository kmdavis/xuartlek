---
noteType: pf2eMonster
aliases: "Hekatonkheires Titan"
tags:
  - pf2e/creature/level/24
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/titan
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Hekatonkheires Titan"
level: 24
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4584"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hekatonkheires Titan"
level: "Creature 24"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Rare"
trait_03: "Titan"
modifier: 43
perception:
  - name: "Perception"
    desc: "+43; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +42, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +48, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +45, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +41, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +39"
abilityMods: [12, 10, 12, 7, 7, 9]
ac: 52
armorclass:
  - name: "AC"
    desc: "52; __Fort__: +44; __Ref__: +40; __Will__: +37 +4 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]"
hp: 500
health:
  - name: "HP"
    desc: "500; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]"
abilities_mid:
  - name: "Impossible Stature"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 120 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 44 Will save or its movement toward the titan is movement over [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Difficult Terrain|difficult terrain]] (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "⬲ The hekatonkheires gains 99 extra reactions on their turn that they can use only to make Reactive Strikes."
speed: "60 feet, fly 60 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ _empty weapon_ +45 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 50 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P and S]]) __Damage__ 4d12+18 bludgeoning plus 2d12 force"
  - name: "Ranged"
    desc: "⬻ _empty weapon_ +43 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 200 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P and S]]) __Damage__ 4d12+18 bludgeoning plus 2d12 force"
abilities_bot:
  - name: "Demolish Veil"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per month"
  - name: "Trigger"
    desc: "The titan casts [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|_interplanar teleport_]]"
  - name: "Effect"
    desc: "The titan arrives in a storm of shattered planar barriers. This has the effects of a 10th-rank [[srd/pf2e/compendium/spells/rank-9/Wrathful Storm|_wrathful storm_]]."
  - name: "Hundred-Dimension Grasp"
    desc: "⬻ The titan reaches between realities to drag foes closer. They attempt an [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] check and compare the result to the Fortitude DCs of all foes within 120 feet. On a success, a foe is teleported to any square the titan chooses within 120 feet; on a critical success, it's also [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]] for 1 round. The titan can Grab any foe brought within 30 feet as a free action."
  - name: "Hundred-Handed Whirlwind"
    desc: "⬺ The titan overwhelms opponents with blows both conventional and interplanar. They make one empty weapon Strike against each foe within reach. Even on a failed attack (but not a critical failure), the titan deals 24 force damage to the target. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
  - name: "Send Beyond"
    desc: "⬻"
  - name: "Requirements"
    desc: "The titan has a creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]]"
  - name: "Effect"
    desc: "The titan thrusts the creature into a nightmare realm full of lightless hands and eyes. This has the effects of [[srd/pf2e/compendium/spells/rank-8/Quandary|_quandary_]] (DC 48). The titan can't use Send Beyond for 1d4 rounds."
  - name: "Shape Emptiness"
    desc: "⭓ The titan molds a weapon from interstellar darkness. This empty weapon is a _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+3 major striking]] weapon_ in any form. The titan can't be disarmed of this weapon and it deals an additional 2d12 force damage. If Released, an empty weapon vanishes. Hekatonkheires Anatomy Artisans with exceptional skill can harvest a hekatonkheires's black bones before they dissolve upon the titan's death. These bones can be forged into shapeshifting weapons or refined into planar keys that allow travel to esoteric planes."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 48 - __9th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]], [[srd/pf2e/compendium/spells/rank-9/Phantasmagoria|Phantasmagoria]], [[srd/pf2e/compendium/spells/rank-9/Seize Soul|Seize Soul]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
sourcebook: "_Monster Core 2_, page 322."
```

```encounter-table
name: Hekatonkheires Titan
creatures:
  - 1: Hekatonkheires Titan
```
