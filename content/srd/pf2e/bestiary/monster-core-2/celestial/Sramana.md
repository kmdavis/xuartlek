---
noteType: pf2eMonster
aliases: "Sramana"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Sramana"
level: 15
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4030"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sramana"
level: "Creature 15"
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 29
perception:
  - name: "Perception"
    desc: "+29; darkvision, heed the fettered (imprecise) 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; [[srd/pf2e/compendium/spells/rank-5/Truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +26, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +27, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +29"
abilityMods: [8, 4, 6, 4, 8, 5]
abilities_top:
  - name: "Heed the Fettered"
    desc: "The sramana can detect penitent creatures who wish to atone for their misdeeds, creatures with the [[srd/pf2e/compendium/rules-elements/traits/monster-core/Soulbound|soulbound]] trait, and soul gems as an imprecise sense with a range of 120 feet."
  - name: "Soul-Rescuing Vow"
    desc: "A sramana can use [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|_interplanar teleport_]] to teleport near a truly penitent creature, soulbound creature, or soul gem of which they're aware. If they do, they don't need a planar key and arrive 1d20 miles away from the subject. They can also teleport to [[srd/pf2e/compendium/gm/Planes#Nirvana|Nirvana]] or The [[srd/pf2e/compendium/gm/Planes#Boneyard|Boneyard]] without a planar key."
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/worn-items/Handwraps of Mighty Blows|+1 striking handwraps of mighty blows]]_, expanded healer's toolkit, _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+2 striking]] khakkara_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +26; __Ref__: +24; __Will__: +28"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 15; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] 15"
abilities_mid:
  - name: "Aura of Renunciation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 100 feet. Truly penitent creatures in the sramana's aura are affected by a DC 35 [[srd/pf2e/compendium/spells/rank-1/Sanctuary|_sanctuary_]] spell. If any creature within the aura takes a hostile action, _sanctuary_ ends for only that creature, not for the other creatures in the aura. In addition, soul gems in the aura can't be ingested, consumed, or otherwise used. A creature who attempts to do so becomes [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 1]] unless it succeeds at a DC 37 Fortitude save."
speed: "40 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _khakkara_ +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shove|Shove]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 2d6+14 bludgeoning plus 2d6 spirit"
  - name: "Melee"
    desc: "⬻ _fist_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 2d4+14 bludgeoning plus 2d6 spirit"
abilities_bot:
  - name: "Shelter the Suffering"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The sramana tosses the shawl of their robes into the air, where it expands to protect the suffering. Each truly penitent creature in a 100-foot emanation is affected by an [[srd/pf2e/compendium/spells/rank-2/Invisibility|_invisibility_]] spell, and the area is affected by the [[srd/pf2e/compendium/spells/rank-6/Field of Life|_field of life_]] spell, though it affects only penitent creatures and [[srd/pf2e/compendium/rules-elements/traits/monster-core/Soulbound|soulbound]] creatures. These effects last for 1 round but can be sustained for up to 1 hour. Soul Saviors Over the course of helping souls renounce suffering, many sramanas develop alliances with [[srd/pf2e/compendium/gm/creature-families/Psychopomp|psychopomps]], whose goal of returning the lost and trapped to the River of Souls they gladly share. These bonds run so deep that it isn't unusual to find sramana volunteering as legal advocates in the [[srd/pf2e/compendium/gm/Planes#Boneyard|Boneyard's]] courts."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Vitality Lash|Vitality Lash]] - __7th__ [[srd/pf2e/compendium/spells/rank-2/Calm|Calm]], [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (at will; see soul-rescuing vow), [[srd/pf2e/compendium/spells/rank-7/Planar Seal|Planar Seal]], [[srd/pf2e/compendium/spells/rank-5/Sending|Sending]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/Clear Mind|Clear Mind]], [[srd/pf2e/compendium/spells/rank-8/Divine Inspiration|Divine Inspiration]], [[srd/pf2e/compendium/spells/rank-8/Moment of Renewal|Moment of Renewal]], [[srd/pf2e/compendium/spells/rank-8/Pinpoint|Pinpoint]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 37 - __1st__ Angelic Messenger - __4th__ Atone"
sourcebook: "_Monster Core 2_, page 28."
```

```encounter-table
name: Sramana
creatures:
  - 1: Sramana
```
