---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jabali"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/large
statblock: inline
name: "Jabali"
level: 7
source: "Monster Core"
aon_id: "creature-3004"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3004"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jabali"
level: "Creature 7"
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: "Genie"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, tremorsense (imprecise) 60 feet"
languages: "Common, Petran; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +19, Crafting +14, Deception +16, Nature +15, Society +14"
abilityMods: [6, 1, 4, 3, 2, 3]
abilities_top:
  - name: "Items"
    desc: "_+1 falchion_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +18; __Ref__: +12; __Will__: +15"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "25 feet, burrow 45 feet, climb 20 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ _falchion_ +20 (Forceful, Magical, reach 10 feet, Sweep) __Damage__ 1d10+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +19 (Agile, Magical, Nonlethal, reach 10 feet) __Damage__ 1d4+12 bludgeoning plus Push 10 feet and stone clutch"
abilities_bot:
  - name: "Earth Glide"
    desc: "The jabali can Burrow through dirt and stone at their full burrow Speed, leaving no tunnels or signs of their passing."
  - name: "Stone Clutch"
    desc: "(Arcane, Earth) When the jabali Pushes a creature into a stone barrier, the surface grips it with fingers of stone. The target must succeed at a DC 22 Reflex save or become grabbed by the surface (Escape DC 28). Jabali Shuyookhs Jabali shuyookhs fulfill wishes as straightforwardly as possible. They add the following innate spells: __8th__ _earthquake_; __6th__ _mountain resilience_ (at will; self only), _petrify_; __5th__ _illusory disguise_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 24 - __Cantrips (4th)__ Detect Magic - __4th__ Shape Stone (at will) - __5th__ Wall of Stone - __7th__ Interplanar Teleport (to Astral Plane; Elemental Planes; or the Universe only) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 158."
```

```encounter-table
name: Jabali
creatures:
  - 1: Jabali
```
