---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Street Musician"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Street Musician"
level: 2
source: "NPC Core"
aon_id: "creature-3571"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3571"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Street Musician"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +6, Crafting +5, Deception +8, Diplomacy +8, Performance +8, Society +6"
abilityMods: [2, 1, 2, 0, 1, 4]
abilities_top:
  - name: "Items"
    desc: "Dagger, Musical Instrument (handheld)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +8; __Will__: +9"
hp: 32
health:
  - name: "HP"
    desc: "32"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, versatile S) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +8 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Distracting Drone"
    desc: "⬻"
  - name: "Requirements"
    desc: "The street musician is playing their instrument"
  - name: "Effect"
    desc: "The street musician attempts a Performance check compared to the Will DC of an observer within 30 feet. On a success, the target is fascinated by the street musician and off-guard for 1 round."
  - name: "Sneak Attack"
    desc: "The street musician deals an additional 1d4 precision damage to off-guard creatures. This increases to 1d6 against creatures off-guard due to the street musician's Feint or distracting drone."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ Daze, Figment, Light, Summon Instrument - __1st__ Charm, Force Barrage, Ventriloquism (3 slots)"
sourcebook: "_NPC Core_, page 125."
```

```encounter-table
name: Street Musician
creatures:
  - 1: Street Musician
```
