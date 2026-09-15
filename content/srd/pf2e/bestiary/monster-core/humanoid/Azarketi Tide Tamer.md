---
noteType: pf2eMonster
aliases: "Azarketi Tide Tamer"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/azarketi
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Azarketi Tide Tamer"
level: 7
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2839"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Azarketi Tide Tamer"
level: "Creature 7"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Azarketi"
trait_03: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15"
languages: "Alghollthu, [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +12, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +14, Underwater Lore +11"
abilityMods: [4, 4, 2, 0, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Hand Crossbow (20 bolts), studded leather, _+1 [[srd/pf2e/compendium/equipment/weapons/spear/Trident|trident]]_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +18; __Will__: +12"
hp: 115
health:
  - name: "HP"
    desc: "115"
abilities_mid:
  - name: "Hydration"
    desc: "Azarketi must regularly submerge themselves in water to rehydrate their water-acclimated skin. After the first 24 hours outside of water, they gain a –1 status penalty to Fortitude saves as their skin cracks and their gills become painful. After 48 hours, they begin to suffocate until returned to water."
  - name: "Speaker of the Oceans"
    desc: "An azarketi tide tamer can speak with [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animals]] that have the [[srd/pf2e/compendium/rules-elements/traits/player-core/Aquatic|aquatic]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Amphibious|amphibious]] trait."
speed: "25 feet; swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trident +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d8+7 piercing"
  - name: "Ranged"
    desc: "⬻ trident +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d8+7 piercing"
  - name: "Ranged"
    desc: "⬻ hand crossbow +17 (range increment 60 feet, reload 1) __Damage__ 1d6 piercing"
abilities_bot:
  - name: "Aquatic Predator"
    desc: "An azarketi deals 2d8 additional damage on a successful weapon Strike while they are underwater."
sourcebook: "_Monster Core_, page 31."
```

```encounter-table
name: Azarketi Tide Tamer
creatures:
  - 1: Azarketi Tide Tamer
```
