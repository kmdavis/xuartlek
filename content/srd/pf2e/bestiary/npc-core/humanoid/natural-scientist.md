---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Natural Scientist"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Natural Scientist"
level: 2
source: "NPC Core"
aon_id: "creature-3468"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3468"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Natural Scientist"
level: "Creature 2"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +8, [[srd/pf2e/compendium/rules-elements/skills/lore|Scouting Lore]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [1, 1, 2, 2, 4, 1]
abilities_top:
  - name: "Never Lost"
    desc: "The natural scientist can always tell true north and gains a +4 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]]. They don't take a –2 item penalty to the check if they don't have a [[srd/pf2e/compendium/equipment/adventuring-gear/compass-lensatic|compass]]."
  - name: "Trained Observer"
    desc: "The natural scientist is accustomed to blending into their surroundings and taking notes, giving them a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core#Gather Information|Gather Information]]."
  - name: "Items"
    desc: "Explorer's Clothing, Staff, Writing Set"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +8; __Ref__: +5; __Will__: +11"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-handed d8]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4+3 bludgeoning Natural Sciences And Those Who Study Them There's a wide variety of things to explore and notate, and natural scientists want to document it all:"
abilities_bot:
  - name: "Astronomers"
    desc: "make detailed observations of the night sky."
  - name: "Biologists"
    desc: "may study the impact of civilization on wilderness areas."
  - name: "Botanists"
    desc: "may protect a newly discovered plant species."
  - name: "Chemists"
    desc: "may try to locate the source of a mysterious oil."
  - name: "Geologists"
    desc: "may rush to study a volcano."
  - name: "Zoologists"
    desc: "may try to track down a rare and elusive animal."
sourcebook: "_NPC Core_, page 53."
```

```encounter-table
name: Natural Scientist
creatures:
  - 1: Natural Scientist
```
