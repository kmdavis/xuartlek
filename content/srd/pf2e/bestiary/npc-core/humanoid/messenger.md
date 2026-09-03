---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Messenger"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Messenger"
level: 1
source: "NPC Core"
aon_id: "creature-3497"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3497"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Messenger"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +6, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [0, 3, 4, 0, 1, 1]
abilities_top:
  - name: "Don't Shoot the Messenger"
    desc: "Messengers get a +2 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] checks to convince another creature not to blame them for any news they deliver."
  - name: "Road Runner"
    desc: "Messengers can use [[srd/pf2e/compendium/rules-elements/skills/society|Society]] in place of [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Direction|Sense Direction]] when they're on a road."
  - name: "Items"
    desc: "Dagger, satchel of mail, Sling (10 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +10; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +8 (range increment 50 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]]) __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Express Messenger"
    desc: "Allies traveling with the messenger gain a +5-foot circumstance bonus to travel Speed, to a maximum of the messenger's travel Speed. If they use the [[srd/pf2e/compendium/rules-elements/actions/player-core#Hustle|Hustle]] activity, they can Hustle for a minimum of 1 hour instead of the usual amount."
  - name: "Special Delivery"
    desc: "⬺ The messenger Interacts to take an item of light Bulk or less held by a willing ally within reach, Strides, then delivers the item to a willing ally in reach at their new location."
sourcebook: "_NPC Core_, page 70."
```

```encounter-table
name: Messenger
creatures:
  - 1: Messenger
```
