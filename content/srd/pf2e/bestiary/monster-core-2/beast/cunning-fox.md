---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cunning Fox"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/small
statblock: inline
name: "Cunning Fox"
level: 1
source: "Monster Core 2"
aon_id: "creature-4564"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4564"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Cunning Fox"
level: "Creature 1"
size: "Small"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common, Fey; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Deception +6, Stealth +8, Survival +5"
abilityMods: [1, 3, 0, 2, 2, 1]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +8; __Will__: +7"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ bleed, disease, paralyzed, poison, precision; __Resistances__ all damage 2 (except force, _ghost touch_, or spirit; double resistance vs. non-magical)"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +6 (Finesse, magical) __Damage__ 1d8+1 force"
  - name: "Melee"
    desc: "⬻ jaws +6 (Agile, finesse, magical) __Damage__ 1d4+1 force"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "⬺ (Mental, primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The spirit guide forms a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 10, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. This bond strengthens the spirit guide's connection to the Universe. While bonded, the spirit guide loses the incorporeal and spirit traits, loses their immunities and resistances, and changes their Strikes to deal the appropriate physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "⬺"
  - name: "Requirements"
    desc: "The spirit guide is currently Bonded with a Mortal"
  - name: "Effect"
    desc: "The spirit guide makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ Guidance, Read Aura, Stabilize - __1st__ Cleanse Cuisine, Detect Poison - __3rd__ Wanderer’s Guide - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 304."
```

```encounter-table
name: Cunning Fox
creatures:
  - 1: Cunning Fox
```
