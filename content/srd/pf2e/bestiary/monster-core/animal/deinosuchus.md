---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deinosuchus"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Deinosuchus"
level: 9
source: "Monster Core"
aon_id: "creature-2888"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2888"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Deinosuchus"
level: "Creature 9"
size: "Huge"
trait_01: "Animal"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16"
abilityMods: [7, 3, 5, -5, 2, -4]
abilities_top:
  - name: "Deep Breath"
    desc: "A deinosuchus can hold its breath for about 2 hours."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +20; __Ref__: +16; __Will__: +15"
hp: 175
health:
  - name: "HP"
    desc: "175"
speed: "30 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+13 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 1d10+11 bludgeoning"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 50 feet"
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 2d8+7 bludgeoning, Rupture 18"
sourcebook: "_Monster Core_, page 69."
```

```encounter-table
name: Deinosuchus
creatures:
  - 1: Deinosuchus
```
