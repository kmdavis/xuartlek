---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3111"
socialImage: og-image.png
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
    desc: "+6; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +7, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +4"
abilityMods: [0, 3, 0, 1, 1, 4]
abilities_top:
  - name: "Animal Empathy"
    desc: "The naiad can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill with [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animals]]."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +3; __Ref__: +6; __Will__: +8"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 3; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 3"
abilities_mid:
  - name: "Water Dependent"
    desc: "A naiad is bonded to a spring, pond, or similar-sized water feature. If she is more than 300 feet away from it for 24 hours or more, she gains the weak adjustments until she returns. She can perform a 24-hour ritual to bond herself to a new body of water."
  - name: "Water Healing"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]]) For every 10 minutes a naiad spends soaking in her bonded body of water, she regains 7 Hit Points."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ aqueous fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|Water]]) __Damage__ 1d8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ water orb +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|Water]]) __Damage__ 1d6 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/Create Water|Create Water]], [[srd/pf2e/compendium/spells/rank-1/Hydraulic Push|Hydraulic Push]], [[srd/pf2e/compendium/spells/focus/Tidal Surge|Tidal Surge]] (at will)"
sourcebook: "_Monster Core_, page 244."
```

```encounter-table
name: Naiad
creatures:
  - 1: Naiad
```
