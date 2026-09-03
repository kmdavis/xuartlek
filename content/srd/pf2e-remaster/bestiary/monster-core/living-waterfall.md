---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Waterfall"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Living Waterfall"
level: 5
source: "Monster Core"
aon_id: "creature-2990"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2990"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Living Waterfall"
level: "Creature 5"
size: "Medium"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +12"
abilityMods: [4, 3, 3, -2, 1, 0]
abilities_top:
  - name: "Waterbound"
    desc: "When not touching water, the living waterfall is slowed 1 and can't use reactions."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +12; __Will__: +10"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ fire 5"
abilities_mid:
  - name: "Vortex"
    desc: "(aura, water) 30 feet. Water in the area that is in the same body of water as the living waterfall is difficult terrain for Swimming creatures that don't have the water trait."
speed: "20 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ wave +15 (reach 10 feet) __Damage__ 2d8+7 bludgeoning plus Push or Pull 5 feet"
abilities_bot:
  - name: "Drench"
    desc: "⬻ (Primal, Water) The elemental puts out all fires in a 5-foot emanation. It extinguishes all non-magical fires automatically and attempts to counteract magical fires (+14 counteract modifier)."
sourcebook: "_Monster Core_, page 148."
```

```encounter-table
name: Living Waterfall
creatures:
  - 1: Living Waterfall
```
