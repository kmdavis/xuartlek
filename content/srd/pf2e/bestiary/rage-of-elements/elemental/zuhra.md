---
noteType: pf2eMonster
aliases: "Zuhra"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Zuhra"
level: 8
source: "Rage of Elements"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2655"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Zuhra"
level: "Creature 8"
size: "Large"
trait_01: "Elemental"
trait_02: "Genie"
trait_03: "Metal"
trait_04: "Uncommon"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Talican|Talican]]; _truespeech_"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +17, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +19, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +16"
abilityMods: [3, 5, 6, 4, 3, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 striking spiked chain_"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +17; __Will__: +17"
hp: 125
health:
  - name: "HP"
    desc: "125; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] 10"
abilities_mid:
  - name: "Conductive Redirection"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]])"
  - name: "Trigger"
    desc: "The zuhra is hit by an attack, spell, or effect that deals electricity damage"
  - name: "Effect"
    desc: "The zuhra conducts the electricity through their body, taking damage as normal, and redirecting a bolt at one target within 30 feet that they can see. The zuhra makes a ranged attack roll with a +20 modifier against the target's AC. On a hit or critical hit, the target takes electricity damage equal to the full damage of the triggering effect."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spiked chain_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 2d8+9 slashing"
  - name: "Melee"
    desc: "⬻ hand blade +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d4+9 slashing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Blinding Reflection"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Light|Light]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The zuhra is in dim or bright light"
  - name: "Effect"
    desc: "The zuhra briefly reshapes part of their metallic body into a concave surface to reflect the surrounding light into the eyes of a creature within 30 feet. The target must attempt a DC 26 Reflex save. It's then temporarily immune for 1 hour."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] until the start of the zuhra's next turn."
  - name: "Failure"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/Conditions#Blinded|blinded]] until the start of the zuhra's next turn."
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The zuhra transforms into a Small or Medium metal elemental or animal. This doesn't affect the zuhra's statistics, but it could change the damage type of their Strikes. Distant Thunder Zuhras favor music over all other arts. Given their long isolation, however, their preferences are quite unlike those of other genies or most musicians of the Universe. They value volume, intensity, and discordant combinations of sounds. Lead vocal parts incorporate droning and screams, often with a chorus providing a melodic counterpoint. Skimming Along Zuhras achieve flight by using magnetism to lift their own bodies into the air. As this grows more difficult the higher they go, many zuhras' preferred method of movement isn't walking or flying, but gliding along the smooth surfaces of their home plane much the way mortals cross ice on skates, with only a thin layer of electromagnetism between them and the ground."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (×2), Magnetic Attraction (at will), Magnetic Repulsion (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Mercurial Stride|Mercurial Stride]], [[srd/pf2e/compendium/spells/rank-4/Weapon Storm|Weapon Storm]] - __5th__ [[srd/pf2e/compendium/spells/rank-2/Clad in Metal|Clad in Metal]] (can choose uncommon metals) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (at will; to [[srd/pf2e/compendium/gm/Planes#Astral Plane|Astral Plane]], Elemental Planes, or the Universe only) - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/Truespeech|Truespeech]]"
sourcebook: "_Rage of Elements_, page 160."
```

```encounter-table
name: Zuhra
creatures:
  - 1: Zuhra
```
