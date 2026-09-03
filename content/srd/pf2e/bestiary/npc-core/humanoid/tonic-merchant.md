---
obsidianUIMode: preview
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
aon_id: "creature-3483"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3483"
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
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +10, [[srd/pf2e/compendium/rules-elements/skills/lore|Mercantile Lore]] +9, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9"
abilityMods: [0, 2, 1, 4, 1, 2]
abilities_top:
  - name: "Items"
    desc: "moderate acid flask (×8), [[srd/pf2e/compendium/equipment/adventuring-gear/alchemists-toolkit|Alchemist's Toolkit]], Dagger, formula book, [[srd/pf2e/compendium/equipment/adventuring-gear/healers-toolkit-expanded|Healer's Toolkit]]"
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
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ acid flask +10 ([[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 2d6 persistent acid damage plus 2 acid [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Healing Bomb"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The tonic merchant quickly crafts a [[srd/pf2e/compendium/equipment/alchemical-items/antidote-major|lesser antidote]], [[srd/pf2e/compendium/equipment/alchemical-items/antiplague-major|lesser antiplague]], or [[srd/pf2e/compendium/equipment/alchemical-items/elixir-of-life-true|minor elixir of life]] and lobs it at a willing or [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] ally within 30 feet. The elixir affects the ally as though they imbibed it. The tonic merchant can use the rarest materials in their toolkit to improve the item to a moderate antidote, moderate antiplague, or lesser elixir of life. Afterward, they must spend 10 minutes gathering new ingredients before they can do so again."
sourcebook: "_NPC Core_, page 62."
```

```encounter-table
name: Tonic Merchant
creatures:
  - 1: Tonic Merchant
```
