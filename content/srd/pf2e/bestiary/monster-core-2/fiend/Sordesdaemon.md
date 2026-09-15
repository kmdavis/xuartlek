---
noteType: pf2eMonster
aliases: "Sordesdaemon"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Sordesdaemon"
level: 15
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4307"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sordesdaemon"
level: "Creature 15"
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "+26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +29, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +26, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +24, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +28"
abilityMods: [8, 3, 9, 6, 5, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +30; __Ref__: +23; __Will__: +26 +1 status to all saves vs. magic"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Miasma of Pollution"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]) 30 feet. A creature that enters the aura or begins its turn in it must succeed at a DC 34 Fortitude save or be [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 2 (plus [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 as long as it's sickened on a critical failure). Creatures in the aura can't reduce the value of the sickened condition. A creature that succeeds at its save is temporarily immune for 1 minute. Creatures made of water (such as [[srd/pf2e/compendium/gm/creature-families/Elemental, Water|water elementals]]) and [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]] creatures use an outcome one degree of success worse than the result of their save."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 3d8+16 bludgeoning plus pollution infusion"
abilities_bot:
  - name: "Pollution Infusion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/Virulent|virulent]]) Non-[[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiend]] creatures adjacent to the afflicted creature take a –1 circumstance penalty to saving throws against disease"
  - name: "Saving Throw"
    desc: "DC 36 Fortitude"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 1 (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]] 1 and drained 1 (1 day)"
  - name: "Stage 3"
    desc: "doomed 1 and drained 2 (1 day)"
  - name: "Stage 4"
    desc: "doomed 2 and drained 2 (1 week)"
  - name: "Stage 5"
    desc: "dead"
  - name: "Retch of Foulness"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) The sordesdaemon exhales a spray of sewage that deals 8d6 acid damage and 8d6 poison damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] (DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save). It can't use Retch of Foulness again for 1d4 rounds. Daemonic Pollution Sordesdaemons who aren't compelled to pursue a specific task often find their way into sewers beneath large cities, where they subjugate other creatures that wallow in filth (such as ofalths). They think nothing of sacrificing these minions if it advances their own aims."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Toxic Cloud|Toxic Cloud]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/Desiccate|Desiccate]], [[srd/pf2e/compendium/spells/rank-8/Spiritual Epidemic|Spiritual Epidemic]]"
sourcebook: "_Monster Core 2_, page 81."
```

```encounter-table
name: Sordesdaemon
creatures:
  - 1: Sordesdaemon
```
