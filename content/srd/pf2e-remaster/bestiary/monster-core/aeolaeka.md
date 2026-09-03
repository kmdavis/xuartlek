---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Aeolaeka"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Aeolaeka"
level: 12
source: "Monster Core"
aon_id: "creature-2843"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2843"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aeolaeka"
level: "Creature 12"
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Earth"
trait_04: "Holy"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, tremorsense (precise) 60 feet"
languages: "Draconic, Empyrean, Petran; _speak with stones_, _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +25, Diplomacy +22, Intimidation +22, Nature +23"
abilityMods: [6, 4, 7, 2, 5, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 striking warhammer_"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +20; __Will__: +23"
hp: 250
health:
  - name: "HP"
    desc: "250; __Weaknesses__ cold iron 15, unholy 15"
speed: "25 feet, burrow 25 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ _warhammer_ +25 (Holy, Magical, Shove) __Damage__ 2d8+12 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "An aeolaeka can Burrow through any earthen matter, including rock. When they do so, the aeolaeka moves at their full burrow Speed, leaving no tunnels or signs of their passing."
  - name: "Liberate the Earth"
    desc: "⬺ (Concentrate, Divine, Earth) The aeolaeka conjures churning stones, creating a 60-foot line of rolling boulders. Creatures in the line take 10d6 bludgeoning damage with a DC 35 Reflex save. The area is difficult terrain for 24 hours before the leftover stone crumbles to dust. The aeolaeka can't Liberate the Earth for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature takes no damage."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and is knocked prone."
  - name: "Critical Failure"
    desc: "The creature takes double damage, is knocked prone, and is immobilized by the rubble (Escape DC 32)."
  - name: "Statue"
    desc: "⬻ (Concentrate) Until the next time they act, the aeolaeka appears to be a statue. They have an automatic result of 45 on Deception checks and DCs to pass as a statue."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24 - __3rd__ Earthbind (at will) - __5th__ Heal, Locate, Wall of Stone, Weapon Storm - __6th__ Petrify, Sure Footing - __Constant (5th)__ Speak with Stones, Truespeech"
sourcebook: "_Monster Core_, page 35."
```

```encounter-table
name: Aeolaeka
creatures:
  - 1: Aeolaeka
```
