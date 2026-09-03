---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Izfiitar"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/medium
statblock: inline
name: "Izfiitar"
level: 20
source: "Monster Core 2"
aon_id: "creature-4520"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4520"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Izfiitar"
level: "Creature 20"
size: "Medium"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, entropy sense (imprecise) 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Protean; telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +38, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +35, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +35, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +37, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +37, [[srd/pf2e/compendium/rules-elements/skills/lore|Maelstrom Lore]] +37, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +36, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +38, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +35, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +38"
abilityMods: [9, 10, 9, 7, 8, 9]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]]) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/veil-of-privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 44
armorclass:
  - name: "AC"
    desc: "44; __Fort__: +33; __Ref__: +36; __Will__: +38 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 360
health:
  - name: "HP"
    desc: "360 (fast healing 20); __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 20, precision 20, protean anatomy 25 Kiss of the Speakers (divine) The izfiitar continuously tinkers with the myriad possibilities in which it can move or manipulate magic. The izfiitar is always [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] and can use the extra action only to Step, Stride, or as part of Casting a Spell."
abilities_mid:
  - name: "Prescient Revision"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]])"
  - name: "Trigger"
    desc: "The izfiitar fails a check"
  - name: "Effect"
    desc: "The izfiitar rerolls the triggering check and takes the better result. For 1d4 rounds, it loses the effects of Kiss of the Speakers and can't use Reshape Reality."
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "40 feet, fly 50 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d10+19 piercing plus greater warpwave strike"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d8+19 slashing plus greater warpwave strike"
  - name: "Melee"
    desc: "⬻ tail +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 4d12+19 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The izfiitar takes the appearance of any Huge or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal."
  - name: "Constrict"
    desc: "⬻ 2d8+19 bludgeoning, DC 44"
  - name: "Greater Warpwave Strike"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) Any creature struck and damaged by an izfiitar's jaws or claw Strike must succeed at a DC 42 Fortitude save or be subject to a particularly powerful warpwave. Roll twice and apply both affects, rerolling any duplicates."
  - name: "Reshape Reality"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) When the izfiitar casts [[srd/pf2e/compendium/spells/rank-4/mirage|_mirage_]], it infuses the illusion with quasi-real substance. Creatures that don't disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
  - name: "Storm of Claws"
    desc: "⬺ The izfiitar makes up to six claw Strikes, each against a different target. Heralds Of The Speakers Izfiitars with the greatest authority have even greater powers, such as the ability to cleave off portions of other planes into the [[srd/pf2e/compendium/gm/planes#Maelstrom|Maelstrom]] or to flaunt the laws of reality to redirect spell effects at their whims."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/creation|Creation]] (at will), [[srd/pf2e/compendium/spells/rank-4/mirage|Mirage]] (at will; see Reshape Reality), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]] (at will; self only) - __7th__ [[srd/pf2e/compendium/spells/rank-7/warp-mind|Warp Mind]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-4/confusion|Confusion]] (at will), [[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|Cursed Metamorphosis]], [[srd/pf2e/compendium/spells/rank-6/disintegrate|Disintegrate]], [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-4/divine-wrath|Divine Wrath]], [[srd/pf2e/compendium/spells/rank-9/massacre|Massacre]], [[srd/pf2e/compendium/spells/rank-9/overwhelming-presence|Overwhelming Presence]] - __10th__ [[srd/pf2e/compendium/spells/rank-10/manifestation|Manifestation]] - __Constant (5th)__ [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
sourcebook: "_Monster Core 2_, page 261."
```

```encounter-table
name: Izfiitar
creatures:
  - 1: Izfiitar
```
