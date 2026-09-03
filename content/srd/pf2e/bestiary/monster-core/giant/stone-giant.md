---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stone Giant"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Stone Giant"
level: 8
source: "Monster Core"
aon_id: "creature-3012"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3012"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Stone Giant"
level: "Creature 8"
size: "Large"
trait_01: "Earth"
trait_02: "Giant"
trait_03: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Common, Jotun, Petran"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +20, Intimidation +14, Nature +18, Stealth +14"
abilityMods: [6, 2, 4, 0, 4, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 striking greatclub_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +14; __Will__: +14"
hp: 150
health:
  - name: "HP"
    desc: "150"
abilities_mid:
  - name: "Swat Projectile"
    desc: "⬲"
  - name: "Requirements"
    desc: "The stone giant must have a free hand but can Release anything as part of this reaction"
  - name: "Trigger"
    desc: "The giant is targeted by a physical ranged attack"
  - name: "Effect"
    desc: "The stone giant gains a +4 circumstance bonus to AC against the triggering attack. If the attack misses and the projectile was made of stone, the giant can throw it back at the attacker as a rock ranged Strike."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatclub_ +21 (Backswing, Magical, reach 10 feet, Shove) __Damage__ 2d10+12 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, reach 10 feet) __Damage__ 2d6+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +18 (Brutal, range increment 120 feet) __Damage__ 2d6+12 bludgeoning"
abilities_bot:
  - name: "Big Swing"
    desc: "⬺ The stone giant makes a greatclub Strike. The target is Pushed up to 10 feet on a hit or up to 20 feet on a critical hit. If the target collides with a solid object, it takes bludgeoning damage as though it had fallen the distance it moved."
  - name: "Create Boulder"
    desc: "⬻ (Earth, Primal) The stone giant molds a boulder from primal earth and throws it as a rock Strike. A creature hit by the Strike must succeed at a DC 26 Reflex save or be knocked prone."
sourcebook: "_Monster Core_, page 164."
```

```encounter-table
name: Stone Giant
creatures:
  - 1: Stone Giant
```
