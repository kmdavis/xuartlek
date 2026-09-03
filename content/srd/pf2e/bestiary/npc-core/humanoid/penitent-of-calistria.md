---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Penitent Of Calistria"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Penitent Of Calistria"
level: 0
source: "NPC Core"
aon_id: "creature-3438"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3438"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Penitent Of Calistria"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/lore|Calistria Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +3, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +4"
abilityMods: [2, 1, 2, 0, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Dagger, Explorer's Clothing, [[srd/pf2e/compendium/equipment/adventuring-gear/religious-symbol-silver|religious symbol]] of Calistria, Whip"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +5; __Will__: +6"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+2 slashing"
  - name: "Melee"
    desc: "⬻ dagger +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
abilities_bot:
  - name: "Agonizing Drive"
    desc: "The penitent ignores the penalty to attack rolls from being [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] and gains a status bonus to damage rolls equal to their frightened value."
  - name: "Repentant Defiance"
    desc: "⬺ The penitent Strikes, then increases their own [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] value by 2 and deals 3 slashing damage to themselves, bypassing resistance. The penitent then gains resistance 3 to physical damage until the start of their next turn."
sourcebook: "_NPC Core_, page 28."
```

```encounter-table
name: Penitent Of Calistria
creatures:
  - 1: Penitent Of Calistria
```
