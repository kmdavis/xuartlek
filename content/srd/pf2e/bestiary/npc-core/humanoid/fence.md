---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fence"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Fence"
level: 5
source: "NPC Core"
aon_id: "creature-3430"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3430"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Fence"
level: "Creature 5"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Accounting Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +15"
abilityMods: [0, 3, 0, 4, 2, 4]
abilities_top:
  - name: "Fence's Eye"
    desc: "Fences can use [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] to identify an item's value and [[srd/pf2e/compendium/rules-elements/actions/player-core#Identify Magic|Identify Magic]] on an item. They gain a +2 circumstance bonus to Underworld Lore checks when doing so, and to all Underworld Lore checks related to stolen items."
  - name: "Items"
    desc: "Dagger (10), lesser darkvision elixir, Disguise Kit, Shortsword, [[srd/pf2e/compendium/equipment/alchemical-items/smoke-ball-greater|lesser smoke ball]] (2), [[srd/pf2e/compendium/equipment/adventuring-gear/thieves-toolkit-infiltrator-picks|Thieves' Toolkit]]"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +9; __Ref__: +12; __Will__: +15"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ dagger +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Fence's Feint"
    desc: "⬻ The fence [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feints]], then can Step. If the Feint succeeds, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the fence's melee attacks until the end of the fence's next turn (or to all melee attacks on a critical success)."
  - name: "Quick Rummage"
    desc: "⬻ The fence always has a few items close at hand. The fence Interacts to draw a weapon or an item that takes a single action to activate, and then Strikes with the weapon or Activates the Item."
  - name: "Sneak Attack"
    desc: "The fence deals an extra 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 21."
```

```encounter-table
name: Fence
creatures:
  - 1: Fence
```
