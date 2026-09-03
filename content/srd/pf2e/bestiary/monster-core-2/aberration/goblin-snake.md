---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Snake"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/small
statblock: inline
name: "Goblin Snake"
level: 1
source: "Monster Core 2"
aon_id: "creature-4415"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4415"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Goblin Snake"
level: "Creature 1"
size: "Small"
trait_01: "Aberration"
trait_02: "Goblin"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Goblin|Goblin]]; snake empathy"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +4"
abilityMods: [3, 4, 2, -2, 0, 1]
abilities_top:
  - name: "Snake Empathy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) A goblin snake can communicate with snakes."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +10; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15"
abilities_mid:
  - name: "Coiled Strike"
    desc: "⬲ As Reactive Strike, but the goblin snake can use this reaction only if it's Coiled."
speed: "25 feet, burrow 5 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Coil"
    desc: "⬻ The goblin snake uses an action to coil itself, increasing its reach with its fangs from 5 to 10 feet. After the goblin snake Strikes with its fangs, it becomes uncoiled."
  - name: "Goblin Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|Olfactory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) The goblin snake belches a cloud of nauseating vapor in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]]. Non-[[srd/pf2e/compendium/rules-elements/traits/player-core/goblin|goblin]] creatures within the cloud must succeed at a DC 16 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1. On a critical failure, a creature is also [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for as long as it is sickened. Creatures that successfully save are immune for 24 hours. The goblin snake can't use Goblin Breath again for 1d4 rounds."
sourcebook: "_Monster Core 2_, page 168."
```

```encounter-table
name: Goblin Snake
creatures:
  - 1: Goblin Snake
```
