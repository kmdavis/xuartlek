---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Duskwalker Ghost Hunter"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/duskwalker
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Duskwalker Ghost Hunter"
level: 4
source: "Monster Core"
aon_id: "creature-3139"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3139"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Duskwalker Ghost Hunter"
level: "Creature 4"
size: "Medium"
trait_01: "Duskwalker"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Uncommon"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [2, 4, 1, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows), Hatchet (2), Leather Armor"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +10 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects"
hp: 56
health:
  - name: "HP"
    desc: "56; __Immunities__ effects that would transform their body or soul to an [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] 2"
abilities_mid:
  - name: "Ghost Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The duskwalker is targeted by a Strike or spell"
  - name: "Effect"
    desc: "The duskwalker gains a +2 circumstance bonus to AC, resistance 5 to [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] damage, and increases their resistance to [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] damage to 5, all against the triggering attack."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hatchet +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+5 slashing"
  - name: "Ranged"
    desc: "⬻ composite longbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 1d8+4 piercing"
  - name: "Ranged"
    desc: "⬻ hatchet +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d6+5 slashing"
abilities_bot:
  - name: "Ghost Hunter"
    desc: "The duskwalker's weapons have the benefits of the [[srd/pf2e/compendium/equipment/runes/ghost-touch|_ghost touch_]] property rune on attacks against [[srd/pf2e/compendium/rules-elements/traits/gm-core/incorporeal|incorporeal]] [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]]."
  - name: "Spirit Hunter"
    desc: "⬻ The duskwalker designates a single creature they can observe as their prey. The duskwalker gains a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] checks, and [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] checks against their prey and to any check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] about it, and deal an additional 2 spirit damage with all weapon Strikes against their prey. These effects last until the duskwalker uses Spirit Hunter again."
  - name: "Spirit Shot"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The duskwalker has designated a creature as their prey using Spirit Hunter"
  - name: "Effect"
    desc: "The duskwalker makes two ranged Strikes against their prey. If both Strikes hit, combine their damage for the purpose of resistances and weaknesses."
sourcebook: "_Monster Core_, page 266."
```

```encounter-table
name: Duskwalker Ghost Hunter
creatures:
  - 1: Duskwalker Ghost Hunter
```
