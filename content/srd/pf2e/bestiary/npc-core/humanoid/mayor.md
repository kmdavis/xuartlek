---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mayor"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mayor"
level: 0
source: "NPC Core"
aon_id: "creature-3549"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3549"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mayor"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; up to 2 additional languages spoken in their settlement"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/lore|Guild Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +13"
abilityMods: [0, 2, 1, 1, 2, 3]
abilities_top:
  - name: "Political Specialist"
    desc: "For encounters involving seeking political favors, the mayor is a 6th-level challenge."
  - name: "Pulse of the Electorate"
    desc: "The mayor can quickly find things out, and 1 hour after anyone in their settlement becomes aware of an event or activity, the mayor becomes aware of it, so long as they have had time to hobnob with their constituents."
  - name: "Items"
    desc: "decorative sword of station (functions as [[srd/pf2e/compendium/equipment/weapons/sword/shortsword|shortsword]])"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +6; __Ref__: +3; __Will__: +14"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "But Will It Lose Me Votes"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Trigger"
    desc: "A creature succeeds (but doesn't critically succeed) at a [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] check to make a [[srd/pf2e/compendium/rules-elements/actions/player-core#Request|Request]] of the mayor"
  - name: "Effect"
    desc: "The triggering creature (or one of its allies) must attempt the check again within the next hour, this time against the mayor's [[srd/pf2e/compendium/rules-elements/skills/society|Society]] DC. Society or a relevant [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] skill may be used for this check instead of Diplomacy."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ decorative sword of station +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6 piercing"
  - name: "Melee"
    desc: "⬻ fist +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4 bludgeoning"
sourcebook: "_NPC Core_, page 109."
```

```encounter-table
name: Mayor
creatures:
  - 1: Mayor
```
