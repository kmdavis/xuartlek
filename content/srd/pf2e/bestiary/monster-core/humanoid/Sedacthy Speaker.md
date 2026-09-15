---
noteType: pf2eMonster
aliases: "Sedacthy Speaker"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/sedacthy
  - pf2e/creature/trait/medium
statblock: inline
name: "Sedacthy Speaker"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3180"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sedacthy Speaker"
level: "Creature 6"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Sedacthy"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; darkvision, wavesense 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; sea speech"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +14, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +15"
abilityMods: [6, 3, 4, 2, 3, 5]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking [[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]] can be understood by any [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]] that has a swim Speed or the [[srd/pf2e/compendium/rules-elements/traits/player-core/Amphibious|amphibious]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Aquatic|aquatic]] trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently [[srd/pf2e/compendium/rules-elements/Conditions#Helpful|helpful]]."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/weapons/spear/Trident|trident]]_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +13; __Will__: +15"
hp: 95
health:
  - name: "HP"
    desc: "95"
abilities_mid:
  - name: "Speaker's Privilege"
    desc: "⬲"
  - name: "Trigger"
    desc: "The sedacthy speaker takes damage"
  - name: "Requirements"
    desc: "The sedacthy speaker has cover from an [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]] ally"
  - name: "Effect"
    desc: "The animal takes the damage instead."
speed: "20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _trident_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d8+10 piercing"
  - name: "Melee"
    desc: "⬻ jaws +16 __Damage__ 1d6+8 piercing plus 1d4 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d6+8 slashing"
  - name: "Ranged"
    desc: "⬻ _trident_ +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]]) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "Animal Shield"
    desc: "⬻"
  - name: "Requirements"
    desc: "The sedacthy speaker is adjacent to a Large or larger [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]] ally"
  - name: "Effect"
    desc: "The speaker gains cover until the start of their next turn or when they're no longer adjacent to the animal, whichever comes first."
  - name: "Exploit Weakness"
    desc: "The speaker's Strikes deal 1d6 additional damage to creatures that are [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] or [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]]."
  - name: "Painful Cry"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]]) The sedacthy shrieks across a range of painfully high tones, dealing 3d6 sonic damage and 1d6 mental damage to all creatures in a 30-foot cone, with a DC 23 basic Fortitude save. A creature that fails its save is [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 1]]."
  - name: "Shared Feast"
    desc: "⬺ The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
  - name: "Swim Together"
    desc: "⬺"
  - name: "Requirements"
    desc: "The speaker is adjacent to an [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animal]] ally"
  - name: "Effect"
    desc: "The speaker and the animal both [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]], ending their movement adjacent to one another."
sourcebook: "_Monster Core_, page 301."
```

```encounter-table
name: Sedacthy Speaker
creatures:
  - 1: Sedacthy Speaker
```
