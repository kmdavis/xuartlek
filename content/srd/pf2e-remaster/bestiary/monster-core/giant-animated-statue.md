---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Animated Statue"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/huge
statblock: inline
name: "Giant Animated Statue"
level: 7
source: "Monster Core"
aon_id: "creature-2821"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2821"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Animated Statue"
level: "Creature 7"
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +17"
abilityMods: [6, -1, 6, -5, 0, -5]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +17; __Ref__: +10; __Will__: +9 construct armor"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Hardness__ 10"
abilities_mid:
  - name: "Construct Armor"
    desc: "Like normal objects, an animated statue has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. Once an animated statue is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 22."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone fist +19 (Magical) __Damage__ 2d12+6 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ flaming coal +12 (Fire, Magical, range increment 80 feet) __Damage__ 2d6+6 bludgeoning and 2d8 fire"
abilities_bot:
  - name: "Brazier"
    desc: "The statue carries a wide brazier full of hot coals. To make flaming coal Strikes or use Burn Alive, the statue must have the brazier held in one hand or otherwise within reach. Instead of targeting the statue with an attack, a creature can target the brazier directly. The brazier has the same AC and saves as the statue. Dealing 15 cold damage to the brazier or dousing it with at least 2 gallons of water extinguishes the coals. This prevents the statue from using Burn Alive and causes its ranged attacks to no longer deal fire damage."
  - name: "Burn Alive"
    desc: "⬻ (Fire) The statue grinds a creature it has grabbed or restrained into the red-hot coals of its brazier. The target takes 3d8 fire damage and 1d8 persistent fire damage."
sourcebook: "_Monster Core_, page 19."
```

```encounter-table
name: Giant Animated Statue
creatures:
  - 1: Giant Animated Statue
```
