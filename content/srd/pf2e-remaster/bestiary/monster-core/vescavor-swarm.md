---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vescavor Swarm"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Vescavor Swarm"
level: 5
source: "Monster Core"
aon_id: "creature-3227"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3227"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vescavor Swarm"
level: "Creature 5"
size: "Large"
trait_01: "Fiend"
trait_02: "Swarm"
trait_03: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Chthonian"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +10, Stealth +13"
abilityMods: [-2, 5, 4, -3, 1, 1]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +15; __Will__: +9"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ grabbed, precision, prone, restrained, swarm mind; __Resistances__ bludgeoning 5, piercing 5, slashing 2; __Weaknesses__ area damage 5, cold iron 5, holy 5, splash damage 5"
speed: "20 feet, fly 40 feet"
abilities_bot:
  - name: "Devour All"
    desc: "⬺ The swarm eat away the very earth beneath their feet. The swarms Strides. All squares they occupy during their movement becomes difficult terrain. Any creatures they move through must succeed a DC 21 Reflex save or fall prone."
  - name: "Maddening Gibbers"
    desc: "⬻ (Auditory, Mental) Each stupefied creature in the swarm's space must attempt a DC 21 Will saving throw as the swarm yammers the endless chorus of the Outer Rifts."
  - name: "Critical Success"
    desc: "The target is unaffected and is temporarily immune to Maddening Gibbers for 1 minute."
  - name: "Success"
    desc: "The target is unaffected and is immune to Maddening Gibbers for 1 round."
  - name: "Failure"
    desc: "The target becomes confused for 1 round."
  - name: "Critical Failure"
    desc: "The target becomes confused for 1 round and can't target fiends while confused in this way."
  - name: "Ravenous Bites"
    desc: "⬻ Each enemy in the swarm's space takes 3d6 piercing damage (DC 20 basic Fortitude save). A creature that fails its save is also stupefied 1 for 1 round."
sourcebook: "_Monster Core_, page 338."
```

```encounter-table
name: Vescavor Swarm
creatures:
  - 1: Vescavor Swarm
```
