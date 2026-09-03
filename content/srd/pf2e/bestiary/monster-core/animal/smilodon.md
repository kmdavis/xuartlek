---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Smilodon"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Smilodon"
level: 6
source: "Monster Core"
aon_id: "creature-2868"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2868"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Smilodon"
level: "Creature 6"
size: "Large"
trait_01: "Animal"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [6, 2, 3, -4, 2, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +12; __Will__: +10"
hp: 110
health:
  - name: "HP"
    desc: "110"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +16 __Damage__ 2d10+6 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d8+6 slashing plus Grab"
abilities_bot:
  - name: "Pierce Armor"
    desc: "⬻ The smilodon makes a fangs Strike against a creature that's [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]. If the attack hits, the creature is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]; if the creature is wearing armor with Hardness 10 or lower, the armor is [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]]. If this Strike breaks a creature's armor or damages a creature who is unarmored or wearing broken armor, the creature also takes 2d6 persistent bleed damage. This Strike doesn't further damage armor that's already broken."
  - name: "Pounce"
    desc: "⬻ The smilodon Strides and makes a Strike at the end of that movement. If the smilodon began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after this ability's Strike."
  - name: "Sneak Attack"
    desc: "The smilodon deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 51."
```

```encounter-table
name: Smilodon
creatures:
  - 1: Smilodon
```
