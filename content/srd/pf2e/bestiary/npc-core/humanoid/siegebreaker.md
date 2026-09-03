---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Siegebreaker"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Siegebreaker"
level: 14
source: "NPC Core"
aon_id: "creature-3520"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3520"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Siegebreaker"
level: "Creature 14"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +27, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/lore|Siege Lore]] +29, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +25, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +23"
abilityMods: [2, 5, 4, 5, 2, 0]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "A siegebreaker carries 15 alchemical grenades that deal either acid, cold, or fire damage plus 10 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent damage]] and 10 [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage of the same type (typically five of each damage type). They replenish these grenades each day."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/alchemists-toolkit|Alchemist's Toolkit]], formula book, _+2 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/club/light-mace|light mace]]_, _+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]_"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +25; __Ref__: +28; __Will__: +23 Resistances [[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|alchemical]] items 10"
hp: 300
health:
  - name: "HP"
    desc: "300"
abilities_mid:
  - name: "Explosive Compounds"
    desc: "When an attacker scores a critical hit against the siegebreaker, one of the siegebreaker's alchemical grenades bursts. The GM determines the grenade randomly. The siegebreaker takes damage from the grenade as though they were hit by the grenade (applying their resistance normally), and any creature in a 10-foot emanation takes the splash damage."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _light mace_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 2d4+18 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+18 bludgeoning"
  - name: "Ranged"
    desc: "⬻ alchemical grenade +27 (range increment 60 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]]) __Damage__ 3d6 acid, cold, or fire plus 10 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent damage]] and 10 [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage of the same type"
abilities_bot:
  - name: "Expanded Splash"
    desc: "The siegebreaker's grenades deal splash damage in a 10-foot radius."
  - name: "Quick Grenadier"
    desc: "⬻ The siegebreaker Interacts to draw a grenade, then Strikes with it."
  - name: "The Wall Must Fall"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|Exploration]])"
  - name: "Requirements"
    desc: "The siegebreaker is at the base of a fortified wall"
  - name: "Effect"
    desc: "The siegebreaker has studied for years to gain exact knowledge of how to combine the alchemical ingredients in their grenades to exponentially multiply their power, creating a terrifying siege-ender bomb that can break open a city wall. The siegebreaker spends 10 minutes combining the ingredients from 9 different alchemical grenades of their choice. The siegebreaker then sets a fuse timer up to 1 minute long. When time's up, the bomb explodes in a concentrated 20-foot burst, dealing 20d6 acid, cold, or fire damage that ignores up to 10 Hardness of structures. Any creature in the area can reduce the damage they take with a DC 37 basic Reflex save."
sourcebook: "_NPC Core_, page 86."
```

```encounter-table
name: Siegebreaker
creatures:
  - 1: Siegebreaker
```
