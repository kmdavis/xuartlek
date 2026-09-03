---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Physician"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Physician"
level: -1
source: "NPC Core"
aon_id: "creature-3480"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3480"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Physician"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; (8 to notice ailments)"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +12, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +5"
abilityMods: [-1, 1, 1, 4, 2, 2]
abilities_top:
  - name: "Medical Specialist"
    desc: "For medical matters, the physician is a 4th-level challenge."
  - name: "Bedside Manner"
    desc: "A physician has a +4 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] on or make a [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] of a [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|diseased]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poisoned]], or wounded creature."
  - name: "Doctor's Hand"
    desc: "When the physician rolls a critical failure on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Disease|Treat Disease]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Poison|Treat Poison]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Treat Wounds|Treat Wounds]], they get a failure instead."
  - name: "Items"
    desc: "minor elixir of life (2), [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|Healer's Toolkit]], medical textbook"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +9; __Ref__: +3; __Will__: +8"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4–1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ medical textbook +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4–1 bludgeoning"
sourcebook: "_NPC Core_, page 60."
```

```encounter-table
name: Physician
creatures:
  - 1: Physician
```
