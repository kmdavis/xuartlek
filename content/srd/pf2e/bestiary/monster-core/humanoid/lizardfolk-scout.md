---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lizardfolk Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/lizardfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Lizardfolk Scout"
level: 1
source: "Monster Core"
aon_id: "creature-3091"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3091"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lizardfolk Scout"
level: "Creature 1"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], Iruxi"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +4, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [2, 3, 1, -1, 3, 1]
abilities_top:
  - name: "Deep Breath"
    desc: "A lizardfolk scout can hold their breath for 15 minutes."
  - name: "Items"
    desc: "Blowgun (10 darts), 1 of which is coated with [[srd/pf2e/compendium/equipment/alchemical-items/giant-centipede-venom|giant centipede venom]])"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +8; __Will__: +6"
hp: 17
health:
  - name: "HP"
    desc: "17"
speed: "25 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ tail +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ blowgun +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], range increment 20 feet, reload 1) __Damage__ 1 piercing plus giant centipede venom"
abilities_bot:
  - name: "Giant Centipede Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 14 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d4 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d4 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] (1 round)"
  - name: "Stage 3"
    desc: "1d4 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], and [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] (1 round)"
  - name: "Hidden Movement"
    desc: "If the lizardfolk scout starts its turn [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] from or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] by a creature, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the scout's attacks until the end of the turn."
  - name: "Sneak Attack"
    desc: "The lizardfolk scout deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures. __Terrain Advantage Non-[[srd/pf2e/compendium/gm/creature-families/lizardfolk|lizardfolk]] creatures that are in difficult terrain or are in water and lack a swim Speed are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the lizardfolk scout.__"
sourcebook: "_Monster Core_, page 227."
```

```encounter-table
name: Lizardfolk Scout
creatures:
  - 1: Lizardfolk Scout
```
