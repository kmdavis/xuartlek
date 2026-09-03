---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vescavor Queen"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Vescavor Queen"
level: 9
source: "Monster Core"
aon_id: "creature-3228"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3228"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vescavor Queen"
level: "Creature 9"
size: "Large"
trait_01: "Fiend"
trait_02: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +20, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +20, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +16"
abilityMods: [6, 5, 5, 1, 3, 2]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +17; __Ref__: +19; __Will__: +15"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 10; __Weaknesses__ cold iron 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 1d10+13 piercing plus 1d10 acid"
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d10+8 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d4 piercing plus 2d10 acid"
  - name: "Ranged"
    desc: "⬻ spit +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 30 feet) __Damage__ 2d8 acid plus rage pheromones"
abilities_bot:
  - name: "Chaotic Spawning"
    desc: "⬽ The vescavor queen strengthens her swarms. All [[srd/pf2e/bestiary/monster-core/fiend/vescavor-swarm|vescavor swarms]] within 100 feet become Huge and [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]] for 1 minute. Vescavor swarms can only use the extra action each round for the Ravenous Bites action."
  - name: "Feeding Time"
    desc: "⬻ The vescavor queen causes any number of vescavor swarms within 100 feet to immediately use their reaction to perform the Ravenous Bites action."
  - name: "Opportune Snack"
    desc: "⬻ The vescavor queen pulls a creature it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] into a space adjacent to it and makes a jaws Strike with a +2 circumstance bonus."
  - name: "Rage Pheromones"
    desc: "If the vescavor queen's spit Strike damages a creature, it takes a –2 status penalty to all saving throws imposed by vescavor swarms for 1 minute."
sourcebook: "_Monster Core_, page 339."
```

```encounter-table
name: Vescavor Queen
creatures:
  - 1: Vescavor Queen
```
