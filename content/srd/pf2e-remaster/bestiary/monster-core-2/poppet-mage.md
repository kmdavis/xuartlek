---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Poppet Mage"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/small
statblock: inline
name: "Poppet Mage"
level: 2
source: "Monster Core 2"
aon_id: "creature-4515"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4515"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Poppet Mage"
level: "Creature 2"
size: "Small"
trait_01: "Construct"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Common; two languages their creator speaks"
skills:
  - name: "Skills"
    desc: "Arcana +8, Crafting +8, Diplomacy +6, Occultism +8"
abilityMods: [1, 1, 0, 4, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Hand Crossbow (10 bolts), spellbook containing their prepared spells, Staff"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +5; __Will__: +11"
hp: 30
health:
  - name: "HP"
    desc: "30; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Weaknesses__ fire 3"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +9 (two-hand 1d8) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +9 (range increment 60 feet) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "Magic Hat"
    desc: "⬺ (Concentrate, Manipulate)"
  - name: "Frequency"
    desc: "one per day"
  - name: "Requirements"
    desc: "The poppet mage has a free hand"
  - name: "Effect"
    desc: "The poppet mage pulls off their hat, and with a jaunty display, pulls one of the following items from their hat: a lesser glue bomb, a lesser smoke ball, or a _minor healing potion_. This consumable lasts for 1 hour before becoming inert."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ Daze, Figment, Prestidigitation, Shield, Telekinetic Projectile - __1st__ Dizzying Colors, Mending, Sleep"
sourcebook: "_Monster Core 2_, page 256."
```

```encounter-table
name: Poppet Mage
creatures:
  - 1: Poppet Mage
```
