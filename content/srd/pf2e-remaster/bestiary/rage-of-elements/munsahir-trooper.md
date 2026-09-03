---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Munsahir Trooper"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Munsahir Trooper"
level: 5
source: "Rage of Elements"
aon_id: "creature-2638"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2638"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Munsahir Trooper"
level: "Creature 5"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Common, Pyric"
skills:
  - name: "Skills"
    desc: "Athletics +12, Crafting +11, Plane of Fire Lore +11, Stealth +12"
abilityMods: [3, 1, 5, 2, 3, 1]
abilities_top:
  - name: "Items"
    desc: "breastplate, dueling pistol (20 rounds), warhammer"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +14; __Ref__: +10; __Will__: +10"
hp: 85
health:
  - name: "HP"
    desc: "85; __Immunities__ fire; __Weaknesses__ cold 5"
abilities_mid:
  - name: "Heat of the Forge"
    desc: "(aura, fire) 10 feet. An munsahir's skin radiates heat like a forge's fire. A creature that starts its turn in the area must succeed at a DC 20 Fortitude save or become fatigued while it remains in the area. Creatures immune to environmental heat effects or with any fire resistance are immune."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +14 (Shove) __Damage__ 1d8+9 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ dueling pistol +12 (Concealable, Concussive, fatal d10, range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing plus 1d6 fire"
abilities_bot:
  - name: "Burning Touch"
    desc: "(Fire, Primal) The munsahir gatecrasher's Strikes deal an extra 1d6 fire damage (included above). When the gatecrasher successfully performs a Grapple or Shove action, they also deal 1d6 fire damage to their target."
  - name: "Volcanic Hammer"
    desc: "⬺ The trooper makes a warhammer Strike that deals one extra weapon die of damage and 2d6 persistent fire damage."
sourcebook: "_Rage of Elements_, page 131."
```

```encounter-table
name: Munsahir Trooper
creatures:
  - 1: Munsahir Trooper
```
