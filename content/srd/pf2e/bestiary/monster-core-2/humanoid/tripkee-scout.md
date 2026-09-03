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
source: "Monster Core 2"
other_sources: "NPC Core"
aon_id: "creature-4589"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4589"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
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
    desc: "[[srd/pf2e/compendium/equipment/weapons/dart/dart|Dart]] (5), [[srd/pf2e/compendium/equipment/armor#Leather Armor|Leather Armor]], [[srd/pf2e/compendium/equipment/adventuring-gear/net|Net]], [[srd/pf2e/compendium/equipment/weapons/knife/sickle|Sickle]]"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +9; __Will__: +6"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet, climb 20 feet; jungle passage"
attacks:
  - name: "Melee"
    desc: "⬻ sickle +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|trip]]) __Damage__ 1d4+1 slashing"
  - name: "Ranged"
    desc: "⬻ dart +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Hurl Net"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tripkee is wielding a net in two hands"
  - name: "Effect"
    desc: "The tripkee makes a ranged Strike (with a +9 attack modifier) against a Medium or smaller creature within 20 feet. On a hit, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] and takes a –10-foot circumstance penalty to its Speeds. On a critical hit, the creature is restrained instead. The DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] the net is 16. A creature adjacent to the target can Interact with the net to remove it."
  - name: "Jungle Passage"
    desc: "Tripkees [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Ignore Difficult Terrain|ignore difficult terrain]] in forests and jungles."
sourcebook: "_Monster Core 2_, page 327."
```

```encounter-table
name: Tripkee Scout
creatures:
  - 1: Tripkee Scout
```
