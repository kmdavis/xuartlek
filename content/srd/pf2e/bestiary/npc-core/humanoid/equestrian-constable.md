---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Equestrian Constable"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Equestrian Constable"
level: 4
source: "NPC Core"
aon_id: "creature-3557"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3557"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Equestrian Constable"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Settlement Lore]] +8"
abilityMods: [4, 1, 3, 0, 2, 1]
abilities_top:
  - name: "Trained Animal"
    desc: "The equestrian constable rides a trained mount of their level or lower, usually a [[srd/pf2e/bestiary/monster-core/animal/war-horse|war horse]] or, for elite equestrian constables, a [[srd/pf2e/bestiary/npc-core/animal/veteran-war-horse|veteran war horse]]. The animal has the standard number of actions, uses its normal stat block, and counts toward the encounter's XP budget normally."
  - name: "Items"
    desc: "Crossbow (20 bolts), Guisarme, Half Plate, poor manacles, Rope, Signal Whistle"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +8; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Opportune Maneuver"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet uses an action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] trait or leaves a space within the constable's reach during its move action"
  - name: "Effect"
    desc: "The constable attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] the triggering creature. On a success, the triggering action is [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupted]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ guisarme +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d8+8 slashing plus Knockdown"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +11 (range increment 120 feet, reload 1) __Damage__ 1d8+4 piercing"
abilities_bot:
  - name: "Vigilant Vantage"
    desc: "⬻ The equestrian constable [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeks]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Point Out|Points Out]] a target. They can Interact to draw an item or [[srd/pf2e/compendium/rules-elements/actions/player-core#Command an Animal|Command an Animal]] to approach or attack the target."
sourcebook: "_NPC Core_, page 113."
```

```encounter-table
name: Equestrian Constable
creatures:
  - 1: Equestrian Constable
```
