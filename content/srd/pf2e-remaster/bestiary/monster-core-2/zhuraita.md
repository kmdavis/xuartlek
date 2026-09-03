---
obsidianUIMode: preview
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
aon_id: "creature-4095"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4095"
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
    desc: "Perception +28; darkvision, _truesight_"
languages: "Common, Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Academia Lore +30, Acrobatics +25, Arcana +28, Athletics +25, Library Lore +30, Nature +28, Occultism +26, Religion +28, Scribing Lore +28"
abilityMods: [4, 6, 5, 7, 7, 5]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +23; __Ref__: +26; __Will__: +29"
hp: 280
health:
  - name: "HP"
    desc: "280; __Weaknesses__ cold iron 15, unholy 15"
abilities_mid:
  - name: "Deconstruct"
    desc: "⬲"
  - name: "Trigger"
    desc: "The zhuraita is targeted by an effect with the linguistic or mental trait"
  - name: "Effect"
    desc: "The zhuraita critiques their enemy's theoretical underpinnings, attempting a counteract check with a bonus of +28 (counteract rank 8). If the effect is counteracted, the triggering enemy becomes frightened 1 (frightened 2 if the zhuraita critically succeeded)."
speed: "40 feet; fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ thesis +27 (Holy, Magical) __Damage__ 3d12+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ looseleaf +27 (Holy, Magical, range 60 feet) __Damage__ 3d10+10 slashing"
abilities_bot:
  - name: "Revealing Hypothesis"
    desc: "⭓ (Concentrate)"
  - name: "Requirements"
    desc: "The zhuraita hits a creature with its thesis"
  - name: "Effect"
    desc: "The zhuraita's thesis opens, with the pages fluttering at an unnatural speed. It then slams shut, with the cover now showing the image of the creature it hit. The zhuraita's Strikes against that creature deal an additional 2d6 precision damage. The zhuraita can only have one creature as the focus of its Revealing Hypothesis, which lasts until they target someone else."
  - name: "Thesis Shield"
    desc: "⬻ A spinning circle of tomes surrounds the zhuraita, lasting until the start of their next turn. While Thesis Shield is active, the zhuraita gains a +2 circumstance bonus to AC and has the concealed condition. Prayer To The Zhuraita Many a scholar have found themselves burning the last nub of their candle late into the night, the halls of learning echoing their words: _O holy Scholar, please recall to me this footnote's source; Without its mislaid citation, my evidence will falter; My professor will scorn my unfinished work; Earning my thesis unjust failure._"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ Detect Magic, Guidance, Read Aura - __1st__ Mindlink (at will) - __3rd__ Hypercognition - __4th__ Translate (at will) - __8th__ Clear Mind - __Constant (5th)__ Truespeech - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core 2_, page 52."
```

```encounter-table
name: Zhuraita
creatures:
  - 1: Zhuraita
```
