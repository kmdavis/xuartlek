---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drover"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Drover"
level: 0
source: "NPC Core"
aon_id: "creature-3491"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3491"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Drover"
level: "Creature 0"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/lore|Livestock Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +5"
abilityMods: [3, 2, 2, 0, 1, 0]
abilities_top:
  - name: "Whistling"
    desc: "Drovers can whistle instead of speaking when communicating simple messages (such as “go left,” “split the herd,” and “danger ahead”) to other drovers or when using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Command an Animal|Command an Animal]] action on their herding dogs."
  - name: "Items"
    desc: "lasso, overalls, Signal Whistle, Sling (20 bullets), Whip"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +6; __Will__: +5"
hp: 18
health:
  - name: "HP"
    desc: "18"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|Reach]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 1d4+3 slashing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ sling +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+1 piercing"
abilities_bot:
  - name: "Hogtie"
    desc: "⬺"
  - name: "Requirements"
    desc: "A creature is grappled or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the drover's lasso"
  - name: "Effect"
    desc: "The drover can pull the grappled creature up to 20 feet. Then, if the creature is within reach, the drover hogties it, attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] it again. On a success, the creature is restrained with the lasso, and the drover doesn't need to maintain the grapple. The hogtie lasts until the creature [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] or the lasso is [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Forced Open]]. The drover can Interact to free a hogtied creature within reach."
  - name: "Lasso"
    desc: "⬺ The drover uses their lasso to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] a Large or smaller creature up to 20 feet away. They can continue to Grapple to keep their hold on the target so long as the target remains within 20 feet and they continue to hold the end of the lasso. In addition to the [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] creature being able to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]], a successful DC 16 [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Force Open]] can remove the lasso entirely."
sourcebook: "_NPC Core_, page 67."
```

```encounter-table
name: Drover
creatures:
  - 1: Drover
```
