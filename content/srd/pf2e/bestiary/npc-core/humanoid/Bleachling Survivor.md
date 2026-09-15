---
noteType: pf2eMonster
aliases: "Bleachling Survivor"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Bleachling Survivor"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3636"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Bleachling Survivor"
level: "Creature 2"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 8
perception:
  - name: "Perception"
    desc: "+8; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Gnomish|Gnomish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +8, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +7, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +8"
abilityMods: [1, 1, 3, 1, 3, 1]
abilities_top:
  - name: "Unflappable"
    desc: "When the bleachling survivor rolls a critical failure on a check with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]] trait, they get a failure instead."
  - name: "Items"
    desc: "Dagger, Longbow (20 arrows)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +8; __Will__: +12"
hp: 34
health:
  - name: "HP"
    desc: "34"
abilities_mid:
  - name: "Flinch Back"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy moves into an adjacent space"
  - name: "Effect"
    desc: "The bleachling survivor Steps up to 10 feet. They must end this movement in a space that is not adjacent to an enemy."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ longbow +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]], reload 0) __Damage__ 1d8 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The bleachling survivor deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 182."
```

```encounter-table
name: Bleachling Survivor
creatures:
  - 1: Bleachling Survivor
```
