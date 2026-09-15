---
noteType: pf2eMonster
aliases: "Merchant"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Merchant"
level: -1
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3412"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Merchant"
level: "Creature -1"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +12, [[srd/pf2e/compendium/rules-elements/skills/Lore|Mercantile Lore]] +12, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +8, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +8"
abilityMods: [2, 0, -1, 2, 2, 3]
abilities_top:
  - name: "Sales Specialist"
    desc: "For encounters involving negotiation or mercantile skill, a merchant is a 4th-level challenge."
  - name: "Appraising Eye"
    desc: "The merchant can use [[srd/pf2e/compendium/gm/creature-families/Ant|Mercantile Lore]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] about items, including determining their value. They can also attempt to [[srd/pf2e/compendium/rules-elements/actions/player-core#Identify Magic|Identify Magic]] using Mercantile Lore and can do so without first knowing whether the item is [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]."
  - name: "Items"
    desc: "Club, Padded Armor"
ac: 13
armorclass:
  - name: "AC"
    desc: "13; __Fort__: +1; __Ref__: +2; __Will__: +10"
hp: 7
health:
  - name: "HP"
    desc: "7"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +4 __Damage__ 1d6+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ club +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]]) __Damage__ 1d6+2 bludgeoning"
sourcebook: "_NPC Core_, page 8."
```

```encounter-table
name: Merchant
creatures:
  - 1: Merchant
```
