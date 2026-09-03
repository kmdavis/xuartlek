---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Watch Officer"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Watch Officer"
level: 3
source: "NPC Core"
aon_id: "creature-3556"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3556"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Watch Officer"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; (9 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +11, Diplomacy +6, Intimidation +9, Legal Lore +7, Society +5"
abilityMods: [4, 1, 3, 0, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Crossbow (20 bolts), Dagger, Signal Whistle, Steel Shield (Hardness 5, HP 20, BT 10), warhammer"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +6; __Will__: +8"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Air of Authority"
    desc: "(aura, emotion, mental) 10 feet. Creatures in the aura who are the same or lower level than the watch officer take a –2 status penalty to their Will DC against the watch officer's attempts to Coerce or Demoralize them."
  - name: "Bravery"
    desc: "When the watch officer rolls a success on a Will save against a fear effect, they get a critical success instead. In addition, any time they gain the frightened condition, reduce its value by 1."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +13 (Shove) __Damage__ 1d8+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +13 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8+3 piercing"
abilities_bot:
  - name: "Sudden Charge"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The watch officer Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against that enemy."
sourcebook: "_NPC Core_, page 113."
```

```encounter-table
name: Watch Officer
creatures:
  - 1: Watch Officer
```
