---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mist Stalker"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Mist Stalker"
level: 4
source: "Monster Core 2"
aon_id: "creature-4391"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4391"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mist Stalker"
level: "Creature 4"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Elemental"
trait_03: "Water"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, mist vision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +10, Stealth +12"
abilityMods: [4, 4, 2, 1, 5, 0]
abilities_top:
  - name: "Mist Cloud"
    desc: "(aura, primal, water) 15 feet. The mist stalker is surrounded by mist. Creatures in the aura are concealed. If wind disperses the aura, it returns automatically at the start of the mist stalker's turn. This cloud is suppressed in water."
  - name: "Mist Vision"
    desc: "The mist stalker ignores the concealed condition from mist and fog."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +12; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ bleed, paralyzed, poison, sleep"
speed: "20 feet, climb 20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +14 (Finesse, sweep, reach 10 feet) __Damage__ 2d8+4 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d8+4 bludgeoning, DC 21"
  - name: "Solidify Mist"
    desc: "⬻ (Primal, water) The mist stalker makes its mist cloud congeal, causing the aura to be difficult terrain until the start of the mist stalker's next turn. In addition, the mist stalker can make the mist even thicker around a single Medium or smaller creature within the cloud. The creature must succeed at a DC 20 Reflex save or become immobilized until it Escapes or is no longer in the mist cloud's emanation."
sourcebook: "_Monster Core 2_, page 150."
```

```encounter-table
name: Mist Stalker
creatures:
  - 1: Mist Stalker
```
