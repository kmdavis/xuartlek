---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cave Giant"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Cave Giant"
level: 6
source: "Monster Core 2"
aon_id: "creature-4408"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4408"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Cave Giant"
level: "Creature 6"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +14"
abilityMods: [6, 3, 5, -2, 3, 2]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/runes/weapon-potency-3|+1]] [[srd/pf2e/compendium/equipment/weapons/axe/greataxe|greataxe]]_, [[srd/pf2e/compendium/equipment/armor#Hide Armor|Hide Armor]]"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +13; __Will__: +11"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]]) __Damage__ 1d12+9 slashing"
  - name: "Melee"
    desc: "⬻ fist +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 1d8+9 bludgeoning"
  - name: "Ranged"
    desc: "⬻ rock +16 (Brutal, range increment 120 feet) __Damage__ 2d6+10 bludgeoning"
abilities_bot:
  - name: "Forceful Fracture"
    desc: "⬺"
  - name: "Requirements"
    desc: "The cave giant is within reach of any kind of stone"
  - name: "Effect"
    desc: "The cave giant pounds their fist into the nearby stone, fracturing it into chunks to hurl at other creatures. The giant then makes two ranged rock Strikes, each targeting a separate creature. Both attacks count toward their multiple attack penalty, but the penalty doesn't increase until after they've made both attacks."
  - name: "Smear"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Requirements"
    desc: "The cave giant is within reach of a creature that is adjacent to a wall or other solid vertical surface"
  - name: "Effect"
    desc: "The cave giant snags the creature and smashes it against the wall. The giant attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the target's Reflex DC. On a success, the cave giant Grabs the creature and smears it along the nearby wall, dealing 2d8+8 bludgeoning damage. On a critical success, the damage is doubled. Cave Giant Allies A lucky cave giant might manage to capture and tame a giant reptile, such as a monitor lizard or giant salamander, to serve as a maltreated pet or guard beast. These reptiles are often abused by their cruel keepers, learning to react toward all humanoids with fear and violence."
sourcebook: "_Monster Core 2_, page 162."
```

```encounter-table
name: Cave Giant
creatures:
  - 1: Cave Giant
```
