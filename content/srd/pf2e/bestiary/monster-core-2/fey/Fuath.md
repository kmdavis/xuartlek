---
noteType: pf2eMonster
aliases: "Fuath"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/tiny
statblock: inline
name: "Fuath"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4424"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fuath"
level: "Creature 1"
size: "Tiny"
trait_01: "Aquatic"
trait_02: "Fey"
trait_03: "Gremlin"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/Lore|Sailing Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +7"
abilityMods: [1, 4, 2, 1, 3, -1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/dart/Dart|darts]] (6)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +6"
hp: 18
health:
  - name: "HP"
    desc: "18; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 2, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 2"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A fuath becomes [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 1 (or increases its drained condition by 1) after every consecutive hour they're exposed to sunlight. Being submerged in more than a foot of water prevents the sunlight from harming the fuath."
speed: "20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]]) __Damage__ 1d6+1 slashing"
  - name: "Ranged"
    desc: "⬻ dart +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], range increment 20 feet) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Viscous Choke"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The fuath surrounds the head of one air-breathing creature within 30 feet in a magical film of viscous water for 1 minute. The target must succeed at a DC 17 Reflex save or it begins to choke and must hold its breath to avoid [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Encounter Mode#Drowning and Suffocating|drowning]]. The film can be temporarily wiped away with a total of 3 Interact actions by the choking creature or creatures adjacent to it, allowing a new Reflex save with a +2 circumstance bonus to end the effect. (These actions don't need to be consecutive or made by the same creature.) Fuath Guardians Lone fuaths sometimes appoint themselves guardians of nature, protecting spawning grounds from overfishing or preventing careless cutting of peat bogs. Most, however, are unrepentant saboteurs."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Create Water|Create Water]], [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]]"
sourcebook: "_Monster Core 2_, page 177."
```

```encounter-table
name: Fuath
creatures:
  - 1: Fuath
```
