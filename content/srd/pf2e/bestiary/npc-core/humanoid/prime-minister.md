---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Prime Minister"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Prime Minister"
level: 0
source: "NPC Core"
aon_id: "creature-3550"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3550"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Prime Minister"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; (19 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 3 additional languages spoken in their nation"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +22, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +22, [[srd/pf2e/compendium/rules-elements/skills/lore|Guild Lore]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +19, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +19, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +22"
abilityMods: [0, 2, 1, 3, 3, 4]
abilities_top:
  - name: "Political Specialist"
    desc: "For encounters involving politics, the prime minister is a 10th-level challenge."
  - name: "Unshakable Confidence"
    desc: "All attempts to [[srd/pf2e/compendium/rules-elements/actions/war-of-immortals#Arrow Splits Arrow|Coerce]] the prime minister have a result one degree worse."
  - name: "Items"
    desc: "Rapier"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +6; __Ref__: +3; __Will__: +19"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Cutting Counterpoint"
    desc: "⬲"
  - name: "Trigger"
    desc: "The prime minister hears a creature attempt a [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]], [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]], or an [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check against any creature other than the prime minister"
  - name: "Effect"
    desc: "The prime minister interrupts with a witty barb, cutting the credibility of the creature's argument. The prime minister attempts their own check of the same type. If the result is higher than that of the triggering check, the triggering check is considered a failure regardless of its roll. In extended negotiations, like a Victory Point challenge, the prime minister can't use this ability again until every creature in the discussion has had an opportunity to attempt a check (even if they decide not to make one)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6 piercing"
  - name: "Melee"
    desc: "⬻ fist +5 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
sourcebook: "_NPC Core_, page 110."
```

```encounter-table
name: Prime Minister
creatures:
  - 1: Prime Minister
```
