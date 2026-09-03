---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Alicorn"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Alicorn"
level: 15
source: "Howl of the Wild"
aon_id: "creature-3320"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3320"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Alicorn"
level: "Creature 15"
size: "Huge"
trait_01: "Beast"
trait_02: "Fey"
trait_03: "Holy"
trait_04: "Rare"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, scent (imprecise) 30 feet"
languages: "Common, Empyrean, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +27, Arcana +27, Athletics +27, Diplomacy +30, Stealth +25"
abilityMods: [8, 7, 4, 6, 4, 6]
abilities_top:
  - name: "Wild Empathy"
    desc: "The alicorn has an empathic connection to the creatures of the natural world that. The alicorn can use Diplomacy to Make an Impression on animals and to make very simple Requests of them."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +26; __Ref__: +26; __Will__: +29"
hp: 320
health:
  - name: "HP"
    desc: "320; __Immunities__ poison"
abilities_mid:
  - name: "Draw in Magic"
    desc: "⬲ (arcane, concentrate)"
  - name: "Trigger"
    desc: "A creature within 30 feet of the alicorn Casts a Spell"
  - name: "Effect"
    desc: "The alicorn attempts to counteract the triggering spell (counteract modifier +28, counteract rank 8th). If successful, the alicorn can choose to gain the effects of the triggering spell as its sole target."
speed: "40 feet, fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +29 (Holy, Magical) __Damage__ 4d10+10 piercing plus 2d6 spirit and ghost touch"
  - name: "Melee"
    desc: "⬻ hoof +29 (Holy, Magical, reach 10 feet) __Damage__ 4d6+10 piercing plus 2d6 spirit and ghost touch"
  - name: "Melee"
    desc: "⬻ wing +29 (Agile, Magical, reach 10 feet) __Damage__ 4d8+10 bludgeoning and ghost touch"
abilities_bot:
  - name: "Aerial Attack"
    desc: "⬺ The alicorn Flies and Strikes twice with their wings at any points during their movement. Each attack counts toward the alicorn's multiple attack penalty, but the penalty doesn't increase until after they make all the attacks."
  - name: "Beam of Light"
    desc: "⬺ (Arcane, Concentrate, Fire, Holy, Light) The alicorn harnesses a powerful burning ray of light from their horn. Creatures in a 120-foot line take 16d6 fire damage (DC 36 basic Fortitude save). An unholy creature in the area takes an additional 8d6 spirit damage. If the light passes through an area of magical darkness or targets a creature affected by magical darkness, the beam attempts to counteract the darkness (counteract modifier +28, counteract rank 8th). The alicorn can't use its Beam of Light again for 1d4 rounds."
  - name: "Ghost Touch"
    desc: "An alicorn's Strikes have the effects of a _ghost touch_ property rune."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ Light - __1st__ Gentle Landing (at will) - __5th__ Banishment - __6th__ Telepathy - __8th__ Wall of Force"
sourcebook: "_Howl of the Wild_, page 191."
```

```encounter-table
name: Alicorn
creatures:
  - 1: Alicorn
```
