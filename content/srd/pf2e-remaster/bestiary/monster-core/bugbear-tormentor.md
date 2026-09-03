---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bugbear Tormentor"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/bugbear
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Bugbear Tormentor"
level: 3
source: "Monster Core"
aon_id: "creature-2861"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2861"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Bugbear Tormentor"
level: "Creature 3"
size: "Medium"
trait_01: "Bugbear"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision, scent (imprecise) 30 feet"
languages: "Common, Goblin"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +9, Intimidation +7, Stealth +8, Thievery +8"
abilityMods: [4, 3, 2, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Chain Shirt, Dagger, Sickle (2)"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +9; __Ref__: +10; __Will__: +6"
hp: 44
health:
  - name: "HP"
    desc: "44"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +11 (Agile, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ sickle +11 (Agile, Trip) __Damage__ 1d4+6 slashing"
  - name: "Ranged"
    desc: "⬻ dagger +10 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The bugbear tormentor deals 1d6 extra precision damage to off-guard creatures."
  - name: "Twin Feint"
    desc: "⬺ The bugbear tormentor makes a dazzling series of attacks with two weapons, using the first attack to throw their foe off-guard against a second attack at a different angle. They make one Strike with each of their two melee weapons, both against the same target. The target is automatically off-guard against the second attack. The bugbear tormentor applies their multiple attack penalty to these Strikes normally."
sourcebook: "_Monster Core_, page 47."
```

```encounter-table
name: Bugbear Tormentor
creatures:
  - 1: Bugbear Tormentor
```
