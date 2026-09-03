---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zealot of Asmodeus"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Zealot of Asmodeus"
level: 4
source: "NPC Core"
aon_id: "creature-3444"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3444"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Zealot of Asmodeus"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +9, Deception +10, Intimidation +10, Religion +12, Society +7"
abilityMods: [4, 1, 1, 0, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Half Plate, Mace, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +7; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
  - name: "Swear Vengeance"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature the zealot can see damages a follower of Asmodeus other than the zealot"
  - name: "Effect"
    desc: "The zealot is affected by a _sure strike_ spell. If the zealot makes an attack roll against anyone other than the triggering creature, the _sure strike_ ends with no effect."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mace +12 (Shove) __Damage__ 1d8+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +9 (deadly 1d10, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Channel Smite"
    desc: "⬺ (Divine)"
  - name: "Cost"
    desc: "the zealot expends a _harm_ spell"
  - name: "Effect"
    desc: "The zealot makes a melee Strike. If it hits, they damage the target with a 1-action _harm_ spell. The target automatically gets a failure (or a critical failure if the Strike was a critical hit). The spell doesn't have the manipulate trait when cast this way."
  - name: "Deadly Simplicity"
    desc: "The zealot deals 1d8 damage with their mace instead of 1d6."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 19, attack +11 - __Cantrips (2nd)__ Detect Magic, Divine Lance, Forbidding Ward, Read Aura, Sigil - __1st__ Command, Runic Weapon, Spirit Link - __2nd__ Cleanse Affliction, Harm (×4), See the Unseen, Share Life"
sourcebook: "_NPC Core_, page 31."
```

```encounter-table
name: Zealot of Asmodeus
creatures:
  - 1: Zealot of Asmodeus
```
