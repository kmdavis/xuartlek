---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ogre Spider"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Ogre Spider"
level: 5
source: "Monster Core 2"
aon_id: "creature-4562"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4562"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ogre Spider"
level: "Creature 5"
size: "Huge"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, web sense"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13"
abilityMods: [6, 4, 4, -5, 2, -4]
abilities_top:
  - name: "Web Sense"
    desc: "The ogre spider has imprecise tremorsense to detect the vibrations of creatures touching its web"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +15; __Ref__: +13; __Will__: +9"
hp: 70
health:
  - name: "HP"
    desc: "70"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ bite +15 __Damage__ 2d8+8 piercing plus ogre spider venom"
  - name: "Ranged"
    desc: "⬻ web +13 (range increment 30 feet) __Damage__ web trap"
abilities_bot:
  - name: "Eerie Flexibility"
    desc: "An ogre spider can fit through tight spaces as if it were a Large creature. While Squeezing, it can move at its full Speed."
  - name: "Ogre Spider Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage, [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1, and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 round)"
  - name: "Stage 3"
    desc: "2d6 poison damage, clumsy 1, and enfeebled 1 (1 round)"
  - name: "Stage 4"
    desc: "2d6 poison damage, clumsy 2, and enfeebled 2 (1 round)"
  - name: "Web Trap"
    desc: "A creature hit by the ogre spider's web attack is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] and stuck to the nearest surface until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 22)."
sourcebook: "_Monster Core 2_, page 302."
```

```encounter-table
name: Ogre Spider
creatures:
  - 1: Ogre Spider
```
