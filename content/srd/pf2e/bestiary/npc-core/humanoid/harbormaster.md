---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Harbormaster"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Harbormaster"
level: 3
source: "NPC Core"
aon_id: "creature-3553"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3553"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Harbormaster"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 2 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Fishing Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Sailing Lore]] +10"
abilityMods: [4, 2, 2, 2, 1, 0]
abilities_top:
  - name: "Steady Balance"
    desc: "Whenever the harbormaster rolls a success on a check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Balance|Balance]], they get a critical success instead. They're not [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] while Balancing on narrow surfaces and uneven ground."
  - name: "Items"
    desc: "Fishing Tackle, Hatchet (2), ledger, Manacles, Spyglass"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hatchet +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hatchet +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+7 slashing"
abilities_bot:
  - name: "Experienced Hand"
    desc: "The harbormaster has endured their share of adverse conditions at sea. Any creature that's in adverse weather or aboard a vessel on rough water is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the harbormaster."
sourcebook: "_NPC Core_, page 111."
```

```encounter-table
name: Harbormaster
creatures:
  - 1: Harbormaster
```
