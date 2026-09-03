---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Commoner"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Commoner"
level: -1
source: "NPC Core"
aon_id: "creature-3488"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3488"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Commoner"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +2"
abilityMods: [3, 1, 2, 0, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Sickle"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +6; __Ref__: +3; __Will__: +3"
hp: 10
health:
  - name: "HP"
    desc: "10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sickle +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+2 slashing"
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +3 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4+2 bludgeoning"
abilities_bot:
  - name: "Power of the Mob"
    desc: "When three or more commoners are adjacent to each other, each commoner gets a +1 circumstance bonus to [[srd/pf2e/compendium/rules-elements/actions/player-core-2|Athletic]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]], attack rolls, and damage rolls."
sourcebook: "_NPC Core_, page 66."
```

```encounter-table
name: Commoner
creatures:
  - 1: Commoner
```
