---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Marrmora"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Marrmora"
level: 15
source: "Monster Core 2"
aon_id: "creature-4472"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4472"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Marrmora"
level: "Creature 15"
size: "Medium"
trait_01: "Fey"
trait_02: "Fire"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; low-light vision"
languages: "Common, Elven, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +25, Deception +30, Intimidation +30, Nature +30, Stealth +27, Survival +27"
abilityMods: [6, 4, 8, 4, 6, 8]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +29; __Ref__: +25; __Will__: +27"
hp: 280
health:
  - name: "HP"
    desc: "280; __Immunities__ fire; __Resistances__ physical 10 (except slashing); __Weaknesses__ cold iron 15"
abilities_mid:
  - name: "Fascination of Flame"
    desc: "(aura, emotion, mental, primal) 30 feet. A creature that enters or begins its turn in this aura's emanation must attempt a DC 33 Will save. Regardless of the result of the saving throw, the creature is temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature loses any resistance to fire for 1 round."
  - name: "Failure"
    desc: "The creature loses any resistance to fire for 1 hour."
  - name: "Critical Failure"
    desc: "The creature loses any resistance to fire for 1 hour and gains weakness 15 to fire for the same duration."
  - name: "Absorb Flame"
    desc: "⬲"
  - name: "Trigger"
    desc: "The marrmora is targeted by a fire spell or effect or is in the area of a fire effect"
  - name: "Effect"
    desc: "The marrmora is healed by the fire damage, regaining Hit Points equal to half the damage the fire effect would've dealt."
speed: "30 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +29 __Damage__ 3d6+14 slashing plus 3d6 fire and 1d6 persistent fire"
  - name: "Ranged"
    desc: "⬻ flame jet +29 (Fire, range increment 40 feet) __Damage__ 6d6 fire plus 2d6 persistent fire"
abilities_bot:
  - name: "Igniting Assault"
    desc: "⬻"
  - name: "Requirements"
    desc: "The marrmora isn't under the effect of _fire shield_"
  - name: "Effect"
    desc: "The marrmora makes a claw Strike. If they hit, they can immediately cast one of their available _fire shield_ innate spells as a free action. Fey Manipulators Marrmoras exert a strange and subtle dominance over other fey. The fey under their control are filled with both horror at the destruction wrought by marrmoras and fascination with their fiery power."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 36, attack +28 - __Cantrips (8th)__ Ignition - __6th__ Fire Shield (×3), Fireball (×3), One with Plants (at will; appears as a burnt; dead tree) - __7th__ Elemental Form (fire elemental only), Volcanic Eruption, Wall of Fire - __8th__ Blazing Bolt, Fireball"
sourcebook: "_Monster Core 2_, page 220."
```

```encounter-table
name: Marrmora
creatures:
  - 1: Marrmora
```
