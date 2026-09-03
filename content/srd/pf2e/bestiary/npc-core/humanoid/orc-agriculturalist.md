---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orc Agriculturalist"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/medium
statblock: inline
name: "Orc Agriculturalist"
level: 1
source: "NPC Core"
aon_id: "creature-3662"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3662"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Orc Agriculturalist"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Common, Orcish"
skills:
  - name: "Skills"
    desc: "Athletics +5, Crafting +3, Farming Lore +13, Nature +11, Survival +7"
abilityMods: [2, 1, 2, 0, 4, 0]
abilities_top:
  - name: "Farming Specialist"
    desc: "For encounters involving farming, harvesting, or identifying plants, the agriculturalist is a 5th-level challenge."
  - name: "Items"
    desc: "Blowgun (20 darts), pitchfork (as longspear), poisonous herb (5), Sickle"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +9; __Ref__: +6; __Will__: +7"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pitchfork +7 (Reach) __Damage__ 1d8+2 piercing"
  - name: "Melee"
    desc: "⬻ sickle +7 (Agile, Trip) __Damage__ 1d4+2 slashing"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ blowgun +6 (Agile, Nonlethal, range increment 20 feet, reload 1) __Damage__ 1 piercing"
abilities_bot:
  - name: "Herbal Poison"
    desc: "⬻ (Manipulate, Poison) The agriculturalist quickly turns some of their supplies of poisonous herbs into an herbal poison, then applies it to a melee weapon or piece of ammunition in their possession. The next successful attack with a weapon poisoned this way deals an additional 1d6 poison damage. The applied poison fades after its damage is applied to an attack or 1 minute passes, whichever happens first."
  - name: "Poison Detector"
    desc: "⬺ The orc agriculturalist attempts a Farming Lore or Nature check to determine whether an object is poison or has been poisoned. The DC is the poison's DC (if any), or the standard DC of the poison's level. On a critical success, they also learn the number and types of poison involved."
sourcebook: "_NPC Core_, page 206."
```

```encounter-table
name: Orc Agriculturalist
creatures:
  - 1: Orc Agriculturalist
```
