---
obsidianUIMode: preview
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
aon_id: "creature-4584"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4584"
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
    desc: "Perception +43; darkvision, _truesight_"
languages: "Aklo, Chthonian, Common, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +42, Athletics +48, Intimidation +45, Occultism +41, Survival +39"
abilityMods: [12, 10, 12, 7, 7, 9]
ac: 52
armorclass:
  - name: "AC"
    desc: "52; __Fort__: +44; __Ref__: +40; __Will__: +37 +4 status to all saves vs. mental or divine"
hp: 500
health:
  - name: "HP"
    desc: "500; __Immunities__ death effects, disease"
abilities_mid:
  - name: "Impossible Stature"
    desc: "(aura, illusion, occult, mental) 120 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 44 Will save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "⬲ The hekatonkheires gains 99 extra reactions on their turn that they can use only to make Reactive Strikes."
speed: "60 feet, fly 60 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ _empty weapon_ +45 (Magical, reach 50 feet, versatile P and S) __Damage__ 4d12+18 bludgeoning plus 2d12 force"
  - name: "Ranged"
    desc: "⬻ _empty weapon_ +43 (Magical, thrown 200 feet, versatile P and S) __Damage__ 4d12+18 bludgeoning plus 2d12 force"
abilities_bot:
  - name: "Demolish Veil"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per month"
  - name: "Trigger"
    desc: "The titan casts _interplanar teleport_"
  - name: "Effect"
    desc: "The titan arrives in a storm of shattered planar barriers. This has the effects of a 10th-rank _wrathful storm_."
  - name: "Hundred-Dimension Grasp"
    desc: "⬻ The titan reaches between realities to drag foes closer. They attempt an Athletics check and compare the result to the Fortitude DCs of all foes within 120 feet. On a success, a foe is teleported to any square the titan chooses within 120 feet; on a critical success, it's also paralyzed for 1 round. The titan can Grab any foe brought within 30 feet as a free action."
  - name: "Hundred-Handed Whirlwind"
    desc: "⬺ The titan overwhelms opponents with blows both conventional and interplanar. They make one empty weapon Strike against each foe within reach. Even on a failed attack (but not a critical failure), the titan deals 24 force damage to the target. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
  - name: "Send Beyond"
    desc: "⬻"
  - name: "Requirements"
    desc: "The titan has a creature grabbed or restrained"
  - name: "Effect"
    desc: "The titan thrusts the creature into a nightmare realm full of lightless hands and eyes. This has the effects of _quandary_ (DC 48). The titan can't use Send Beyond for 1d4 rounds."
  - name: "Shape Emptiness"
    desc: "⭓ The titan molds a weapon from interstellar darkness. This empty weapon is a _+3 major striking weapon_ in any form. The titan can't be disarmed of this weapon and it deals an additional 2d12 force damage. If Released, an empty weapon vanishes. Hekatonkheires Anatomy Artisans with exceptional skill can harvest a hekatonkheires's black bones before they dissolve upon the titan's death. These bones can be forged into shapeshifting weapons or refined into planar keys that allow travel to esoteric planes."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 48 - __9th__ Interplanar Teleport, Phantasmagoria, Seize Soul, Translocate - __Constant (10th)__ Truesight, Unfettered Movement"
sourcebook: "_Monster Core 2_, page 322."
```

```encounter-table
name: Hekatonkheires Titan
creatures:
  - 1: Hekatonkheires Titan
```
