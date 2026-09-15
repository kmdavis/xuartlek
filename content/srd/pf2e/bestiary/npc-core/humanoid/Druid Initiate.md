---
noteType: pf2eMonster
aliases: "Druid Initiate"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Druid Initiate"
level: 1
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3580"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Druid Initiate"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Wildsong|Wildsong]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +7, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +4, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +7"
abilityMods: [2, 1, 2, 0, 4, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit|Healer's Toolkit]], Leather Armor, [[srd/pf2e/compendium/equipment/adventuring-gear/Primal Symbol|Primal Symbol]], Sling (10 bullets), Staff"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +4; __Will__: +9"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d8]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Spells Primal Spellcasting"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Ignition|Ignition]], [[srd/pf2e/compendium/spells/cantrips/Know the Way|Know the Way]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/Thunderstrike|Thunderstrike]]"
  - name: "Druid Order Spells"
    desc: "DC 17, 1 Focus Point - __1st__ [[srd/pf2e/compendium/spells/focus/Cornucopia|Cornucopia]]"
sourcebook: "_NPC Core_, page 547."
```

```encounter-table
name: Druid Initiate
creatures:
  - 1: Druid Initiate
```
