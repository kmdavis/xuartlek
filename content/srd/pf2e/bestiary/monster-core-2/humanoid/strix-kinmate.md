---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Strix Kinmate"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/strix
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Strix Kinmate"
level: 2
source: "Monster Core 2"
aon_id: "creature-4567"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4567"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Strix Kinmate"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Strix"
trait_03: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Strix"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9"
abilityMods: [2, 4, 0, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/armor#Leather Armor|Leather Armor]], [[srd/pf2e/compendium/equipment/weapons/bow/shortbow|Shortbow]] (20 arrows), [[srd/pf2e/compendium/equipment/weapons/sword/shortsword|Shortsword]]"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +10; __Will__: +7"
hp: 25
health:
  - name: "HP"
    desc: "25"
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ talon +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6+4 slashing"
  - name: "Ranged"
    desc: "⬻ shortbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Strix Camaraderie"
    desc: "Strix kinmates are tightly bonded to one another, adept at teamwork and supporting each other's attacks. If an enemy is within reach of both the kinmate and one other strix, that enemy is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to all strix."
  - name: "Strix Vengeance"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Trigger"
    desc: "The kinmate or a strix ally they can see is damaged by an enemy's critical hit"
  - name: "Effect"
    desc: "Until the end of their next turn, the kinmate gains a +1d6 status bonus to damage rolls on Strikes they make against the triggering enemy."
sourcebook: "_Monster Core 2_, page 307."
```

```encounter-table
name: Strix Kinmate
creatures:
  - 1: Strix Kinmate
```
