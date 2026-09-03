---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "High Roller"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "High Roller"
level: 11
source: "NPC Core"
aon_id: "creature-3511"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3511"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "High Roller"
level: "Creature 11"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; (26 for [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +24, [[srd/pf2e/compendium/rules-elements/skills/lore|Games Lore]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +21, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +22"
abilityMods: [1, 5, 0, 2, 3, 5]
abilities_top:
  - name: "Items"
    desc: "Playing Cards (54-card deck), [[srd/pf2e/compendium/equipment/held-items/predictable-silver-piece|_predictable silver piece_]], _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/rapier|rapier]]_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +17; __Ref__: +24; __Will__: +22"
hp: 150
health:
  - name: "HP"
    desc: "150"
abilities_mid:
  - name: "Tip the Scales"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|fortune]])"
  - name: "Trigger"
    desc: "A creature the high roller is observing critically fails a check"
  - name: "Effect"
    desc: "The high roller picks up on luck that others dropped. They roll twice on their next d20 roll before the end of their next turn and take the better result."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d6+11 piercing"
  - name: "Melee"
    desc: "⬻ fist +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+11 bludgeoning"
  - name: "Melee"
    desc: "⬻ card +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d4+11 slashing"
  - name: "Ranged"
    desc: "⬻ card +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 2d4+11 slashing"
abilities_bot:
  - name: "Lucky Momentum"
    desc: "⬻"
  - name: "Requirements"
    desc: "The high roller's last action was a critical success"
  - name: "Effect"
    desc: "The high roller either Strides twice or attempts a Strike that deals an additional 4d6 precision damage and deals half damage on a failure (but not a critical failure)."
  - name: "Royal Flush Flurry"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Requirements"
    desc: "The high roller has at least 16 cards in one hand"
  - name: "Effect"
    desc: "The high roller unleashes the cards in a 30-foot cone, dealing 16d4 slashing damage to all creatures in the area with a DC 30 basic Reflex save. This ability expends the full deck of cards held."
sourcebook: "_NPC Core_, page 79."
```

```encounter-table
name: High Roller
creatures:
  - 1: High Roller
```
