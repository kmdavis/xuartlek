---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nucol"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Nucol"
level: 4
source: "Monster Core 2"
aon_id: "creature-4534"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4534"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nucol"
level: "Creature 4"
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, scent (imprecise) 100 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +12, Deception +10, Intimidation +12, Stealth +10"
abilityMods: [4, 2, 3, 0, 3, 2]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the _binding circle_ ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +10; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ disease, fear; __Resistances__ poison 5; __Weaknesses__ holy 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusk +12 (deadly d10, magical, unholy) __Damage__ 2d8+6 piercing plus 1d4 spirit and nervous consumption"
abilities_bot:
  - name: "Nervous Consumption"
    desc: "(Disease, divine, emotion, mental)"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Onset"
    desc: "1 minute"
  - name: "Stage 1"
    desc: "sickened 1 and stupefied 1 (1 day)"
  - name: "Stage 2"
    desc: "clumsy 1 and stupefied 2 (1 day)"
  - name: "Stage 3"
    desc: "clumsy 2 and stupefied 3 (1 day)"
  - name: "Skip Between"
    desc: "⬻ (Divine, teleportation) The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Spray Pus"
    desc: "⬻ The nucol flexes one of its infected wounds, releasing a spray of pus in a 15-foot cone or targeting an individual creature within 30 feet. A creature targeted or in the area is exposed to nervous consumption."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20 - __Cantrips (2nd)__ Detect Magic, Telekinetic Hand - __1st__ Grease (×3) - __3rd__ Cleanse Affliction, Fear (at will)"
sourcebook: "_Monster Core 2_, page 275."
```

```encounter-table
name: Nucol
creatures:
  - 1: Nucol
```
