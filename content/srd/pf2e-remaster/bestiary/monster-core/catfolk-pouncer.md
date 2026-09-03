---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Catfolk Pouncer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/catfolk
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Catfolk Pouncer"
level: 1
source: "Monster Core"
aon_id: "creature-2869"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=2869"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Catfolk Pouncer"
level: "Creature 1"
size: "Medium"
trait_01: "Catfolk"
trait_02: "Humanoid"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision"
languages: "Amurrun, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +6, Nature +4, Stealth +7, Survival +4"
abilityMods: [3, 4, 1, -1, 1, 1]
abilities_top:
  - name: "Items"
    desc: "Dagger (3), Greataxe"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +9; __Will__: +4"
hp: 17
health:
  - name: "HP"
    desc: "17"
abilities_mid:
  - name: "Cat's Luck"
    desc: "⬲ (fortune)"
  - name: "Trigger"
    desc: "The catfolk pouncer fails or critically fails a Reflex saving throw"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Reroll that saving throw and take the better result."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ greataxe +8 (Sweep) __Damage__ 1d12+3 slashing"
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4+3 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4 +3 piercing"
abilities_bot:
  - name: "Sudden Charge"
    desc: "⬺ The catfolk pouncer Strides twice. If the catfolk ends their movement within melee reach of at least one enemy, they can make a melee Strike against that enemy."
sourcebook: "_Monster Core_, page 52."
```

```encounter-table
name: Catfolk Pouncer
creatures:
  - 1: Catfolk Pouncer
```
