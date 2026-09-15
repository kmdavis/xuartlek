---
noteType: pf2eMonster
aliases: "Nymolus"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Nymolus"
level: 10
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4025"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nymolus"
level: "Creature 10"
size: "Large"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], Alghollthu, [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +22, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +21, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +19, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +18"
abilityMods: [5, 2, 4, 6, 4, 6]
abilities_top:
  - name: "Inhabit Ugothol"
    desc: "The nymolus spends 10 minutes with a willing [[srd/pf2e/bestiary/monster-core/aberration/Ugothol|ugothol]] to become enmeshed with the creature. The nymolus then fully inhabits the ugothol’s body. While inhabited, the ugothol retains its mental abilities, but its body is completely controlled by the nymolus. The nymolus and ugothol each have an initiative count as if they were separate creatures. The nymolus can’t use any ability that relies on their physical form while inhabiting the ugothol, but the nymolus can still perceive and cast spells normally. The two remain enmeshed until the nymolus uses the ugothol’s Assume Form ability to separate them, or until the ugothol is slain. If the ugothol dies, the nymolus becomes [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] 3 due to the force of the separation."
  - name: "Replace Recollection"
    desc: "The nymolus can spend 10 minutes to replace any memory with another memory they have access to via a memory crystal"
  - name: "Items"
    desc: "3 or more memory crystals"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +20; __Ref__: +15; __Will__: +22"
hp: 190
health:
  - name: "HP"
    desc: "190"
speed: "15 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 2d10+10 bludgeoning plus Grab"
abilities_bot:
  - name: "Extract Memory"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental"
  - name: "Requirements"
    desc: "The target creature must be grabbed]])"
  - name: "Effect"
    desc: "The nymolus reaches into an adjacent creature's memory and extracts up to 10 minutes of the target's experiences, forming them into a memory crystal within the nymolus's brain. The target creature must attempt a DC 27 Will save to avoid losing its memory."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature loses the target memory."
  - name: "Failure"
    desc: "The creature loses the target memory and is [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the creature can only roll to end this condition if it takes damage from the nymolus themself or if counteracted by an effect of at least 13th level or 7th rank."
  - name: "Stunning Pulse"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The nymolus emits a powerful mental pulse that overwhelms nearby creatures. Creatures in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] must attempt a DC 27 Fortitude save to avoid being [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]]. The nymolus can't use Stunning Pulse again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is stunned 1."
  - name: "Failure"
    desc: "The creature is stunned 2."
  - name: "Critical Failure"
    desc: "The creature is stunned 3."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30, attack +21 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Electric Arc|Electric Arc]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Mindlink|Mindlink]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will), [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]] (×3) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Mind Probe|Mind Probe]] (×3), [[srd/pf2e/compendium/spells/rank-4/Mirage|Mirage]] - __6th__ [[srd/pf2e/compendium/spells/rank-4/Rewrite Memory|Rewrite Memory]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (×3) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 23."
```

```encounter-table
name: Nymolus
creatures:
  - 1: Nymolus
```
