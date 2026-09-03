---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Orca"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Orca"
level: 5
source: "Monster Core"
aon_id: "creature-2927"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2927"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Orca"
level: "Creature 5"
size: "Huge"
trait_01: "Animal"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; aquatic echolocation 120 feet, low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [7, 2, 5, -4, 3, 0]
abilities_top:
  - name: "Aquatic Echolocation"
    desc: "An orca can use its hearing as a precise sense at the listed range, but only underwater."
  - name: "Deep Breath"
    desc: "An orca can hold its breath for 2 hours."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +11; __Will__: +12"
hp: 75
health:
  - name: "HP"
    desc: "75"
speed: "swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+9 piercing plus Grab"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 30 feet. An orca can travel no further than 5 feet onto land as part of an Aquatic Ambush. After it does so, it's [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Crawl|Crawls]] to return to the water."
  - name: "Breach"
    desc: "⬺ The orca Swims up to its swim Speed, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] vertically out of the water up to 25 feet in the air, making a Strike against a creature at any point during the jump (this lets it attack a creature within 30 feet of the water's surface). After the Strike, the orca splashes back down into the water."
sourcebook: "_Monster Core_, page 103."
```

```encounter-table
name: Orca
creatures:
  - 1: Orca
```
