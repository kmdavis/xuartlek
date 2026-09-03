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
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +11, Diplomacy +9, Medicine +10, Mercantile Lore +9, Society +9"
abilityMods: [0, 2, 1, 4, 1, 2]
abilities_top:
  - name: "Items"
    desc: "moderate acid flask (×8), Alchemist's Toolkit, Dagger, formula book, Healer's Toolkit"
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
    desc: "⬻ dagger +10 (Agile, Finesse, versatile S) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ acid flask +10 (Splash, thrown 30 feet) __Damage__ 2d6 persistent acid damage plus 2 acid splash damage"
  - name: "Ranged"
    desc: "⬻ dagger +10 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Healing Bomb"
    desc: "⬺ (Manipulate) The tonic merchant quickly crafts a lesser antidote, lesser antiplague, or minor elixir of life and lobs it at a willing or unconscious ally within 30 feet. The elixir affects the ally as though they imbibed it. The tonic merchant can use the rarest materials in their toolkit to improve the item to a moderate antidote, moderate antiplague, or lesser elixir of life. Afterward, they must spend 10 minutes gathering new ingredients before they can do so again."
sourcebook: "_NPC Core_, page 62."
```

```encounter-table
name: Tonic Merchant
creatures:
  - 1: Tonic Merchant
```
