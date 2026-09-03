---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brine Shark"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Brine Shark"
level: 3
source: "Monster Core"
aon_id: "creature-2989"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2989"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Brine Shark"
level: "Creature 3"
size: "Medium"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +8"
abilityMods: [3, 2, 2, -4, 1, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +11; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
speed: "15 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d12+7 piercing plus Grab"
abilities_bot:
  - name: "Deep Plunge"
    desc: "⬻ The brine shark dives into the water, [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swimming]] twice straight down. If it's [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbing]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restraining]] a creature, it brings that creature along with it."
sourcebook: "_Monster Core_, page 148."
```

```encounter-table
name: Brine Shark
creatures:
  - 1: Brine Shark
```
