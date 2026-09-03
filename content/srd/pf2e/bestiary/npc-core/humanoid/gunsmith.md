---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gunsmith"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gunsmith"
level: 1
source: "NPC Core"
aon_id: "creature-3456"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3456"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gunsmith"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +13, [[srd/pf2e/compendium/rules-elements/skills/lore|Firearm Lore]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +5"
abilityMods: [1, 3, 0, 2, 3, 0]
abilities_top:
  - name: "Firearm Specialist"
    desc: "For encounters involving the crafting or maintenance of firearms, the gunsmith is a 6th-level challenge."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]] (gunsmithing), [[srd/pf2e/compendium/equipment/weapons/firearm/dueling-pistol|Dueling Pistol]] (2, 20 rounds)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +8; __Will__: +6"
hp: 16
health:
  - name: "HP"
    desc: "16"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dueling pistol +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/concealable|Concealable]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], range increment 60 feet, reload 1) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Crafty Reload"
    desc: "The gunsmith can Interact to reload a firearm without a free hand if they have a firearm in each hand. In addition, each time the gunsmith reloads a firearm, they can attempt a [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] check against the hard DC for the firearm's level (DC 17 for a [[srd/pf2e/compendium/equipment/weapons/firearm/dueling-pistol-weapon-520|dueling pistol]]). On a success, they gain a +1 circumstance bonus on the next attack roll they make with that firearm before the start of their next turn."
  - name: "Firearm Sabotage"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]])"
  - name: "Requirements"
    desc: "The gunsmith is wielding or holding a one-handed firearm and has a free hand"
  - name: "Effect"
    desc: "The gunsmith deftly makes a minor modification to a firearm that can be detected with a Perception check opposed by the gunsmith's [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] DC. If the sabotage is not reversed with a successful Crafting check against the gunsmith's Crafting DC, the firearm automatically misfires the next time it is used (the flat check is an automatic failure; see the Misfires sidebar)."
sourcebook: "_NPC Core_, page 42."
```

```encounter-table
name: Gunsmith
creatures:
  - 1: Gunsmith
```
