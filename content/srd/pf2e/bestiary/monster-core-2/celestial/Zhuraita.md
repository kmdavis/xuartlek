---
noteType: pf2eMonster
aliases: "Zhuraita"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Zhuraita"
level: 15
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4095"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Zhuraita"
level: "Creature 15"
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 28
perception:
  - name: "Perception"
    desc: "+28; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Lore|Academia Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +28, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Lore|Library Lore]] +30, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +28, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +26, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/Lore|Scribing Lore]] +28"
abilityMods: [4, 6, 5, 7, 7, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +23; __Ref__: +26; __Will__: +29"
hp: 280
health:
  - name: "HP"
    desc: "280; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 15"
abilities_mid:
  - name: "Deconstruct"
    desc: "⬲"
  - name: "Trigger"
    desc: "The zhuraita is targeted by an effect with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Linguistic|linguistic]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] trait"
  - name: "Effect"
    desc: "The zhuraita critiques their enemy's theoretical underpinnings, attempting a counteract check with a bonus of +28 (counteract rank 8). If the effect is counteracted, the triggering enemy becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 1]] (frightened 2 if the zhuraita critically succeeded)."
speed: "40 feet; fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ thesis +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d12+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ looseleaf +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range 60 feet) __Damage__ 3d10+10 slashing"
abilities_bot:
  - name: "Revealing Hypothesis"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]])"
  - name: "Requirements"
    desc: "The zhuraita hits a creature with its thesis"
  - name: "Effect"
    desc: "The zhuraita's thesis opens, with the pages fluttering at an unnatural speed. It then slams shut, with the cover now showing the image of the creature it hit. The zhuraita's Strikes against that creature deal an additional 2d6 precision damage. The zhuraita can only have one creature as the focus of its Revealing Hypothesis, which lasts until they target someone else."
  - name: "Thesis Shield"
    desc: "⬻ A spinning circle of tomes surrounds the zhuraita, lasting until the start of their next turn. While Thesis Shield is active, the zhuraita gains a +2 circumstance bonus to AC and has the [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] condition. Prayer To The Zhuraita Many a scholar have found themselves burning the last nub of their candle late into the night, the halls of learning echoing their words: _O holy Scholar, please recall to me this footnote's source; Without its mislaid citation, my evidence will falter; My professor will scorn my unfinished work; Earning my thesis unjust failure._"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Mindlink|Mindlink]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Hypercognition|Hypercognition]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Translate|Translate]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-2/Clear Mind|Clear Mind]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 52."
```

```encounter-table
name: Zhuraita
creatures:
  - 1: Zhuraita
```
