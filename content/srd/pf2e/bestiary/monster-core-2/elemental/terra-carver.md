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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/lore|Mining Lore]] +25"
abilityMods: [8, -1, 6, 4, 0, 2]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the terra carver is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 and can't use reactions."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +19; __Will__: +23"
hp: 265
health:
  - name: "HP"
    desc: "265; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ crashing fall"
abilities_mid:
  - name: "Crashing Fall"
    desc: "Due to their size, a terra carver falls a lot harder than most creatures. When a terra carver is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] or takes falling damage, they take an additional 15 bludgeoning damage in addition to any other effect."
  - name: "Territorial Retaliation"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 15 feet uses a move action or leaves a square during a move action (move actions using only a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Fly Speed|fly Speed]] don't trigger this reaction)"
  - name: "Effect"
    desc: "The terra carver attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Trip|Trip]] the triggering creature. Regardless of the result, the space of the triggering creature and all spaces on the ground adjacent to that creature become [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] for 1 round"
speed: "20 feet; burrow 10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stone tool +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile B and S]]) __Damage__ 3d10+16 piercing plus hew stone"
  - name: "Ranged"
    desc: "⬻ rock +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet) __Damage__ 3d8+12 bludgeoning"
abilities_bot:
  - name: "Carve Projectile"
    desc: "⬺ The terra carver carves a deadly projectile from nearby materials and makes a rock ranged Strike that gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10 trait]]. On a successful hit, the target also falls [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Hew Stone"
    desc: "Melee attacks the terra carver makes with their stone tool ignore physical [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] and [[srd/pf2e/books/player-core/chapter-6-equipment/shields#Hardness|Hardness]]."
  - name: "Stone Tunnels"
    desc: "A terra carver can burrow through solid stone. When they do, they leave a tunnel."
  - name: "Wedge"
    desc: "⬺ The terra carver attempts a stone tool Strike while wedging the blow further with another tool. If it hits, the target takes an additional 3d10 damage of the same type as the Strike and is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 2 for 1 hour or until the creature is fully healed. This counts as two attacks for the terra carver's multiple attack penalty. Voiceless Miners Terra carvers are talented miners, and their tunnels are some of the longest lasting on any plane. However, the reason for these tunnels is unknown. Scholars have theorized that their tunnels function as a form of written language for the otherwise voiceless elementals. Unfortunately, attempts to map abandoned tunnels often end where another terra carver collapsed an encroaching tunnel, and mapping active tunnels often results in the cartographer never making it back."
sourcebook: "_Monster Core 2_, page 317."
```

```encounter-table
name: Terra Carver
creatures:
  - 1: Terra Carver
```
