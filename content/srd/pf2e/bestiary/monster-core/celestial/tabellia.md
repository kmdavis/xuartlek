---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tabellia"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Tabellia"
level: 14
source: "Monster Core"
aon_id: "creature-2817"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2817"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tabellia"
level: "Creature 14"
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision"
languages: "Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +24, Diplomacy +26, Intimidation +28, Religion +24"
abilityMods: [8, 4, 5, 4, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+2 striking warhammer_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +26; __Will__: +22 +1 status to all saves vs. magic"
hp: 285
health:
  - name: "HP"
    desc: "285; __Weaknesses__ unholy 15"
abilities_mid:
  - name: "Traveler's Aura"
    desc: "(aura, divine) 20 feet. Creatures in the tabellia's aura are immune to ambient environmental damage from any plane, including severe and extreme heat and cold as well as more otherworldly dangers. The tabellia is never off-guard to creatures within their aura."
  - name: "Messenger's Amnesty"
    desc: "(divine) A tabellia with a message to deliver is continually protected by the effect of _sanctuary_ (DC 32). If the angel breaks the sanctuary, the effect returns if the angel ceases hostility for 10 minutes."
speed: "40 feet, fly 75 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _holy_ _warhammer_ +30 (Holy, Magical, Shove) __Damage__ 2d8+14 bludgeoning plus 1d4 spirit (or 2d4 spirit vs. an unholy target)"
abilities_bot:
  - name: "Stunning Strike"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tabellia hit a foe earlier this turn with a weapon Strike"
  - name: "Effect"
    desc: "The tabellia makes a weapon Strike against the foe. On a success, the foe must also succeed at a DC 34 Fortitude save or become stunned 1 (or stunned 2 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28 - __Cantrips (7th)__ Light - __2nd__ Invisibility (at will; self only) - __3rd__ Ring of Truth (at will) - __7th__ Blessed Boundary, Cleanse Affliction, Clear Mind, Divine Decree, Divine Wrath, Heal - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 36 - __1st__ Angelic Messenger"
sourcebook: "_Monster Core_, page 16."
```

```encounter-table
name: Tabellia
creatures:
  - 1: Tabellia
```
