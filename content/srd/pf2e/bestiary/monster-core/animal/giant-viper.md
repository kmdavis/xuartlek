---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Viper"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Viper"
level: 2
source: "Monster Core"
aon_id: "creature-3202"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3202"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Viper"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +6"
abilityMods: [3, 4, 3, -4, 1, -2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +11; __Will__: +6"
hp: 26
health:
  - name: "HP"
    desc: "26"
abilities_mid:
  - name: "Coiled Strike"
    desc: "⬲ As Reactive Strike, but the snake can use this reaction only if it's Coiled."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+3 piercing plus giant viper venom"
abilities_bot:
  - name: "Coil"
    desc: "⬻ The giant viper uses an action to coil itself. While Coiled, the reach of its fangs is 10 feet and it has the Reactive Strike reaction. After the giant viper Strikes with its fangs, it becomes uncoiled."
  - name: "Giant Viper Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]]"
sourcebook: "_Monster Core_, page 317."
```

```encounter-table
name: Giant Viper
creatures:
  - 1: Giant Viper
```
