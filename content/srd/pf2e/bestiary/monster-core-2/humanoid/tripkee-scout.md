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
languages: "Common, Tripkee"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +4, Nature +6, Stealth +7, Survival +6"
abilityMods: [1, 4, 2, 0, 3, -1]
abilities_top:
  - name: "Items"
    desc: "Dart (5), Leather Armor, Net, Sickle"
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
    desc: "⬻ sickle +9 (Agile, finesse, trip) __Damage__ 1d4+1 slashing"
  - name: "Ranged"
    desc: "⬻ dart +9 (Agile, thrown 20 feet) __Damage__ 1d4+1 piercing"
abilities_bot:
  - name: "Hurl Net"
    desc: "⬻"
  - name: "Requirements"
    desc: "The tripkee is wielding a net in two hands"
  - name: "Effect"
    desc: "The tripkee makes a ranged Strike (with a +9 attack modifier) against a Medium or smaller creature within 20 feet. On a hit, the target is off-guard and takes a –10-foot circumstance penalty to its Speeds. On a critical hit, the creature is restrained instead. The DC to Escape the net is 16. A creature adjacent to the target can Interact with the net to remove it."
  - name: "Jungle Passage"
    desc: "Tripkees ignore difficult terrain in forests and jungles."
sourcebook: "_Monster Core 2_, page 327."
```

```encounter-table
name: Tripkee Scout
creatures:
  - 1: Tripkee Scout
```
