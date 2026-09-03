---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crocodile"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Crocodile"
level: 2
source: "Monster Core"
aon_id: "creature-2887"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2887"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Crocodile"
level: "Creature 2"
size: "Large"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7"
abilityMods: [4, 1, 3, -5, 1, -4]
abilities_top:
  - name: "Deep Breath"
    desc: "The crocodile can hold its breath for about 2 hours."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +9; __Ref__: +7; __Will__: +5"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "20 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 __Damage__ 1d10+4 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 35 feet"
  - name: "Death Roll"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]])"
  - name: "Requirements"
    desc: "The crocodile must have a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The crocodile tucks its legs and rolls rapidly, twisting its victim. It makes a jaws Strike with a +2 circumstance bonus to the attack roll against the grabbed creature. If it hits, it also knocks the creature [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. If it fails, it releases the creature."
sourcebook: "_Monster Core_, page 69."
```

```encounter-table
name: Crocodile
creatures:
  - 1: Crocodile
```
