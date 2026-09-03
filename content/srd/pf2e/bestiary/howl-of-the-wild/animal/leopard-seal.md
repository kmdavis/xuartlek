---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Leopard Seal"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Leopard Seal"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3306"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3306"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Leopard Seal"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, scent (imprecise) 40 feet, whisker sense 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [6, 4, 3, -4, 1, 2]
abilities_top:
  - name: "Deep Breath"
    desc: "A leopard seal can hold its breath for 30 minutes."
  - name: "Protective Blubber"
    desc: "A leopard seal treats environmental cold effects as if they were one step less extreme (incredible cold becomes extreme, extreme cold becomes severe, and so on). Whisker Sense A leopard seal can use its whiskers to sense vibrations as a precise sense at the listed range, but only underwater."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +12; __Ref__: +14; __Will__: +8"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "15 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +12 __Damage__ 2d8+6 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+6 bludgeoning"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 50 feet."
  - name: "Predatory Slam"
    desc: "⬺"
  - name: "Requirements"
    desc: "The leopard seal is in water"
  - name: "Effect"
    desc: "The leopard seal travels up to 40 feet, ending its movement on land. Enemies adjacent to the leopard seal when it ends its movement take 2d10 bludgeoning damage (DC 21 basic Reflex save) and are knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] on a failure."
sourcebook: "_Howl of the Wild_, page 178."
```

```encounter-table
name: Leopard Seal
creatures:
  - 1: Leopard Seal
```
