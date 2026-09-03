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
languages: "Common"
skills:
  - name: "Skills"
    desc: "Accounting Lore +13, Acrobatics +10, Crafting +13, Deception +13, Diplomacy +11, Intimidation +11, Society +11, Stealth +10, Thievery +10, Underworld Lore +15"
abilityMods: [0, 3, 0, 4, 2, 4]
abilities_top:
  - name: "Fence's Eye"
    desc: "Fences can use Underworld Lore to identify an item's value and Identify Magic on an item. They gain a +2 circumstance bonus to Underworld Lore checks when doing so, and to all Underworld Lore checks related to stolen items."
  - name: "Items"
    desc: "Dagger (10), lesser darkvision elixir, Disguise Kit, Shortsword, lesser smoke ball (2), Thieves' Toolkit"
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
    desc: "⬻ shortsword +14 (Agile, Finesse, versatile S) __Damage__ 1d6+6 piercing"
  - name: "Melee"
    desc: "⬻ dagger +14 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +14 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Fence's Feint"
    desc: "⬻ The fence Feints, then can Step. If the Feint succeeds, the target is off-guard against the fence's melee attacks until the end of the fence's next turn (or to all melee attacks on a critical success)."
  - name: "Quick Rummage"
    desc: "⬻ The fence always has a few items close at hand. The fence Interacts to draw a weapon or an item that takes a single action to activate, and then Strikes with the weapon or Activates the Item."
  - name: "Sneak Attack"
    desc: "The fence deals an extra 2d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 21."
```

```encounter-table
name: Fence
creatures:
  - 1: Fence
```
