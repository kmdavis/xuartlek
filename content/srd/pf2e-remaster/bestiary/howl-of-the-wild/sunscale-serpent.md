---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sunscale Serpent"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Sunscale Serpent"
level: 14
source: "Howl of the Wild"
aon_id: "creature-3311"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3311"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Sunscale Serpent"
level: "Creature 14"
size: "Huge"
trait_01: "Animal"
trait_02: "Beast"
trait_03: "Incorporeal"
trait_04: "Spirit"
trait_05: "Uncommon"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; low-light vision, tremorsense (imprecise) 100 feet"
languages: "Common, Draconic; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +25, Stealth +33, Survival +28"
abilityMods: [8, 4, 3, 1, 6, -1]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +25; __Ref__: +26; __Will__: +28"
hp: 251
health:
  - name: "HP"
    desc: "251; __Immunities__ disease, paralyzed, poison, precision; __Resistances__ all damage 14 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical)"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲ tail only"
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +28 (Magical, reach 10 feet) __Damage__ 3d8+11 force plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +28 (Agile, Magical, reach 15 feet) __Damage__ 3d6+11 force plus Push"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "(Mental, Primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The spirit guide spends 10 minutes to form a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 28, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. This bond strengthens the spirit guide's connection to the Universe. While bonded, the spirit guide loses the incorporeal and spirit traits, loses their immunity to disease, paralysis, and poison, along with their resistance to all damage, and changes their Strikes to deal the appropriate amount of physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "⬺"
  - name: "Requirements"
    desc: "The sunscale serpent is currently Bonded with a Mortal"
  - name: "Effect"
    desc: "The sunscale serpent makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
  - name: "Sun's Heat"
    desc: "⬺ The sunscale serpent Flies up to its fly Speed. All creatures directly below the spaces it moves through must succeed at a DC 31 Fortitude save or be exposed to sun's touch poison. The serpent cannot fly further than 60 feet above the target or the poison becomes too dispersed in the fall to take effect."
  - name: "Sun's Touch"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "Fortitude DC 34"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "6d8 poison damage and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "8d6 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "6d10 poison damage and fatigued (1 round)"
  - name: "Swallow Whole"
    desc: "⬻ Large, 2d10+9 force and 2d10 fire, Rupture 32"
  - name: "Unleash the Sun"
    desc: "⬽"
  - name: "Requirement"
    desc: "The sunscale serpent is flying"
  - name: "Effect"
    desc: "The sunscale serpent Flies up to its fly Speed, then crashes to the ground, releasing a wave of heat dealing 5d10 fire damage to all creatures within a 60-foot burst and searing their eyes with the erupting glory of its scales. Each creature in the area must attempt a DC 31 Reflex save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is dazzled for 1 round."
  - name: "Critical Failure"
    desc: "The creature takes full damage, is blinded for 1 round, and dazzled for 1 minute."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 31 - __Constant (5th)__ Truespeech"
sourcebook: "_Howl of the Wild_, page 182."
```

```encounter-table
name: Sunscale Serpent
creatures:
  - 1: Sunscale Serpent
```
