---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Inspector"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Inspector"
level: 3
source: "NPC Core"
aon_id: "creature-3554"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3554"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Inspector"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; (15 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Search|Search]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 3 additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +8, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +12"
abilityMods: [1, 3, 0, 4, 3, 1]
abilities_top:
  - name: "Investigation Specialist"
    desc: "For encounters involving investigation, the inspector is a 5th-level challenge."
  - name: "Sense Demise"
    desc: "The inspector can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] on a corpse, learning about the creature in the moments before its death."
  - name: "Items"
    desc: "Leather Armor, Shortsword"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +5; __Ref__: +10; __Will__: +12"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+4 piercing plus 1 precision"
  - name: "Melee"
    desc: "⬻ fist +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning plus 1 precision"
abilities_bot:
  - name: "Unavoidable Question"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]])"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Effect"
    desc: "The inspector [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralizes]] a creature and asks a question. On a success, the next Strike the inspector attempts against that target deals an additional 1d6 precision damage. If the target spends an action on their next turn to answer the question, either truthfully or by succeeding at a DC 25 [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check, they are temporarily immune to the inspector's Unavoidable Question for 1 minute."
sourcebook: "_NPC Core_, page 112."
```

```encounter-table
name: Inspector
creatures:
  - 1: Inspector
```
