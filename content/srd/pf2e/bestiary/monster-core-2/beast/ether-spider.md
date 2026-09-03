---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ether Spider"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/ethereal
  - pf2e/creature/trait/large
statblock: inline
name: "Ether Spider"
level: 5
source: "Monster Core 2"
aon_id: "creature-4398"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4398"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ether Spider"
level: "Creature 5"
size: "Large"
trait_01: "Beast"
trait_02: "Ethereal"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [5, 4, 3, -2, 1, 7]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +15; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75"
speed: "40 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 1d10+7 piercing plus ether spider venom and Grab"
  - name: "Ranged"
    desc: "⬻ web +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 30 feet) __Damage__ ethereal web trap"
abilities_bot:
  - name: "Ether Spider Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage, clumsy 2 and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 (1 round)"
  - name: "Stage 3"
    desc: "3d6 poison damage, clumsy 3 and slowed 2 (1 round)"
  - name: "Ethereal Step"
    desc: "⬻ The ether spider shifts to either the [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]] or [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]]. The ether spider can remain on the Ethereal Plane indefinitely without ill effect. While there, it can see clearly into the Universe with a range of 60 feet. On its first round in an encounter, the ether spider can use this ability once as a free action."
  - name: "Ethereal Web Trap"
    desc: "A creature hit by the ether spider's web attack is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] and stuck to the nearest surface ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 22)."
  - name: "Web Burst"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The ether spider flings a gout of stored webs in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]]. These webs can pass between [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] and the [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]]. Each creature in the area is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], as ethereal web trap, unless it succeeds at a DC 22 Reflex save. Ether Spider Foes The [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]] is a sparsely populated realm in comparison to most, used more for traveling than dwelling. Yet the deep mists here conceal denizens such as monstrous parasitic beings that use humanoids as incubators for eggs, [[srd/pf2e/compendium/rules-elements/traits/player-core/fiend|fiends]] born from the raw fears of mortal life, and ether spiders that are ever vigilant against those foes' machinations."
sourcebook: "_Monster Core 2_, page 154."
```

```encounter-table
name: Ether Spider
creatures:
  - 1: Ether Spider
```
