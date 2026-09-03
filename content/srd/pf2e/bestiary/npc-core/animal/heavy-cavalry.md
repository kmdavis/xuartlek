---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Heavy Cavalry"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Heavy Cavalry"
level: 7
source: "NPC Core"
aon_id: "creature-3528"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3528"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Heavy Cavalry"
level: "Creature 7"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Troop"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +15"
abilityMods: [7, 2, 4, 0, 1, 2]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +17; __Ref__: +13; __Will__: +14"
hp: 105
health:
  - name: "HP"
    desc: "105 (4 segments); __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Mounted Troop"
    desc: "Effects that target only [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animals]] or only [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoids]] might not work on the cavalry brigade, subject to the GM's discretion."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet; troop movement"
abilities_bot:
  - name: "Join the Fray"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The heavy cavalry swing flails at each enemy in a 5-foot emanation, with a DC 22 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+3 bludgeoning damage ⬺ 2d6+7 bludgeoning damage ⬽ 3d6+10 bludgeoning damage"
  - name: "Thunder of Hooves"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The heavy cavalry Strides. At the end of their movement, the cavalry can either attempt an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] each adjacent enemy or an [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] each enemy within 30 feet. Roll only once and compare the result to each enemy's Reflex DC (for Trip) or Will DC (for Demoralize)."
  - name: "Trample"
    desc: "⬽ Medium or smaller, 2d8+7 bludgeoning, DC 22; creatures that fail the save are also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
sourcebook: "_NPC Core_, page 92."
```

```encounter-table
name: Heavy Cavalry
creatures:
  - 1: Heavy Cavalry
```
