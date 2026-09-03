---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hellbound Attorney"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Hellbound Attorney"
level: 4
source: "Monster Core 2"
aon_id: "creature-4326"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4326"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hellbound Attorney"
level: "Creature 4"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Human"
trait_04: "Humanoid"
trait_05: "Uncommon"
trait_06: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; greater darkvision"
languages: "Common, Diabolic"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Deception +11, Diplomacy +11, Intimidation +11, Legal Lore +14, Society +12"
abilityMods: [1, 2, 0, 4, 1, 3]
abilities_top:
  - name: "Items"
    desc: "elegant cane (as mace), legal ledgers"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +9; __Ref__: +12; __Will__: +13"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ fire 4; __Weaknesses__ holy 2"
abilities_mid:
  - name: "Abrogation of Consequences"
    desc: "⬲"
  - name: "Trigger"
    desc: "The Hellbound attorney rolls a success or critical failure on a saving throw against a linguistic effect"
  - name: "Effect"
    desc: "The attorney finds a loophole in the wording of the effect, turning the success into a critical success or a critical failure into a normal failure."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ elegant cane +12 (Agile, finesse, shove) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Opening Statement"
    desc: "⭓ (Auditory, concentrate)"
  - name: "Trigger"
    desc: "The Hellbound attorney's turn begins"
  - name: "Effect"
    desc: "The attorney enumerates the alleged crimes of a creature they can see and attempts a Legal Lore check against that creature's Will DC. On a success, the attorney's Strikes deal an additional 2d6 precision damage (4d6 precision damage on a critical success) to the creature until the end of the attorney's turn."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __1st__ Breathe Fire"
sourcebook: "_Monster Core 2_, page 99."
```

```encounter-table
name: Hellbound Attorney
creatures:
  - 1: Hellbound Attorney
```
