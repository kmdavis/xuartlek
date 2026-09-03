---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Fly"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Fly"
level: 1
source: "Monster Core 2"
aon_id: "creature-4402"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4402"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Giant Fly"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6"
abilityMods: [3, 4, 3, -5, 3, -5]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +9; __Will__: +6"
hp: 20
health:
  - name: "HP"
    desc: "20"
abilities_mid:
  - name: "Avoid the Swat"
    desc: "⬲"
  - name: "Trigger"
    desc: "The giant fly is targeted with a melee or ranged attack by an attacker it can see"
  - name: "Effect"
    desc: "The giant fly gains a +2 circumstance bonus to AC against the triggering attack. If the attack misses, the giant insect can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] up to its fly Speed."
speed: "20 feet, climb 20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +8 __Damage__ 1d6+3 piercing plus fly pox"
abilities_bot:
  - name: "Fly Pox"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/gm-core/virulent|virulent]]) A giant fly could carry any disease, but most transmit a virulent but not fatal infection called fly pox with their bite"
  - name: "Saving Throw"
    desc: "DC 16 Fortitude; Onset 1 day"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 day)"
  - name: "Stage 2"
    desc: "as stage 1 (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 2 (1 day)"
  - name: "Stage 4"
    desc: "as stage 3 (1 day)"
  - name: "Stage 5"
    desc: "enfeebled 2 and [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] (1 day)"
sourcebook: "_Monster Core 2_, page 157."
```

```encounter-table
name: Giant Fly
creatures:
  - 1: Giant Fly
```
