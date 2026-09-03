---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Runaway Blueblood"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Runaway Blueblood"
level: 3
source: "NPC Core"
aon_id: "creature-3508"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3508"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Runaway Blueblood"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Genealogy Lore]] +9, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11"
abilityMods: [1, 3, 0, 2, 0, 4]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/firearm/dueling-pistol|Dueling Pistol]] (10 rounds), fine clothing, signet ring, Shortsword"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +10; __Will__: +9"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dueling pistol +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], range increment 60 feet, reload 1) __Damage__ 1d6+4 piercing __“Courageous” Retreat__ ⬻"
abilities_bot:
  - name: "Requirements"
    desc: "The runaway blueblood is adjacent to at least one enemy"
  - name: "Effect"
    desc: "The runaway blueblood gains the [[srd/pf2e/compendium/rules-elements/conditions#Fleeing|fleeing]] condition, gains a +5- foot status bonus to their Speed, and gains a +2 circumstance bonus to their AC against reactions triggered by their movement. The blueblood Strides. The effects last until the end of the blueblood's current turn."
  - name: "Sneak Attack"
    desc: "The runaway blueblood deals an extra 1d6 damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 77."
```

```encounter-table
name: Runaway Blueblood
creatures:
  - 1: Runaway Blueblood
```
