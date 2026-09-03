---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Farmer"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Farmer"
level: 0
source: "NPC Core"
aon_id: "creature-3492"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3492"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Farmer"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Farming Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +4, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [3, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "apple, pitchfork, work clothes (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]])"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +5; __Will__: +4"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pitchfork +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ apple +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d4+3 bludgeoning"
abilities_bot:
  - name: "Pitch Bale"
    desc: "⬻"
  - name: "Requirements"
    desc: "The farmer's last action was a successful pitchfork Strike"
  - name: "Effect"
    desc: "The farmer moves the creature they hit with their pitchfork up to 5 feet, and the target falls [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. The target can attempt a DC 13 Reflex save to avoid falling prone and avoids being moved altogether on a critical success."
sourcebook: "_NPC Core_, page 67."
```

```encounter-table
name: Farmer
creatures:
  - 1: Farmer
```
