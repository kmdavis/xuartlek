---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warden"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Warden"
level: 6
source: "NPC Core"
aon_id: "creature-3562"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3562"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Warden"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +15, Nature +11, Stealth +13, Survival +13"
abilityMods: [4, 2, 3, 1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "Backpack, Bastard Sword, Bedroll, Compass, _+1 composite longbow_ (10 arrows), Flint and Steel, maps, pup tent, Scale Mail"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +15; __Will__: +11"
hp: 100
health:
  - name: "HP"
    desc: "100"
abilities_mid:
  - name: "Warding Strike"
    desc: "⬲"
  - name: "Trigger"
    desc: "One of the warden's enemies within 100 feet attacks one of the warden's allies or a person the warden is sworn to protect"
  - name: "Effect"
    desc: "The warden Strikes the triggering enemy. If the Strike hits, the enemy's attack is deflected, reducing its damage by 8, or by 16 if the warden's Strike was a critical hit."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bastard sword +16 (two-hand d12) __Damage__ 1d8+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +17 (deadly d10, Magical, Propulsive, range increment 100 feet, reload 0, volley 30 feet) __Damage__ 1d8+8 piercing"
abilities_bot:
  - name: "Warden's Protection"
    desc: "A warden deals an extra 1d8 damage to any creature trespassing on the territory the warden protects."
sourcebook: "_NPC Core_, page 117."
```

```encounter-table
name: Warden
creatures:
  - 1: Warden
```
