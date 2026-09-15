---
noteType: pf2eMonster
aliases: "Archer Sentry"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Archer Sentry"
level: 2
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3552"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Archer Sentry"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 11
perception:
  - name: "Perception"
    desc: "+11"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +4"
abilityMods: [2, 4, 1, 0, 3, 0]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (100 arrows), Leather Armor, Shortsword, Signal Whistle"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite longbow +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Sentry's Aim"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The archer sentry aims carefully and fires. They make a ranged weapon Strike with a +1 circumstance bonus. The Strike ignores the [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] condition, lesser cover, and standard cover, and reduces greater cover to standard cover."
sourcebook: "_NPC Core_, page 111."
```

```encounter-table
name: Archer Sentry
creatures:
  - 1: Archer Sentry
```
