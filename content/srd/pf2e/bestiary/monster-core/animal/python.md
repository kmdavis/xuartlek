---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Python"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Python"
level: 1
source: "Monster Core"
aon_id: "creature-3201"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3201"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Python"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [3, 3, 3, -4, 1, -2]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +10; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Tighten Coils"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the python attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]]"
  - name: "Effect"
    desc: "The DC of the Escape check is increased by 2."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 __Damage__ 1d8+3 piercing plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d8 bludgeoning, DC 17"
  - name: "Wrap in Coils"
    desc: "⬻"
  - name: "Requirements"
    desc: "A Medium or smaller creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in the python's jaws"
  - name: "Effect"
    desc: "The python moves the creature into its coils, freeing its jaws to make attacks, then uses Constrict against the creature. The python's coils can hold one creature."
sourcebook: "_Monster Core_, page 316."
```

```encounter-table
name: Python
creatures:
  - 1: Python
```
