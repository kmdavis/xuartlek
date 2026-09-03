---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mage Knight"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mage Knight"
level: 10
source: "NPC Core"
aon_id: "creature-3531"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3531"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mage Knight"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Arcana +22, Athletics +21, Warfare Lore +20"
abilityMods: [5, 1, 2, 4, 3, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 full plate_, _+1 striking mace_, spellbook, Steel Shield (Hardness 5, HP 20, BT 10)"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +18; __Ref__: +13 (+16 against damaging effects); __Will__: +21"
hp: 140
health:
  - name: "HP"
    desc: "140"
abilities_mid:
  - name: "Shield Block"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _mace_ +22 (Magical, Shove) __Damage__ 2d6+11 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +21 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+11 bludgeoning"
abilities_bot:
  - name: "Wizard School Spells"
    desc: "DC 28, 2 Focus Points - __5th__ Energy Absorption, Force Bolt"
  - name: "Bespell Strikes"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per turn"
  - name: "Requirements"
    desc: "The mage knight's most recent action was to cast a non-cantrip spell"
  - name: "Effect"
    desc: "The mage knight siphons spell energy into one weapon they're wielding, or into one of their unarmed attacks. Until the end of the turn, the weapon or unarmed attack deals an extra 2d6 force damage and gains the arcane trait if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead."
  - name: "Drain Bonded Item"
    desc: "⭓ (Arcane)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The mage knight hasn't acted yet on this turn"
  - name: "Effect"
    desc: "The mage knight expends the power stored in their bonded item (typically their shield). This gives them the ability to cast one prepared spell they prepared today and already cast, without spending a slot."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 28, attack +20 - __Cantrips (5th)__ Detect Magic, Electric Arc, Frostbite, Light, Read Aura, Telekinetic Hand, Telekinetic Projectile - __1st__ Enfeeble, Fleet Step, Sure Strike - __2nd__ Invisibility (×2), Mist - __3rd__ Earthbind, Vampiric Feast, Wall of Thorns - __4th__ Fireball, Fly, Weapon Storm - __5th__ Force Barrage, Impaling Spike, Toxic Cloud"
sourcebook: "_NPC Core_, page 94."
```

```encounter-table
name: Mage Knight
creatures:
  - 1: Mage Knight
```
