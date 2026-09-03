---
obsidianUIMode: preview
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
aon_id: "creature-4424"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4424"
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
    desc: "Perception +8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +7"
abilityMods: [1, 4, 2, 1, 3, -1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/dart/dart|darts]] (6)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +9; __Will__: +6"
hp: 18
health:
  - name: "HP"
    desc: "18; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/cold-iron-object-high-grade|cold iron]] 2, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 2"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A fuath becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (or increases its drained condition by 1) after every consecutive hour they're exposed to sunlight. Being submerged in more than a foot of water prevents the sunlight from harming the fuath."
speed: "20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6+1 slashing"
  - name: "Ranged"
    desc: "⬻ dart +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], range increment 20 feet) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Viscous Choke"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The fuath surrounds the head of one air-breathing creature within 30 feet in a magical film of viscous water for 1 minute. The target must succeed at a DC 17 Reflex save or it begins to choke and must hold its breath to avoid [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Drowning and Suffocating|drowning]]. The film can be temporarily wiped away with a total of 3 Interact actions by the choking creature or creatures adjacent to it, allowing a new Reflex save with a +2 circumstance bonus to end the effect. (These actions don't need to be consecutive or made by the same creature.) Fuath Guardians Lone fuaths sometimes appoint themselves guardians of nature, protecting spawning grounds from overfishing or preventing careless cutting of peat bogs. Most, however, are unrepentant saboteurs."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/create-water|Create Water]], [[srd/pf2e/compendium/spells/rank-1/sleep|Sleep]]"
sourcebook: "_Monster Core 2_, page 177."
```

```encounter-table
name: Fuath
creatures:
  - 1: Fuath
```
