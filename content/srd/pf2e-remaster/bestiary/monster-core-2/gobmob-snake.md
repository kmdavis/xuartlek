---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gobmob Snake"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/goblin
  - pf2e/creature/trait/mutant
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Gobmob Snake"
level: 4
source: "Monster Core 2"
aon_id: "creature-4416"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4416"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Gobmob Snake"
level: "Creature 4"
size: "Medium"
trait_01: "Aberration"
trait_02: "Goblin"
trait_03: "Mutant"
trait_04: "Uncommon"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, scent (imprecise) 30 feet"
languages: "Common, Goblin; snake empathy"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +10, Intimidation +9, Stealth +12, Survival +8"
abilityMods: [3, 5, 2, -2, 1, 2]
abilities_top:
  - name: "Snake Empathy"
    desc: "(primal) A gobmob snake can communicate with snakes."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +13; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60"
abilities_mid:
  - name: "Incessant Yammering"
    desc: "(auditory, aura, linguistic) 15 feet. A gobmob snake's heads constantly bicker and snipe at one another, annoying and distracting anyone nearby. Each non-goblin creature that begins its turn in the aura must attempt a DC 21 Will save. On a failure, it takes a –1 status penalty to Perception checks and Will saves for 1 round. On a success, it is temporarily immune for 1 minute."
  - name: "Infighting"
    desc: "Whenever a gobmob snake critically fails at an attack roll or skill check, it must succeed at a DC 5 flat check or become slowed 1 as its heads argue over which of them is to blame. An enemy can provoke an argument by attempting a DC 20 Deception check as a single action with the auditory, concentrate, linguistic, and mental traits."
  - name: "Coiled Strike"
    desc: "⬲ As Reactive Strike, but the gobmob snake can use this reaction only if it's Coiled."
speed: "25 feet, burrow 5 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +14 (Finesse, unarmed) __Damage__ 2d6+5 piercing"
abilities_bot:
  - name: "Coil"
    desc: "⬻ The gobmob snake uses an action to coil itself, increasing its reach with its fangs from 5 to 10 feet. After the goblin snake Strikes with its fangs, it becomes uncoiled."
  - name: "Goblin Breath"
    desc: "⬺ (Olfactory, poison) The gobmob snake belches a cloud of nauseating vapor in a 15-foot cone. Non-goblin creatures within the cloud must succeed at a DC 20 Fortitude save or become sickened 1. On a critical failure, a creature is also slowed 1 for as long as it is sickened. Creatures that successfully save are immune for 24 hours. The goblin snake can't use Goblin Breath again for 1d4 rounds."
sourcebook: "_Monster Core 2_, page 168."
```

```encounter-table
name: Gobmob Snake
creatures:
  - 1: Gobmob Snake
```
