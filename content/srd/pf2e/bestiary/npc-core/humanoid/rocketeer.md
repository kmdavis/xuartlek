---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Rocketeer"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Rocketeer"
level: 6
source: "NPC Core"
aon_id: "creature-3463"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3463"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Rocketeer"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +14, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +12"
abilityMods: [2, 4, 2, 2, 2, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]] (rocketry), flight suit (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), heavy wrench (functions as a [[srd/pf2e/compendium/equipment/weapons/club/mace|mace]]), moderate alchemist's fire (4), _+1 slide pistol_ (20 rounds)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +16; __Will__: +14"
hp: 85
health:
  - name: "HP"
    desc: "85"
abilities_mid:
  - name: "Fuel Tank Vulnerability"
    desc: "When the rocketeer is struck by a critical hit that deals piercing or fire damage, they must attempt a DC 5 flat check. On a failure, the rocketeer's fuel tank explodes, dealing 6d6 fire damage to the rocketeer and all creatures in a 20-foot emanation and knocking the rocketeer [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. The rocketeer loses their fly Speed and can't use Explosive Liftoff, Mid-air Collision, or Rocketing Strafe until they repair their jet pack, which requires an appropriate set of artisan's tools and takes 2 hours."
speed: "25 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ heavy wrench +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d6+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _slide pistol_ +17 ([[srd/pf2e/compendium/rules-elements/traits/gm-core/city|capacity 5]], [[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], range increment 30 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Explosive Liftoff"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Requirements"
    desc: "The rocketeer is standing on a horizontal surface"
  - name: "Effect"
    desc: "The rocketeer unleashes the full strength of their jets to launch themself into the air, dealing 7d6 fire and bludgeoning damage to all creatures in a 15-foot emanation with a DC 24 basic Reflex save. The rocketeer [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] twice, straight up into the air."
  - name: "Mid-air Collision"
    desc: "⬺ The rocketeer [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] twice, then attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]] another flying creature. If they roll a success on the [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check, they get a critical success instead."
  - name: "Rocketing Strafe"
    desc: "⬺ The rocketeer [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] and makes two melee Strikes at any point during that movement. Each Strike must target a different creature. The rocketeer can forgo the melee Strikes to instead make one slide pistol Strike at any point during that movement and Interact to select the next loaded chamber of their slide pistol; they can do these in either order. Any Strike made as part of a Rocketing Strafe deals an additional 2d6 damage and takes the normal multiple attack penalty."
sourcebook: "_NPC Core_, page 47."
```

```encounter-table
name: Rocketeer
creatures:
  - 1: Rocketeer
```
