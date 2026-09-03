---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Court Historian"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Court Historian"
level: -1
source: "NPC Core"
aon_id: "creature-3415"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3415"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Court Historian"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Genealogy Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Scribing Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9"
abilityMods: [0, 1, -1, 5, 3, 2]
abilities_top:
  - name: "Historical Specialist"
    desc: "In matters regarding history or court records, the court historian is a 5th-level challenge."
  - name: "Records Don't Lie"
    desc: "The court historian has a Perception DC of 25 against [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks asserting false current or historical events."
  - name: "Items"
    desc: "court record, [[srd/pf2e/compendium/equipment/adventuring-gear/clothing-desert|fine clothing]], inkwell, Writing Set"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +3; __Ref__: +5; __Will__: +9"
hp: 7
health:
  - name: "HP"
    desc: "7"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ inkwell +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "Distracting Diatribe"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The court historian monotonously recites facts to distract a creature within 30 feet that can hear them. The target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] for 1 round."
sourcebook: "_NPC Core_, page 12."
```

```encounter-table
name: Court Historian
creatures:
  - 1: Court Historian
```
