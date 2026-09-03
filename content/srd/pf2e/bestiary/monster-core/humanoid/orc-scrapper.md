---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Scrapper"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Scrapper"
level: 0
source: "Monster Core"
aon_id: "creature-3129"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3129"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Orc Scrapper"
level: "Creature 0"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Orcish|Orcish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +2"
abilityMods: [3, 2, 2, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "shoddy breastplate, Javelin (3), Orc Knuckle Dagger (2)"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +4; __Will__: +2"
hp: 18
health:
  - name: "HP"
    desc: "18"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ orc knuckle dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]]) __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+3 piercing"
sourcebook: "_Monster Core_, page 258."
```

```encounter-table
name: Orc Scrapper
creatures:
  - 1: Orc Scrapper
```
