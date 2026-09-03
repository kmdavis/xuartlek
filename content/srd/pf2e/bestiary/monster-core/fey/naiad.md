---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Naiad"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/nymph
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Naiad"
level: 1
source: "Monster Core"
aon_id: "creature-3111"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3111"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Naiad"
level: "Creature 1"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: "Water"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "Common, Elven, Fey, Thalassic"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +3, Diplomacy +7, Nature +6, Stealth +6, Survival +4"
abilityMods: [0, 3, 0, 1, 1, 4]
abilities_top:
  - name: "Animal Empathy"
    desc: "The naiad can ask questions of, receive answers from, and use the Diplomacy skill with animals."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +3; __Ref__: +6; __Will__: +8"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ fire 3; __Weaknesses__ cold iron 3"
abilities_mid:
  - name: "Water Dependent"
    desc: "A naiad is bonded to a spring, pond, or similar-sized water feature. If she is more than 300 feet away from it for 24 hours or more, she gains the weak adjustments until she returns. She can perform a 24-hour ritual to bond herself to a new body of water."
  - name: "Water Healing"
    desc: "(healing, primal, vitality) For every 10 minutes a naiad spends soaking in her bonded body of water, she regains 7 Hit Points."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ aqueous fist +8 (Agile, Finesse, Magical, Water) __Damage__ 1d8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ water orb +8 (Magical, range 60 feet, Water) __Damage__ 1d6 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __1st__ Charm, Create Water, Hydraulic Push, Tidal Surge (at will)"
sourcebook: "_Monster Core_, page 244."
```

```encounter-table
name: Naiad
creatures:
  - 1: Naiad
```
