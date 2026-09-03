---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arboreal Warden"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Arboreal Warden"
level: 4
source: "Monster Core"
aon_id: "creature-2829"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2829"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Arboreal Warden"
level: "Creature 4"
size: "Large"
trait_01: "Plant"
trait_02: "Wood"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
languages: "Arboreal, Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +13, Stealth +9"
abilityMods: [5, 1, 3, 1, 3, 1]
abilities_top:
  - name: "Items"
    desc: "large bark shield, stone longsword"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +9; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75; __Resistances__ bludgeoning 5, piercing 5; __Weaknesses__ axes 5, fire 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone longsword +13 (reach 10 feet) __Damage__ 1d8+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ shield bash +13 __Damage__ 1d6+10 bludgeoning"
abilities_bot:
  - name: "Shield Push"
    desc: "⬺ The arboreal warden Strides and then makes a shield bash Strike. If the attack hits, the target is pushed 10 feet."
sourcebook: "_Monster Core_, page 24."
```

```encounter-table
name: Arboreal Warden
creatures:
  - 1: Arboreal Warden
```
