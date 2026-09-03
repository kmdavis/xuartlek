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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +30, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +30, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +27"
abilityMods: [6, 4, 8, 4, 6, 8]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +29; __Ref__: +25; __Will__: +27"
hp: 280
health:
  - name: "HP"
    desc: "280; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 10 (except slashing); __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 15"
abilities_mid:
  - name: "Fascination of Flame"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 30 feet. A creature that enters or begins its turn in this aura's emanation must attempt a DC 33 Will save. Regardless of the result of the saving throw, the creature is temporarily immune for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature loses any [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] to fire for 1 round."
  - name: "Failure"
    desc: "The creature loses any resistance to fire for 1 hour."
  - name: "Critical Failure"
    desc: "The creature loses any resistance to fire for 1 hour and gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Weakness|weakness]] 15 to fire for the same duration."
  - name: "Absorb Flame"
    desc: "⬲"
  - name: "Trigger"
    desc: "The marrmora is targeted by a [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] spell or effect or is in the area of a fire effect"
  - name: "Effect"
    desc: "The marrmora is healed by the fire damage, regaining Hit Points equal to half the damage the fire effect would've dealt."
speed: "30 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +29 __Damage__ 3d6+14 slashing plus 3d6 fire and 1d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
  - name: "Ranged"
    desc: "⬻ flame jet +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], range increment 40 feet) __Damage__ 6d6 fire plus 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire]]"
abilities_bot:
  - name: "Igniting Assault"
    desc: "⬻"
  - name: "Requirements"
    desc: "The marrmora isn't under the effect of [[srd/pf2e/compendium/spells/rank-4/fire-shield|_fire shield_]]"
  - name: "Effect"
    desc: "The marrmora makes a claw Strike. If they hit, they can immediately cast one of their available _fire shield_ [[srd/pf2e/books/player-core/chapter-7-spells/innate-spells|innate spells]] as a free action. Fey Manipulators Marrmoras exert a strange and subtle dominance over other [[srd/pf2e/compendium/rules-elements/traits/player-core/fey|fey]]. The fey under their control are filled with both horror at the destruction wrought by marrmoras and fascination with their fiery power."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 36, attack +28 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]] - __6th__ [[srd/pf2e/compendium/spells/rank-4/fire-shield|Fire Shield]] (×3), [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] (×3), [[srd/pf2e/compendium/spells/rank-2/one-with-plants|One with Plants]] (at will; appears as a burnt; dead tree) - __7th__ [[srd/pf2e/compendium/spells/rank-5/elemental-form|Elemental Form]] (fire elemental only), [[srd/pf2e/compendium/spells/rank-7/volcanic-eruption|Volcanic Eruption]], [[srd/pf2e/compendium/spells/rank-4/wall-of-fire|Wall of Fire]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/blazing-bolt|Blazing Bolt]], [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]]"
sourcebook: "_Monster Core 2_, page 220."
```

```encounter-table
name: Marrmora
creatures:
  - 1: Marrmora
```
