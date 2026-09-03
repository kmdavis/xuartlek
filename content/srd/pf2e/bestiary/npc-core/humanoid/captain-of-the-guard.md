---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Captain of the Guard"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Captain of the Guard"
level: 6
source: "NPC Core"
aon_id: "creature-3560"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3560"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Captain of the Guard"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +15, Diplomacy +11, Intimidation +13, Legal Lore +12, Society +10, Warfare Lore +8"
abilityMods: [5, 0, 2, 0, 3, 3]
abilities_top:
  - name: "Items"
    desc: "Crossbow (20 bolts), Dagger, Full Plate, _+1 longsword_, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +12; __Will__: +15"
hp: 95
health:
  - name: "HP"
    desc: "95"
abilities_mid:
  - name: "Aura of Command"
    desc: "(aura, emotion, mental) 30 feet. The captain of the guard bolsters lower-level guards under their command, granting them a +1 status bonus to their attack rolls and a +2 status bonus to their Will saves."
  - name: "Bravery"
    desc: "When the captain rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the frightened condition, reduce its value by 1."
  - name: "Shield Warden"
    desc: "When the captain has their shield raised, they can Shield Block when an attack is made against an adjacent ally. If they do, the shield prevents that ally from taking damage instead of the captain."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +18 (Magical, versatile P) __Damage__ 1d8+11 slashing"
  - name: "Melee"
    desc: "⬻ fist +17 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +12 (range increment 120 feet, reload 1) __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Shielded Advance"
    desc: "⬻"
  - name: "Requirements"
    desc: "The captain of the guard has their shield raised"
  - name: "Effect"
    desc: "The captain of the guard presses forward, using their shield to push back foes. The captain Strides and Shoves, in either order. The multiple attack penalty doesn't apply to this Shove, though the Shove does count toward the captain's multiple attack penalty."
sourcebook: "_NPC Core_, page 115."
```

```encounter-table
name: Captain of the Guard
creatures:
  - 1: Captain of the Guard
```
