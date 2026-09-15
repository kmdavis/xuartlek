---
noteType: pf2eMonster
aliases: "Pakalchi"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Pakalchi"
level: 9
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4536"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Pakalchi"
level: "Creature 9"
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +18"
abilityMods: [4, 5, 4, 2, 3, 6]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/Binding Circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +17; __Ref__: +18; __Will__: +20"
hp: 150
health:
  - name: "HP"
    desc: "150; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Entangling Train"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature moves adjacent to the pakalchi"
  - name: "Effect"
    desc: "Writhing, pitch-black vines wrap around the creature. The creature takes 1d6 slashing damage and a –15-foot circumstance penalty to its Speeds until the end of its next turn."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d10+6 slashing plus 1d6 spirit, 1d6 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed]], and betrayal toxin"
  - name: "Melee"
    desc: "⬻ claw +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d10+6 slashing plus 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ thorn +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], range increment 50 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d4+6 piercing plus 1d6 spirit, 1d6 [[srd/pf2e/compendium/rules-elements/Conditions#Persistent Damage|persistent bleed]], and betrayal toxin"
abilities_bot:
  - name: "Betrayal Toxin"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]) A creature affected by betrayal toxin hears whispers of incessant doubt in their head and can't treat any creature as their ally"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 1 (1 round)"
  - name: "Stage 2"
    desc: "stupefied 2 (1 round)"
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __5th__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/Mask of Terror|Mask of Terror]] (self only) - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 276."
```

```encounter-table
name: Pakalchi
creatures:
  - 1: Pakalchi
```
