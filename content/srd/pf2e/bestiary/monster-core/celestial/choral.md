---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Choral"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/small
statblock: inline
name: "Choral"
level: 6
source: "Monster Core"
aon_id: "creature-2815"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2815"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Choral"
level: "Creature 6"
size: "Small"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Diplomacy +15, Performance +17, Religion +14"
abilityMods: [1, 4, 2, 3, 4, 5]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +10; __Ref__: +14; __Will__: +16 +1 status to all saves vs. magic"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ sonic 5; __Weaknesses__ unholy 5"
abilities_mid:
  - name: "Harmonizing Aura"
    desc: "(aura, divine, sonic) 20 feet. Allies in the aura gain a +2 status bonus to sonic damage rolls and a +1 status bonus to AC and all saves against effects with the auditory or sonic trait. Enemies in the aura take a –2 status penalty to sonic damage rolls and a –1 status penalty to AC and all saves against sonic and auditory effects."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse, Holy, Magical) __Damage__ 2d6+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ piercing hymn +17 (Holy, Magical, range 90 feet, Sonic) __Damage__ 4d6 sonic damage plus deafening aria"
abilities_bot:
  - name: "Deafening Aria"
    desc: "On a critical hit with piercing hymn, the target is deafened for 1 minute."
  - name: "Harmonize"
    desc: "⬻ (Concentrate, Divine, Sonic) The choral angel lends their harmony to a choral angel ally within their harmonizing aura. The ally can, on their next turn, expend their 3rd-rank _noise blast_ to instead cast _calm_, _heroism_, or 4th-rank _noise blast_. If the ally is benefiting from 5 or more chorals' Harmonize actions, they can instead choose _divine decree_."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15 - __Cantrips (3rd)__ Courageous Anthem, Uplifting Overture - __1st__ Counter Performance (at will) - __2nd__ Invisibility (at will; self only), Noise Blast (at will) - __3rd__ Cleanse Affliction, Clear Mind (at will), Heal, Noise Blast - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 23 - __1st__ Angelic Messenger"
sourcebook: "_Monster Core_, page 15."
```

```encounter-table
name: Choral
creatures:
  - 1: Choral
```
