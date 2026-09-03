---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Miner"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Miner"
level: 0
source: "NPC Core"
aon_id: "creature-3494"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3494"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Miner"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +3, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Mining Lore]] +4, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [2, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Hammer, Lantern, miner's harness (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), Pick, Piton (5), Rope (100 feet)"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +7; __Ref__: +5; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pick +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]]) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Piton Pin"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Requirements"
    desc: "The miner has their hammer in hand"
  - name: "Effect"
    desc: "The miner Interacts to draw a piton, then hammers it into a creature to pin them in place, attempting an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the target's Reflex DC. On a hit, the target is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until it removes the piton with a successful DC 10 Athletics check made as an Interact action."
sourcebook: "_NPC Core_, page 68."
```

```encounter-table
name: Miner
creatures:
  - 1: Miner
```
