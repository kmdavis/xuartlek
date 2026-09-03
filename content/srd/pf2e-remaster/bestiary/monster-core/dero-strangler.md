---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dero Strangler"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/dero
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Dero Strangler"
level: 3
source: "Monster Core"
aon_id: "creature-2903"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2903"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Dero Strangler"
level: "Creature 3"
size: "Small"
trait_01: "Dero"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Aklo, Sakvroth"
skills:
  - name: "Skills"
    desc: "Athletics +11, Intimidation +7, Medicine +6, Stealth +10"
abilityMods: [4, 3, 3, 0, -1, 2]
abilities_top:
  - name: "Items"
    desc: "cytillesh toolkit (see sidebar), Hand Crossbow (10 bolts), Lethargy Poison (5 doses), Rope (50 feet), spiked chain"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +8; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ confused"
abilities_mid:
  - name: "Ill Glow"
    desc: "(disease, light) A non-dero living creature that starts its turn grabbed or restrained by the strangler is exposed to the sickly blue light from the strangler's cytillesh toolkit. It must succeed at a DC 19 Fortitude save or become sickened 1. This has no effect if the strangler isn't wearing the toolkit. Vulnerable to Sunlight A dero strangler takes 8 damage for every hour they're exposed to sunlight."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ spiked chain +11 (Disarm, Trip) __Damage__ 1d8+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +10 (range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing plus lethargy poison"
abilities_bot:
  - name: "Dero Medicine"
    desc: "⬻ (Healing, Manipulate)"
  - name: "Requirements"
    desc: "The dero is wearing a cytillesh toolkit and has a hand free"
  - name: "Effect"
    desc: "The dero excises damaged flesh and crudely stitches wounds shut, healing themself or an ally in reach for 2d8 Hit Points. For 1 hour, the target has slashing weakness 2 and is immune to Dero Medicine."
  - name: "Strangle"
    desc: "⬻ (Attack, Nonlethal)"
  - name: "Requirements"
    desc: "The dero must have two free hands or be wielding a spiked chain"
  - name: "Effect"
    desc: "The dero attempts an Athletics check to Grapple with a +2 circumstance bonus. On a success, the target also takes 1d6+6 bludgeoning damage and can't speak (including to Cast a Spell) as long as they're grabbed or restrained."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19 - __Cantrips (2nd)__ Daze, Light, Read Aura - __2nd__ Darkness, Revealing Light"
sourcebook: "_Monster Core_, page 84."
```

```encounter-table
name: Dero Strangler
creatures:
  - 1: Dero Strangler
```
