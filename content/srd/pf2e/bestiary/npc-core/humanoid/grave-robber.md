---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grave Robber"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Grave Robber"
level: 1
source: "NPC Core"
aon_id: "creature-3424"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3424"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Grave Robber"
level: "Creature 1"
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
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +6, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +2, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +2, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Underworld Lore]] +6"
abilityMods: [1, 2, 2, 3, 2, -1]
abilities_top:
  - name: "Items"
    desc: "embalming flask, Holy Water, shovel"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +7; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shovel +6 __Damage__ 1d6+1 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ embalming flask +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|Alchemical]], range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]]) __Damage__ 1d4 acid plus 1 acid splash damage and alchemical embalming"
abilities_bot:
  - name: "Alchemical Embalming"
    desc: "The grave robber carries alchemical vials of specially prepared embalming fluid meant to hinder pursuit by anyone who interrupts their grave-robbing. A creature hit by a grave robber's embalming flask takes a –10-foot penalty to all its Speeds for 1 round. On a critical hit from an embalming flask, the target is also [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] for 1 minute."
sourcebook: "_NPC Core_, page 18."
```

```encounter-table
name: Grave Robber
creatures:
  - 1: Grave Robber
```
