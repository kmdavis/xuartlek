---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shuln"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Shuln"
level: 12
source: "Monster Core"
aon_id: "creature-3191"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3191"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shuln"
level: "Creature 12"
size: "Huge"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; scent 30 feet, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +22"
abilityMods: [7, 4, 6, -3, 4, 1]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +19; __Will__: +21"
hp: 195
health:
  - name: "HP"
    desc: "195; __Resistances__ physical 10 (except adamantine or bludgeoning), [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 15"
speed: "40 feet, burrow 20 feet; unstoppable burrow"
attacks:
  - name: "Melee"
    desc: "⬻ adamantine claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d8+10 slashing"
  - name: "Melee"
    desc: "⬻ adamantine fangs +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+10 piercing plus shuln saliva"
abilities_bot:
  - name: "Armor-Rending Strikes"
    desc: "Any time the shuln scores a critical hit with a melee Strike, it also deals the same amount of damage to the target's armor, bypassing any Hardness lower than 10, as if adamantine."
  - name: "Shuln Saliva"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 32 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and slowed 1 (1 round)"
  - name: "Stage 3"
    desc: "4d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] for 2d6 hours. Shuln saliva overcomes the inexorable ability."
  - name: "Unstoppable Burrow"
    desc: "Shulns can burrow into solid rock and any metal with a hardness less than that of [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]] as though it were soil or loose rubble, leaving a tunnel 10 feet in diameter. Stubbornness and Spit Adventurers who fear encounters with [[srd/pf2e/bestiary/monster-core/animal/cave-worm|cave worms]] might seek out a shuln and attempt to lure it along or magically compel it to aid in the fight to come, but the shuln's stubborn personality makes such efforts difficult and unreliable. More often, acquiring the shuln's saliva is an easier tactic, although the poison must be alchemically preserved if it is to be used as an injury poison, for this foul-smelling liquid breaks down quickly once it drools from the shuln's toothy maw."
sourcebook: "_Monster Core_, page 309."
```

```encounter-table
name: Shuln
creatures:
  - 1: Shuln
```
