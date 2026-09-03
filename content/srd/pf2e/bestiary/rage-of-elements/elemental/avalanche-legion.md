---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Avalanche Legion"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Avalanche Legion"
level: 11
source: "Rage of Elements"
aon_id: "creature-2622"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2622"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Avalanche Legion"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: "Troop"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23"
abilityMods: [5, 0, 4, -2, 1, 0]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the avalanche legion is slowed 1."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +24; __Ref__: +20; __Will__: +21"
hp: 240
health:
  - name: "HP"
    desc: "240 (16 squares); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet, burrow 25 feet; earth glide, troop movement"
abilities_bot:
  - name: "Earth Glide"
    desc: "The avalanche legion can Burrow through any earthen matter, including rock. When it does so, the legion moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Pummeling Boulders"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The avalanche legion unleashes an onslaught of blows against each enemy in a 5-foot emanation (DC 28 basic Reflex save). The damage depends on the number of actions. ⬻ 2d8 bludgeoning damage ⬺ 3d8+8 bludgeoning damage ⬽ 4d8+11 bludgeoning damage"
  - name: "Spinning Stones"
    desc: "⬺ The avalanche legion spins in place, kicking up a barrage of stones. Each creature in a 10-foot burst within 30 feet of the troop takes 1d12+8 bludgeoning damage (DC 28 basic Reflex save). When the troop is reduced to 8 or fewer squares, this area decreases to a 5-foot burst."
  - name: "Trample into the Earth"
    desc: "⬽ The avalanche legion speeds forward, running over creatures with their stone bodies and knocking them down. As Trample; Gargantuan or smaller, 2d8 bludgeoning damage, DC 28. A creature that critically fails its save is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. Familial Instincts Although elementals don't reproduce like typical creatures, living landslide sometimes develop bonds with smaller or weaker earth elementals, such as earth wisps, living boulders, and sod hounds. When several of these smaller elementals are gathered in one place, living landslides who cared for the creatures often continue to watch over their wards. Avalanche legions sometimes form from these gatherings, as multiple living landslides join forces to protect the smaller elementals."
sourcebook: "_Rage of Elements_, page 102."
```

```encounter-table
name: Avalanche Legion
creatures:
  - 1: Avalanche Legion
```
