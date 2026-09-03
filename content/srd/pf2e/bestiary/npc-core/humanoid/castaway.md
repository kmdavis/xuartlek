---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Castaway"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Castaway"
level: 5
source: "NPC Core"
aon_id: "creature-3602"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3602"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Castaway"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +12, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [4, 2, 3, 0, 4, -1]
abilities_top:
  - name: "Items"
    desc: "Blowgun (10 blowgun darts), Hatchet"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +13; __Will__: +11"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Skittish"
    desc: "⬲"
  - name: "Trigger"
    desc: "The castaway takes damage from a Strike"
  - name: "Effect"
    desc: "The castaway Steps away from the source of the Strike."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hatchet +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+7 slashing"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ blowgun +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], reload 1) __Damage__ 1 piercing plus 2d6 poison and 1d6 persistent poison"
abilities_bot:
  - name: "Cockamamie Rant"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The castaway launches into a nonsensical verbal stream of consciousness. Creatures in a 30-foot emanation must succeed at a DC 19 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round. Once a creature has succeeded at a save against the castaway's Cockamamie Rant, they are immune to its effects for 24 hours."
  - name: "Snare Master"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trap|Trap]])"
  - name: "Frequency"
    desc: "five times per day"
  - name: "Effect"
    desc: "By scrounging local materials, the castaway constructs a simple but effective deadfall without expending resources. Treat this as a snare with a DC 19 Perception check to spot, and a DC 23 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to disable. It occupies a single 5-foot square and lasts 24 hours before falling apart. The first creature that enters the space takes 6d6 bludgeoning damage"
  - name: "Sneak Attack"
    desc: "The castaway deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_NPC Core_, page 148."
```

```encounter-table
name: Castaway
creatures:
  - 1: Castaway
```
