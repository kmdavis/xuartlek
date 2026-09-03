---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arms Dealer"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Arms Dealer"
level: 2
source: "NPC Core"
aon_id: "creature-3506"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3506"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Arms Dealer"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (11 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Firearm Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +9"
abilityMods: [0, 3, 0, 1, 3, 3]
abilities_top:
  - name: "Arms Dealing Specialist"
    desc: "For encounters involving the purchase of weapons, the arms dealer is a 5th-level challenge."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/firearm/flintlock-musket-weapon-521|Flintlock Musket]] (20 rounds), [[srd/pf2e/compendium/equipment/weapons/firearm/hand-cannon|Hand Cannon]] (20 rounds), [[srd/pf2e/compendium/equipment/assistive-items/cane|sword cane]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +7; __Will__: +9"
hp: 28
health:
  - name: "HP"
    desc: "28 __You Call That a Gun?__ The arms dealer seems unaffected by your attempts to threaten them. The arms dealer gains a +2 circumstance bonus to their Will DC against [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] checks while they're holding a firearm."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sword cane +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ flintlock musket +11 ([[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], range increment 70 feet, reload 1) __Damage__ 1d6+3 piercing"
  - name: "Ranged"
    desc: "⬻ hand cannon +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core-2/modular|modular B]], or S; range increment 30 feet; reload 1) __Damage__ 1d6+3 modular"
abilities_bot:
  - name: "Take Stock"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The arms dealer advises an ally on how to properly use a firearm. The arms dealer chooses an ally within 30 feet wielding a firearm. That ally can use a reaction to Interact to reload their firearm."
sourcebook: "_NPC Core_, page 76."
```

```encounter-table
name: Arms Dealer
creatures:
  - 1: Arms Dealer
```
