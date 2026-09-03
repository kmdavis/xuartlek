---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tiger"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Tiger"
level: 4
source: "Monster Core"
aon_id: "creature-2867"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2867"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tiger"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [5, 3, 3, -4, 2, -2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +13; __Ref__: +11; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 1d10+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d8+7 slashing"
abilities_bot:
  - name: "Pounce"
    desc: "⬻ The tiger Strides and makes a Strike at the end of that movement. If the tiger began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after this ability's Strike."
  - name: "Sneak Attack"
    desc: "The tiger deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Wrestle"
    desc: "⬻ The tiger makes a claw Strike against a creature it is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbing]]. If the attack hits, that creature is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
sourcebook: "_Monster Core_, page 51."
```

```encounter-table
name: Tiger
creatures:
  - 1: Tiger
```
