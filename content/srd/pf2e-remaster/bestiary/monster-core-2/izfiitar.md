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
languages: "Chthonian, Empyrean, Protean; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +38, Arcana +35, Athletics +35, Deception +37, Diplomacy +37, Maelstrom Lore +37, Occultism +36, Religion +38, Society +35, Stealth +38"
abilityMods: [9, 10, 9, 7, 8, 9]
abilities_top:
  - name: "Entropy Sense"
    desc: "(divine, prediction) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. _Veil of privacy_ prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 44
armorclass:
  - name: "AC"
    desc: "44; __Fort__: +33; __Ref__: +36; __Will__: +38 +1 status to all saves vs. magic"
hp: 360
health:
  - name: "HP"
    desc: "360 (fast healing 20); __Resistances__ acid 20, precision 20, protean anatomy 25 Kiss of the Speakers (divine) The izfiitar continuously tinkers with the myriad possibilities in which it can move or manipulate magic. The izfiitar is always quickened and can use the extra action only to Step, Stride, or as part of Casting a Spell."
abilities_mid:
  - name: "Prescient Revision"
    desc: "⬲ (divine, fortune)"
  - name: "Trigger"
    desc: "The izfiitar fails a check"
  - name: "Effect"
    desc: "The izfiitar rerolls the triggering check and takes the better result. For 1d4 rounds, it loses the effects of Kiss of the Speakers and can't use Reshape Reality."
  - name: "Protean Anatomy"
    desc: "(divine) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to polymorph effects unless they're a willing target. If blinded or deafened, the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
speed: "40 feet, fly 50 feet, swim 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Finesse, Magical) __Damage__ 4d10+19 piercing plus greater warpwave strike"
  - name: "Melee"
    desc: "⬻ claw +38 (Agile, Finesse, Magical) __Damage__ 4d8+19 slashing plus greater warpwave strike"
  - name: "Melee"
    desc: "⬻ tail +38 (Magical, reach 10 feet) __Damage__ 4d12+19 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The izfiitar takes the appearance of any Huge or smaller creature. This doesn't change its Speed or its attack and damage bonuses with its Strikes, but might change the damage type its Strikes deal."
  - name: "Constrict"
    desc: "⬻ 2d8+19 bludgeoning, DC 44"
  - name: "Greater Warpwave Strike"
    desc: "(Divine) Any creature struck and damaged by an izfiitar's jaws or claw Strike must succeed at a DC 42 Fortitude save or be subject to a particularly powerful warpwave. Roll twice and apply both affects, rerolling any duplicates."
  - name: "Reshape Reality"
    desc: "(Divine, Polymorph) When the izfiitar casts _mirage_, it infuses the illusion with quasi-real substance. Creatures that don't disbelieve the illusion treat structures and terrain created through the spell as though they were real, ascending illusory stairs, becoming trapped by illusory quicksand, and so on."
  - name: "Storm of Claws"
    desc: "⬺ The izfiitar makes up to six claw Strikes, each against a different target. Heralds Of The Speakers Izfiitars with the greatest authority have even greater powers, such as the ability to cleave off portions of other planes into the Maelstrom or to flaunt the laws of reality to redirect spell effects at their whims."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47 - __4th__ Translocate (at will), Unfettered Movement - __5th__ Creation (at will), Mirage (at will; see Reshape Reality), Translocate - __6th__ Teleport (at will; self only) - __7th__ Warp Mind (at will) - __8th__ Confusion (at will), Cursed Metamorphosis, Disintegrate, Dispel Magic (at will) - __9th__ Divine Wrath, Massacre, Overwhelming Presence - __10th__ Manifestation - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 261."
```

```encounter-table
name: Izfiitar
creatures:
  - 1: Izfiitar
```
