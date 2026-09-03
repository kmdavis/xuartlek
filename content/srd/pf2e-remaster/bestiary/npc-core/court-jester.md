---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Court Jester"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Court Jester"
level: 10
source: "NPC Core"
aon_id: "creature-3578"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3578"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Court Jester"
level: "Creature 10"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21"
languages: "Common; up to 4 others"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Deception +19, Diplomacy +19, Performance +22, Society +19, Stealth +19"
abilityMods: [2, 4, 1, 2, 1, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 striking dagger_ (3), face paints"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +16; __Ref__: +19; __Will__: +22"
hp: 170
health:
  - name: "HP"
    desc: "170; __Resistances__ poison 10"
abilities_mid:
  - name: "Pointed Joke"
    desc: "The court jester can use Performance instead of Intimidation to Demoralize."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +22 (Agile, Finesse, Magical, versatile S) __Damage__ 2d4+8 piercing plus 4d4 persistent poison"
  - name: "Melee"
    desc: "⬻ fist +21 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _dagger_ +22 (Agile, Magical, thrown 10 feet, versatile S) __Damage__ 2d4+8 piercing plus 4d4 persistent poison"
abilities_bot:
  - name: "Poisoned Blade"
    desc: "The jester coats their dagger in poison. These daggers inflict an additional 4d4 persistent poison damage. The poison expires 1 hour after leaving the jester's possession. __No Peeking!__ ⬻ The jester blows chalk or face powder in an adjacent enemy's face. The target must make a DC 29 Fortitude saving throw."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is dazzled for 1 round."
  - name: "Failure"
    desc: "target is dazzled and off-guard for 1 round."
  - name: "Critical Failure"
    desc: "The target is blinded for 1 round."
sourcebook: "_NPC Core_, page 129."
```

```encounter-table
name: Court Jester
creatures:
  - 1: Court Jester
```
