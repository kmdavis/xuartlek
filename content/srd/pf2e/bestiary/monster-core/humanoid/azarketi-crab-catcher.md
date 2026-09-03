---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Azarketi Crab Catcher"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/azarketi
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Azarketi Crab Catcher"
level: 0
source: "Monster Core"
aon_id: "creature-2838"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2838"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Azarketi Crab Catcher"
level: "Creature 0"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Azarketi"
trait_03: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6"
languages: "Alghollthu, Common"
skills:
  - name: "Skills"
    desc: "Athletics +4, Diplomacy +3, Nature +3, Stealth +5, Survival +5, Underwater Lore +4"
abilityMods: [2, 3, 2, 0, 1, 1]
abilities_top:
  - name: "Items"
    desc: "crab cage, Dagger, Sack"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +9; __Will__: +3"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Hydration"
    desc: "Azarketi must regularly submerge themselves in water to rehydrate their water-acclimated skin. After the first 24 hours outside of water, they gain a –1 status penalty to Fortitude saves as their skin cracks and their gills become painful. After 48 hours, they begin to suffocate until returned to water."
  - name: "Swim Away"
    desc: "⬲"
  - name: "Requirement"
    desc: "The azarketi crab catcher is swimming"
  - name: "Trigger"
    desc: "The azarketi crab catcher is targeted with an attack and can see the attacker"
  - name: "Effect"
    desc: "The azarketi crab catcher gains a +2 circumstance bonus to AC against the triggering attack. After the attack, they Swim 5 feet."
speed: "25 feet; swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +7 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+2 piercing"
sourcebook: "_Monster Core_, page 31."
```

```encounter-table
name: Azarketi Crab Catcher
creatures:
  - 1: Azarketi Crab Catcher
```
