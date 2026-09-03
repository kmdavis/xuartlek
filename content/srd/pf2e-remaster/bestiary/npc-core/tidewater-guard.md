---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tidewater Guard"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/lizardfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Tidewater Guard"
level: 4
source: "NPC Core"
aon_id: "creature-3660"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3660"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tidewater Guard"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "Common, Iruxi"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +12, Nature +10, Stealth +11, Survival +10"
abilityMods: [4, 3, 1, -1, 2, 0]
abilities_top:
  - name: "Deep Breath"
    desc: "A tidewater guard can hold their breath for 20 minutes."
  - name: "Tethered Tridents"
    desc: "The tidewater guard's tridents are specially prepared to be aquadynamic and tethered by ropes. They have the tethered trait, meaning that a wielder who has a free hand can Interact to pull the weapon back into their grasp after they have thrown it as a ranged attack or after it has been disarmed (unless it is being held by another creature)."
  - name: "Items"
    desc: "Studded Leather Armor, trident with 50 feet of line (2)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +11; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trident +14 (Tethered) __Damage__ 1d8+7 piercing"
  - name: "Melee"
    desc: "⬻ claw +14 (Agile) __Damage__ 1d6+7 piercing"
  - name: "Ranged"
    desc: "⬻ trident +13 (Tethered, thrown 20 feet) __Damage__ 1d8+7 piercing"
abilities_bot:
  - name: "Reel In"
    desc: "⬺ The tidewater guard makes a ranged Strike with their trident. If the Strike hits, the guard can haul on the attached line, moving the target up to 30 feet in a straight line toward the iruxi."
  - name: "Terrain Advantage"
    desc: "Non-lizardfolk creatures that are in difficult terrain or are in water and lack a swim Speed are off-guard to the tidewater guard."
sourcebook: "_NPC Core_, page 204."
```

```encounter-table
name: Tidewater Guard
creatures:
  - 1: Tidewater Guard
```
