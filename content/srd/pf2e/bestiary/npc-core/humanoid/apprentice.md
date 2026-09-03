---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Apprentice"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Apprentice"
level: -1
source: "NPC Core"
aon_id: "creature-3411"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3411"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Apprentice"
level: "Creature -1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 2
perception:
  - name: "Perception"
    desc: "Perception +2"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +3, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +5, [[srd/pf2e/compendium/rules-elements/skills/lore|Geography Lore]] +5"
abilityMods: [1, 2, 1, 3, 0, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]], [[srd/pf2e/compendium/equipment/adventuring-gear/map-weather-map|assorted maps]], Dagger, rugged clothes with tool belt (functions as [[srd/pf2e/compendium/equipment/armor#Padded Armor|padded armor]])"
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +6; __Will__: +2"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
  - name: "Melee"
    desc: "⬻ fist +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +4 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Apprentice's Ambition"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "A direct superior is supervising the apprentice"
  - name: "Effect"
    desc: "The apprentice gains a +2 circumstance bonus to attack rolls, damage rolls, saving throws, and skill checks until the end of their next turn."
sourcebook: "_NPC Core_, page 8."
```

```encounter-table
name: Apprentice
creatures:
  - 1: Apprentice
```
