---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nagaji Soldier"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/nagaji
  - pf2e/creature/trait/medium
statblock: inline
name: "Nagaji Soldier"
level: 2
source: "Monster Core 2"
aon_id: "creature-4486"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4486"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nagaji Soldier"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Nagaji"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +5"
abilityMods: [4, 1, 3, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/sword/khopesh-weapon-476|Khopesh]], [[srd/pf2e/compendium/equipment/armor#Leather Armor|Leather Armor]], [[srd/pf2e/compendium/equipment/weapons/bow/longbow|Longbow]] (with 20 arrows)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +9; __Ref__: +7; __Will__: +6"
hp: 28
health:
  - name: "HP"
    desc: "28; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 2"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ khopesh +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d8+4 slashing"
  - name: "Ranged"
    desc: "⬻ longbow +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8 piercing"
abilities_bot:
  - name: "Slough Toxins"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The nagaji is afflicted with a poison"
  - name: "Effect"
    desc: "The nagaji accelerates their metabolism. They roll a saving throw against the affliction with a +2 circumstance bonus. If they must attempt an ongoing save against the same poison at the end of their turn, they also get a +2 circumstance bonus to that save."
sourcebook: "_Monster Core 2_, page 232."
```

```encounter-table
name: Nagaji Soldier
creatures:
  - 1: Nagaji Soldier
```
