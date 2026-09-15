---
noteType: pf2eMonster
aliases: "Tonic Merchant"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tonic Merchant"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3483"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tonic Merchant"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "+6"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +11, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +10, [[srd/pf2e/compendium/rules-elements/skills/Lore|Mercantile Lore]] +9, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +9"
abilityMods: [0, 2, 1, 4, 1, 2]
abilities_top:
  - name: "Items"
    desc: "moderate acid flask (×8), [[srd/pf2e/compendium/equipment/adventuring-gear/Alchemist's Toolkit|Alchemist's Toolkit]], Dagger, formula book, [[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit|Healer's Toolkit]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +9; __Will__: +8"
hp: 50
health:
  - name: "HP"
    desc: "50"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ acid flask +10 ([[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|Splash]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]]) __Damage__ 2d6 persistent acid damage plus 2 acid [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Healing Bomb"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]]) The tonic merchant quickly crafts a [[srd/pf2e/compendium/equipment/alchemical-items/Antidote|lesser antidote]], [[srd/pf2e/compendium/equipment/alchemical-items/Antiplague|lesser antiplague]], or [[srd/pf2e/compendium/equipment/alchemical-items/Elixir of Life|minor elixir of life]] and lobs it at a willing or [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] ally within 30 feet. The elixir affects the ally as though they imbibed it. The tonic merchant can use the rarest materials in their toolkit to improve the item to a moderate antidote, moderate antiplague, or lesser elixir of life. Afterward, they must spend 10 minutes gathering new ingredients before they can do so again."
sourcebook: "_NPC Core_, page 62."
```

```encounter-table
name: Tonic Merchant
creatures:
  - 1: Tonic Merchant
```
