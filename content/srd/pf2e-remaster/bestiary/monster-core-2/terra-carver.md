---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Terra Carver"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Terra Carver"
level: 13
source: "Monster Core 2"
aon_id: "creature-4577"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4577"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Terra Carver"
level: "Creature 13"
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, tremorsense (imprecise) 100 feet"
languages: "Petran; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +27, Intimidation +22, Mining Lore +25"
abilityMods: [8, -1, 6, 4, 0, 2]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the terra carver is slowed 1 and can't use reactions."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +19; __Will__: +23"
hp: 265
health:
  - name: "HP"
    desc: "265; __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ crashing fall"
abilities_mid:
  - name: "Crashing Fall"
    desc: "Due to their size, a terra carver falls a lot harder than most creatures. When a terra carver is knocked prone or takes falling damage, they take an additional 15 bludgeoning damage in addition to any other effect."
  - name: "Territorial Retaliation"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet uses a move action or leaves a square during a move action (move actions using only a fly Speed don't trigger this reaction)"
  - name: "Effect"
    desc: "The terra carver attempts an Athletics check to Trip the triggering creature. Regardless of the result, the space of the triggering creature and all spaces on the ground adjacent to that creature become difficult terrain for 1 round"
speed: "20 feet; burrow 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone tool +26 (reach 15 feet, versatile B and S) __Damage__ 3d10+16 piercing plus hew stone"
  - name: "Ranged"
    desc: "⬻ rock +24 (Propulsive, range increment 60 feet) __Damage__ 3d8+12 bludgeoning"
abilities_bot:
  - name: "Carve Projectile"
    desc: "⬺ The terra carver carves a deadly projectile from nearby materials and makes a rock ranged Strike that gains the deadly d10 trait. On a successful hit, the target also falls prone."
  - name: "Hew Stone"
    desc: "Melee attacks the terra carver makes with their stone tool ignore physical resistance and Hardness."
  - name: "Stone Tunnels"
    desc: "A terra carver can burrow through solid stone. When they do, they leave a tunnel."
  - name: "Wedge"
    desc: "⬺ The terra carver attempts a stone tool Strike while wedging the blow further with another tool. If it hits, the target takes an additional 3d10 damage of the same type as the Strike and is enfeebled 2 for 1 hour or until the creature is fully healed. This counts as two attacks for the terra carver's multiple attack penalty. Voiceless Miners Terra carvers are talented miners, and their tunnels are some of the longest lasting on any plane. However, the reason for these tunnels is unknown. Scholars have theorized that their tunnels function as a form of written language for the otherwise voiceless elementals. Unfortunately, attempts to map abandoned tunnels often end where another terra carver collapsed an encroaching tunnel, and mapping active tunnels often results in the cartographer never making it back."
sourcebook: "_Monster Core 2_, page 317."
```

```encounter-table
name: Terra Carver
creatures:
  - 1: Terra Carver
```
