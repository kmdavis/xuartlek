---
obsidianUIMode: preview
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
aon_id: "creature-4307"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4307"
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
    desc: "Perception +26; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +29, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +28, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +26, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +28"
abilityMods: [8, 3, 9, 6, 5, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +30; __Ref__: +23; __Will__: +26 +1 status to all saves vs. magic"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Miasma of Pollution"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]) 30 feet. A creature that enters the aura or begins its turn in it must succeed at a DC 34 Fortitude save or be [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 2 (plus [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 as long as it's sickened on a critical failure). Creatures in the aura can't reduce the value of the sickened condition. A creature that succeeds at its save is temporarily immune for 1 minute. Creatures made of water (such as [[srd/pf2e/compendium/gm/creature-families/elemental-water|water elementals]]) and [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]] creatures use an outcome one degree of success worse than the result of their save."
speed: "30 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d8+16 bludgeoning plus pollution infusion"
abilities_bot:
  - name: "Pollution Infusion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/virulent|virulent]]) Non-[[srd/pf2e/compendium/rules-elements/traits/player-core/fiend|fiend]] creatures adjacent to the afflicted creature take a –1 circumstance penalty to saving throws against disease"
  - name: "Saving Throw"
    desc: "DC 36 Fortitude"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1 and drained 1 (1 day)"
  - name: "Stage 3"
    desc: "doomed 1 and drained 2 (1 day)"
  - name: "Stage 4"
    desc: "doomed 2 and drained 2 (1 week)"
  - name: "Stage 5"
    desc: "dead"
  - name: "Retch of Foulness"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) The sordesdaemon exhales a spray of sewage that deals 8d6 acid damage and 8d6 poison damage in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save). It can't use Retch of Foulness again for 1d4 rounds. Daemonic Pollution Sordesdaemons who aren't compelled to pursue a specific task often find their way into sewers beneath large cities, where they subjugate other creatures that wallow in filth (such as ofalths). They think nothing of sacrificing these minions if it advances their own aims."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-5/toxic-cloud|Toxic Cloud]] (at will), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/desiccate|Desiccate]], [[srd/pf2e/compendium/spells/rank-8/spiritual-epidemic|Spiritual Epidemic]]"
sourcebook: "_Monster Core 2_, page 81."
```

```encounter-table
name: Sordesdaemon
creatures:
  - 1: Sordesdaemon
```
