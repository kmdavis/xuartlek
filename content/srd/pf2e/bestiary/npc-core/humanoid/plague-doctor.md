---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Plague Doctor"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Plague Doctor"
level: 5
source: "NPC Core"
aon_id: "creature-3484"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3484"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Plague Doctor"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Intimidation +9, Medicine +13, Plague Lore +13, Religion +13"
abilityMods: [0, 1, 4, 2, 4, 2]
abilities_top:
  - name: "Items"
    desc: "Crossbow (10 bolts), Healer's Toolkit, _minor potion of healing_ (4), Staff, studded leather"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +8; __Will__: +13 +2 circumstance to all saves vs. disease"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 (two-hand d8) __Damage__ 1d4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +10 (range increment 120 feet, reload 1) __Damage__ 1d8 piercing"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 23, 1 Focus Point - __3rd__ Healer's Blessing"
  - name: "Healing Hands"
    desc: "When the plague doctor casts _heal_, they roll d10s instead of d8s."
  - name: "Improved Communal Healing"
    desc: "When the plague doctor casts _heal_ targeting a single creature, the plague doctor also restores Hit Points equal to the spell's level to themself or any other creature within range of the spell."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 23 - __Cantrips (3rd)__ Guidance, Light, Message, Sigil, Stabilize - __1st__ Detect Poison, Cleanse Cuisine (×2) - __2nd__ Clear Mind (×2), Peaceful Rest - __3rd__ Cleanse Affliction (×2), Heal (×3)"
sourcebook: "_NPC Core_, page 62."
```

```encounter-table
name: Plague Doctor
creatures:
  - 1: Plague Doctor
```
