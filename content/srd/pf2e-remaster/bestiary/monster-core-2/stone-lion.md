---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stone Lion"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Stone Lion"
level: 4
source: "Monster Core 2"
aon_id: "creature-4430"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4430"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Stone Lion"
level: "Creature 4"
size: "Large"
trait_01: "Celestial"
trait_02: "Holy"
trait_03: "Uncommon"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision"
languages: "Common, Empyrean; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +10, Intimidation +8, Meteorology Lore +11, Religion +13"
abilityMods: [4, 3, 3, 1, 5, 0]
abilities_top:
  - name: "Anchored Soul"
    desc: "The stone lion is mystically bonded to their bonded vessel and must remain within 1 mile of it. Some might be further restricted to the location they guard."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +9; __Will__: +13 +1 status to all saves vs. unholy"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ disease, paralyzed, petrified, poison"
abilities_mid:
  - name: "Bonded Vessel"
    desc: "The condition of a stone lion's vessel dictates the lion's maximum Hit Point value. Undamaged, the vessel is an object with 50 hit Points (BT 25). When the cub is in spirit form, damaging it doesn't hurt the vessel, but damaging the vessel deals an equal amount of damage to the lion. When the lion Inhabits its Vessel, they're a single target, and damage reduces the Hit Points of both the lion and the vessel. If the vessel is broken, the lion can still fight normally while inhabiting it and takes no ill effect, but if the vessel is ever destroyed, the lion is instantly slain and can't reconstitute."
  - name: "Reconstitution"
    desc: "(divine) When the lion reaches 0 Hit Points, its spirit dissipates. If its bonded vessel is intact, the lion re-forms in this vessel after 2d4 days, fully healed. If the vessel is broken, it must first be Repaired, after which the cub reforms in 3d4 days."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 2d6+7 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ stone ball +13 (range increment 30 feet) __Damage__ 2d4+7 bludgeoning"
abilities_bot:
  - name: "Inhabit Vessel"
    desc: "⬺ (Manipulate) The lion touches and melds with its bonded vessel, bringing the statue to life. It can cease Inhabiting its Vessel by Dismissing the effect. While Inhabiting the Vessel, it loses its fly Speed and gains: Immunities healing, nonlethal; but Resistances physical 5 (except bludgeoning), Speed 20 feet, and it gains the following Strikes."
  - name: "Spirit Body"
    desc: "When not Inhabiting its Vessel, the cub is incorporeal and gains resistance 5 to all damage (except force damage and damage from Strikes with the _ghost touch_ property rune; double resistance against non-magical)."
sourcebook: "_Monster Core 2_, page 183."
```

```encounter-table
name: Stone Lion
creatures:
  - 1: Stone Lion
```
