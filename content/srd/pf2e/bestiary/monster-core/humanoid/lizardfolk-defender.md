---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lizardfolk Defender"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/lizardfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Lizardfolk Defender"
level: 1
source: "Monster Core"
aon_id: "creature-3090"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3090"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lizardfolk Defender"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], Iruxi"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [3, 2, 3, -1, 2, 0]
abilities_top:
  - name: "Deep Breath"
    desc: "A lizardfolk defender can hold their breath for 15 minutes."
  - name: "Items"
    desc: "Flail, Javelin (3), Wooden Shield (Hardness 3, HP 12, BT 6)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +7; __Will__: +5"
hp: 21
health:
  - name: "HP"
    desc: "21"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet, swim 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flail +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d6+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ tail +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Terrain Advantage"
    desc: "Non-[[srd/pf2e/compendium/rules-elements/traits/player-core-2/lizardfolk|lizardfolk]] creatures that are in difficult terrain or are in water and lack a swim Speed are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the lizardfolk defender."
sourcebook: "_Monster Core_, page 226."
```

```encounter-table
name: Lizardfolk Defender
creatures:
  - 1: Lizardfolk Defender
```
