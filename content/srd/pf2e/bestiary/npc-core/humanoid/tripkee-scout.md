---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tripkee Scout"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Scout"
level: 1
source: "NPC Core"
other_sources: "Monster Core 2"
aon_id: "creature-3673"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3673"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tripkee Scout"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Tripkee|Tripkee]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [1, 4, 2, 0, 3, -1]
abilities_top:
  - name: "Items"
    desc: "Dart (5), Hand Adze, Leather Armor, Net"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +6"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet, climb 20 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ hand adze +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d4+1 slashing"
  - name: "Melee"
    desc: "⬻ fist +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 1d4+1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ hand adze +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]]) __Damage__ 1d4+1 slashing"
abilities_bot:
  - name: "Hurl Net"
    desc: "⬻"
  - name: "Requirements"
    desc: "The scout is wielding a net in two hands"
  - name: "Effect"
    desc: "The scout makes a ranged Strike (with a +9 modifier) against a Medium or smaller creature within 20 feet. On a hit, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] and takes a –10-foot circumstance penalty to its Speeds. On a critical hit, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] instead. The DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] the net is 16. A creature adjacent to the target can Interact with the net to remove it."
  - name: "Forest Passage"
    desc: "The scout ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 214."
```

```encounter-table
name: Tripkee Scout
creatures:
  - 1: Tripkee Scout
```
