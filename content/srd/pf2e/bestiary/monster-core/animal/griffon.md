---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Griffon"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Griffon"
level: 4
source: "Monster Core"
aon_id: "creature-3034"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3034"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Griffon"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11"
abilityMods: [4, 3, 3, -4, 1, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +13; __Will__: +7"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]]) __Damage__ 2d8+4 piercing"
  - name: "Melee"
    desc: "⬻ talon +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+4 piercing"
  - name: "Melee"
    desc: "⬻ wing +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+4 bludgeoning"
abilities_bot:
  - name: "Flying Strafe"
    desc: "⬺ The griffon [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]]up to its fly Speed and makes two talon Strikes at any point during that movement. Each Strike must target a different creature. The attacks take the normal multiple attack penalty."
  - name: "Pounce"
    desc: "⬻ The griffon Strides and makes a talon Strike at the end of that movement. If the griffon began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after the attack."
  - name: "Regal Shriek"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|Fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The griffon unleashes a shriek that transitions into a terrifying roar. Each creature in a 60-foot emanation must attempt a DC 20 Will save. Regardless of the result, creatures are temporarily immune to all griffons' Regal Shrieks for 10 minutes."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 1]]."
  - name: "Failure"
    desc: "The creature is frightened 2. [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|Animals]] are [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for as long as they're frightened."
  - name: "Critical Failure"
    desc: "The creature is frightened 3. Animals are [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]] as long as they're frightened. Alces Wingless griffons, known as alces, result from a rare mutation. Among a clutch of winged griffons, the alce is typically considered the runt, so alces are rarely seen on their own in the wild, though they're often intentionally bred in captivity as relatively affordable exotic mounts. An alce has a land Speed of 35 feet and loses its fly Speed and Flying Strafe."
sourcebook: "_Monster Core_, page 182."
```

```encounter-table
name: Griffon
creatures:
  - 1: Griffon
```
