---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Earth Diver"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/small
statblock: inline
name: "Kobold Earth Diver"
level: 4
source: "NPC Core"
aon_id: "creature-3680"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3680"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Kobold Earth Diver"
level: "Creature 4"
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, tremorsense (imprecise) 10 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Geology Lore]] +11, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [4, 3, 0, 1, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), [[srd/pf2e/compendium/equipment/adventuring-gear/map-weather-map|Map]] (depicting landmarks above and below ground in 1 square mile), Leather Armor, Pick"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +14; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet, burrow 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pick +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]]) __Damage__ 1d6+10 piercing"
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+10 slashing"
  - name: "Ranged"
    desc: "⬻ crossbow +13 (range increment 120 feet, reload 1) __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Pick Smash"
    desc: "⬺ The kobold earth diver smashes their pick into the ground, sending debris exploding in a 5-foot emanation. All creatures and unattended objects in range take 3d6 bludgeoning damage with a DC 20 basic Reflex save. A creature that is [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by an earth diver's Sinkhole takes an additional 1d6 bludgeoning damage."
  - name: "Sinkhole"
    desc: "⬺"
  - name: "Requirements"
    desc: "The earth diver is burrowed beneath a Medium or smaller creature aboveground"
  - name: "Effect"
    desc: "The earth diver creates a small sinkhole under the creature, who must attempt a DC 20 Reflex save. Regardless of the result, the target's space becomes difficult terrain."
  - name: "Failure"
    desc: "The creature falls into the sinkhole and is [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 18)."
  - name: "Critical Failure"
    desc: "As failure, and the creature takes 2d8 bludgeoning damage."
sourcebook: "_NPC Core_, page 199."
```

```encounter-table
name: Kobold Earth Diver
creatures:
  - 1: Kobold Earth Diver
```
