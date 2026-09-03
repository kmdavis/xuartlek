---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bugbear Prowler"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/bugbear
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bugbear Prowler"
level: 2
source: "Monster Core"
aon_id: "creature-2860"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2860"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bugbear Prowler"
level: "Creature 2"
size: "Medium"
trait_01: "Bugbear"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [4, 2, 3, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Bastard Sword, Javelin (3), Leather Armor"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +8; __Will__: +5"
hp: 34
health:
  - name: "HP"
    desc: "34"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bastard sword +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d12]]) __Damage__ 1d8+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Bushwhack"
    desc: "⬻ The bugbear prowler Strides up to 10 feet and attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] a creature they're [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] by. If they succeed, they also deal fist damage to that creature."
  - name: "Mauler"
    desc: "The bugbear prowler gains a +3 circumstance bonus to damage rolls against creatures they have [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]."
sourcebook: "_Monster Core_, page 47."
```

```encounter-table
name: Bugbear Prowler
creatures:
  - 1: Bugbear Prowler
```
