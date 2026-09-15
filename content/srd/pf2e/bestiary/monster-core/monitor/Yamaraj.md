---
noteType: pf2eMonster
aliases: "Yamaraj"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Yamaraj"
level: 20
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3150"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Yamaraj"
level: "Creature 20"
size: "Huge"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: "Uncommon"
modifier: 37
perception:
  - name: "Perception"
    desc: "+37; darkvision, lifesense 240 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; telepathy 120 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +38, Boneyard Lore +40, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +34, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +36, Legal Lore +40, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +38, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +38, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +38"
abilityMods: [10, 7, 7, 10, 7, 6]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +33; __Ref__: +31; __Will__: +35 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 375
health:
  - name: "HP"
    desc: "375 (fast healing 20, lightning drinker); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] (see lightning drinker); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 20, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]] 20"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 60 feet, DC 39"
  - name: "Lightning Drinker"
    desc: "Whenever a yamaraj would take electricity damage if not for its immunity, its fast healing increases to 40 on its next turn. During that turn, if it uses Beetle Breath, the beetles deal 2d12 additional electricity damage."
speed: "35 feet, fly 50 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 4d8+18 piercing plus Improved Grab and yamaraj venom and 3d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 4d4+18 slashing plus 3d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ tail +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 4d10+18 bludgeoning plus 3d6 shepherd's touch"
abilities_bot:
  - name: "Beetle Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) The yamaraj breathes a blast of beetles in a 50-foot cone that deals 14d8 slashing damage and 4d8 persistent slashing damage to creatures in the area with a DC 42 Reflex save. It can't use Beetle Breath again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage and is [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 1]]."
  - name: "Failure"
    desc: "The creature takes full damage and is sickened 2."
  - name: "Critical Failure"
    desc: "The creature takes double damage and is sickened 3."
  - name: "Final Judgment"
    desc: "A yamaraj's [[srd/pf2e/compendium/spells/rank-10/Manifestation|_manifestation_]] spells are used only to pronounce judgment, typically either to restore a dead or destroyed creature to life, bind a creature to the [[srd/pf2e/compendium/gm/Planes#Boneyard|Boneyard]], or banish a creature from the Boneyard."
  - name: "Shepherd's Touch"
    desc: "A yamaraj's Strikes have the benefit of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune and deal an additional 3d6 void damage to living creatures or 3d6 vitality damage to undead."
  - name: "Yamaraj Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]]) While a creature is [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy]] from this poison, it is [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]] with the same value"
  - name: "Saving Throw"
    desc: "DC 42 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "3d8 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 1]] (1 round)"
  - name: "Stage 2"
    desc: "5d8 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "7d8 poison damage and clumsy 3 (1 round)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-5/Mind Probe|Mind Probe]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-6/Chain Lightning|Chain Lightning]] (×3), [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (×3), [[srd/pf2e/compendium/spells/rank-6/Wall of Force|Wall of Force]] - __9th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-9/Seize Soul|Seize Soul]], [[srd/pf2e/compendium/spells/rank-6/Spirit Blast|Spirit Blast]], [[srd/pf2e/compendium/spells/rank-9/Wails of the Damned|Wails of the Damned]] - __10th__ [[srd/pf2e/compendium/spells/rank-10/Manifestation|Manifestation]] (see final judgment), [[srd/pf2e/compendium/spells/rank-10/Revival|Revival]] - __Constant (10th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 44 - __5th__ Call Spirit, Resurrect"
sourcebook: "_Monster Core_, page 277."
```

```encounter-table
name: Yamaraj
creatures:
  - 1: Yamaraj
```
