---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vrolikai"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Vrolikai"
level: 20
source: "Monster Core"
aon_id: "creature-2901"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2901"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vrolikai"
level: "Creature 20"
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +37, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +33, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +36, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +36, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +38, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +34, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +34, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +34"
abilityMods: [10, 7, 9, 6, 6, 8]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +35; __Ref__: +33; __Will__: +34 +1 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 440
health:
  - name: "HP"
    desc: "440; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Death-Stealing Gaze"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a non-[[srd/pf2e/compendium/rules-elements/traits/player-core/demon|demon]] ends its turn in the aura, it must attempt a DC 38 Fortitude save. If it fails, it becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]. A creature that dies while it has drain from a vrolikai's gaze rises as a [[srd/pf2e/compendium/gm/creature-families/ghoul|ghoul]] the next midnight. The GM determines what kind of ghoul."
speed: "35 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ black flame knife +40 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d4+18 piercing plus 2d6 void"
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d12+18 piercing"
  - name: "Melee"
    desc: "⬻ stinger +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d8+18 piercing plus mindwarping"
abilities_bot:
  - name: "Black Flame Knives"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) The vrolikai manifests a dagger-shaped blade of what looks like crystallized black flame in each of their four hands. These weapons function as _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|greater striking]] [[srd/pf2e/compendium/equipment/weapons/knife/dagger|daggers]]_ that deal an additional 2d6 void damage. They fade away into nothingness 1 minute after a vrolikai no longer carries them."
  - name: "Consume Death"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The vrolikai focuses their deathstealing gaze upon a single target they can see within 30 feet. The target must immediately attempt a Fortitude save against death-stealing gaze."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is affected by death-stealing gaze and becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]. If the creature was already drained 1 by the death-stealing gaze before attempting the save, a failed save increases the value of the drained condition by 1, to a maximum of drained 4. The vrolikai gains 10 temporary Hit Points, and the drained creature is temporarily immune until the start of the vrolikai's next turn."
  - name: "Critical Failure"
    desc: "As failure, but the creature increases the amount of drain by 2."
  - name: "Focused Flames"
    desc: "⬺ The vrolikai attacks a single target with all of their black flame knives. The demon makes a black flame knife Strike with the following additional effects. This counts toward the vrolikai's multiple attack penalty as a number of attacks equal to the number of back flame knives the vrolikai used."
  - name: "Critical Success"
    desc: "The target takes an additional 2d6 void damage for each knife beyond the first (typically 6d6 extra damage) and takes 4d6 persistent void damage."
  - name: "Success"
    desc: "The target takes an additional 2d6 void damage for each knife beyond the first."
  - name: "Failure"
    desc: "The vrolikai deals the damage their black flame knife Strike normally deals on a hit."
  - name: "Mindwarping"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The sting of a vrolikai is mind-warping. A creature struck must attempt a DC 44 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature becomes [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] for 1 minute."
  - name: "Failure"
    desc: "The creature becomes stupefied 1. If it's already stupefied, its stupefied value increases by 1 instead (to a maximum of stupefied 4)."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/regenerate|Regenerate]] - __10th__ [[srd/pf2e/compendium/spells/rank-7/execute|Execute]], [[srd/pf2e/compendium/spells/rank-3/paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-9/massacre|Massacre]], [[srd/pf2e/compendium/spells/rank-6/vampiric-exsanguination|Vampiric Exsanguination]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 44 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 82."
```

```encounter-table
name: Vrolikai
creatures:
  - 1: Vrolikai
```
