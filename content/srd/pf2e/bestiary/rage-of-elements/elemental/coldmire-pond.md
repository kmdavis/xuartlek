---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Coldmire Pond"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Coldmire Pond"
level: 8
source: "Rage of Elements"
aon_id: "creature-2660"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2660"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Coldmire Pond"
level: "Creature 8"
size: "Huge"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18"
abilityMods: [5, 3, 5, 2, 2, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +13"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Shallow Waters"
    desc: "The coldmire pond can occupy the same space as other creatures. Creatures who move through the coldmire pond treat it as difficult terrain. Two creatures both occupying the coldmire pond's space are flanking it, regardless of their actual positions within the coldmire pond."
speed: "20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ clammy pseudopod +20 __Damage__ 2d8+9 bludgeoning and Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d6 bludgeoning plus 1d6 cold, DC 25"
  - name: "Drag Below"
    desc: "⬺"
  - name: "Requirements"
    desc: "The coldmire pond occupies the same space as a target it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The coldmire pond pulls the target below the surface. The target must succeed at a DC 26 Reflex save or fall [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] and begin drowning."
  - name: "Flash Flood"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]]) Water surges out of the coldmire pond in a 20-foot emanation and crashes into nearby creatures, knocking them off their feet. Creatures in the area, as well as any creatures currently sharing the coldmire pond's space, take 4d8 bludgeoning damage and are knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] (DC 26 basic Reflex save). Creatures standing inside the coldmire pond treat their result as one step worse."
sourcebook: "_Rage of Elements_, page 180."
```

```encounter-table
name: Coldmire Pond
creatures:
  - 1: Coldmire Pond
```
