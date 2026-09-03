---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Musketeer"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Musketeer"
level: 3
source: "NPC Core"
aon_id: "creature-3507"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3507"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Musketeer"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +8, Deception +8, Intimidation +10, Stealth +11, Thievery +9"
abilityMods: [1, 4, 1, 0, 1, 3]
abilities_top:
  - name: "Items"
    desc: "Flintlock Musket (10 rounds), Leather Armor, Rapier"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +11; __Will__: +6"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +11 (deadly d8, Disarm, Finesse) __Damage__ 1d6+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ flintlock musket +11 (Concussive, fatal d10, range increment 70 feet, reload 1) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Musketeer's Advance"
    desc: "⬺"
  - name: "Requirements"
    desc: "The musketeer is wielding a flintlock musket"
  - name: "Effect"
    desc: "The musketeer makes a flintlock musket Strike. If the Strike hits, the target is off-guard to melee attacks by the musketeer until the end of the musketeer's next turn. Regardless of whether the Strike hit, the musketeer then Interacts to swap their flintlock musket for their rapier and Strides toward the creature they attacked."
  - name: "One for All"
    desc: "⬻"
  - name: "Requirements"
    desc: "The musketeer is wielding a single one-handed weapon in one hand and has their other hand free"
  - name: "Effect"
    desc: "The musketeer grants a +1 circumstance bonus to AC to themself until the start of their next turn. Allies also gain this bonus while adjacent to the musketeer. If a creature would benefit from more than one creature's One for All ability, the bonus is +2 instead of +1."
  - name: "Sneak Attack"
    desc: "The musketeer deals an extra 1d6 precision damage to off-guard creatures."
sourcebook: "_NPC Core_, page 77."
```

```encounter-table
name: Musketeer
creatures:
  - 1: Musketeer
```
