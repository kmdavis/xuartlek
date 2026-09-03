---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Feathered Bear"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/large
statblock: inline
name: "Feathered Bear"
level: 10
source: "Monster Core 2"
aon_id: "creature-4565"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4565"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Feathered Bear"
level: "Creature 10"
size: "Large"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, scent (imprecise) 60 feet"
languages: "Common, Fey; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +22, Intimidation +20, Survival +16"
abilityMods: [7, 2, 5, 0, 2, 3]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +16; __Will__: +18"
hp: 160
health:
  - name: "HP"
    desc: "160; __Immunities__ bleed, disease, paralyzed, poison, precision; __Resistances__ all damage 10 (except force, _ghost touch_, or spirit; double resistance vs. non-magical)"
abilities_mid:
  - name: "Guardian's Aegis"
    desc: "(aura, primal) 30 feet. All allies within 30 feet of the feathered bear gain a +1 status bonus to saves against magical effects. The bonus increases to +2 if the effect originated from a fiend."
  - name: "Avenging Claws"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet damages the feathered bear's ally with a melee attack"
  - name: "Effect"
    desc: "The feathered bear immediately Steps toward the triggering attacker and makes a claws Strike."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +21 (Magical) __Damage__ 3d10+9 force"
  - name: "Melee"
    desc: "⬻ claw +21 (Agile, magical) __Damage__ 3d6+9 force plus Grab"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "(Mental, primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The spirit guide forms a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 20, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. This bond strengthens the spirit guide's connection to the Universe. While bonded, the spirit guide loses the incorporeal and spirit traits, loses their immunities and resistances, and changes their Strikes to deal the appropriate physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "⬺"
  - name: "Requirements"
    desc: "The spirit guide is currently Bonded with a Mortal"
  - name: "Effect"
    desc: "The spirit guide makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
  - name: "Mauler"
    desc: "The feathered bear gains a +4 circumstance bonus to damage rolls against creatures they've grabbed."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27 - __Cantrips (3rd)__ Know the Way - __3rd__ Environmental Endurance, Haste, Jump, Oaken Resilience - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 305."
```

```encounter-table
name: Feathered Bear
creatures:
  - 1: Feathered Bear
```
