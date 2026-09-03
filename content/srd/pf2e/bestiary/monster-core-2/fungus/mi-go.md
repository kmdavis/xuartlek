---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mi-Go"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Mi-Go"
level: 6
source: "Monster Core 2"
aon_id: "creature-4473"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4473"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mi-Go"
level: "Creature 6"
size: "Medium"
trait_01: "Fungus"
trait_02: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, tremorsense (precise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Mi-Go"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +17, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +15, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +13"
abilityMods: [2, 5, 3, 5, 4, 2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +13; __Ref__: +17; __Will__: +14"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ slashing 5"
abilities_mid:
  - name: "No Breath"
    desc: "A mi-go doesn't breathe and is immune to effects that require breathing (such as an inhaled poison)."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 2d6+4 slashing plus Grab"
abilities_bot:
  - name: "Clever Disguises"
    desc: "The mi-go can use [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonate]] any Medium humanoid creature, although creating such a disguise takes 1 hour. They can't Impersonate a specific individual with this ability."
  - name: "Eviscerate"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The mi-go performs a swift and painful surgery on a creature they have [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] or that's otherwise [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]]attempting a [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] check against the target's Fortitude DC. Regardless of the result the target then becomes temporarily immune for 24 hours."
  - name: "Critical Success"
    desc: "The target takes 6d6 slashing damage, is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for 1 round, and becomes [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1, enfeebled 1, or [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (the mi-go chooses) for 24 hours."
  - name: "Success"
    desc: "The target takes 4d6 slashing damage and is slowed 1 for 1 round by the pain."
  - name: "Failure"
    desc: "The target takes 2d6 slashing damage."
  - name: "Critical Failure"
    desc: "The target takes no damage."
  - name: "Sneak Attack"
    desc: "A mi-go's Strikes deal an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. Mi-Go Language The mi-go language consists of pulsations and flashes of a wide range of colors (some of which can't be seen by humans) generated on a mi-go's head. This language can be learned by other creatures, but they can't use it to “speak” to others without the use of illusion magic capable of generating the complex series of colors. Even then, most creatures can convey only basic notions and concepts."
sourcebook: "_Monster Core 2_, page 221."
```

```encounter-table
name: Mi-Go
creatures:
  - 1: Mi-Go
```
