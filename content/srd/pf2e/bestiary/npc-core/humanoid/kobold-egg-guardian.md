---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Egg Guardian"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Egg Guardian"
level: 3
source: "NPC Core"
aon_id: "creature-3655"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3655"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Kobold Egg Guardian"
level: "Creature 3"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +9"
abilityMods: [3, 3, 1, 0, 0, 3]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Leather Armor, Longspear"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +12; __Will__: +6"
hp: 48
health:
  - name: "HP"
    desc: "48"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d8+5 piercing"
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +12 (range increment 120 feet, reload 1) __Damage__ 1d8+2 piercing"
abilities_bot:
  - name: "Immobilizing Thrust"
    desc: "⬺ The kobold egg guardian makes a longspear Strike. If the Strike hits, the target must attempt a DC 20 Reflex save. On a failure, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until the kobold egg guardian moves, attacks with the longspear, or is no longer wielding the longspear."
  - name: "Luring Retreat"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The kobold egg guardian screams and Strides up to their Speed. Each enemy who sees or hears the kobold egg guardian must succeed at a DC 17 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by the egg guardian for 1 round. On the creature's turn, it must use at least 1 action (or 2 actions on a critical failure) to move closer to the kobold egg guardian (while avoiding obvious dangers). Regardless of the result of the save, targets are then immune to Luring Retreat for 24 hours."
sourcebook: "_NPC Core_, page 198."
```

```encounter-table
name: Kobold Egg Guardian
creatures:
  - 1: Kobold Egg Guardian
```
