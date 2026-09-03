---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Werewolf"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/werecreature
  - pf2e/creature/trait/medium
statblock: inline
name: "Werewolf"
level: 3
source: "Monster Core"
aon_id: "creature-3236"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3236"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Werewolf"
level: "Creature 3"
size: "Medium"
trait_01: "Beast"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Werecreature"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
languages: "Common; wolf empathy"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Athletics +9, Survival +10"
abilityMods: [4, 2, 2, -1, 2, 1]
abilities_top:
  - name: "Wolf Empathy"
    desc: "The werewolf can communicate with canine creatures."
  - name: "Items"
    desc: "battle axe, Composite Shortbow (20 arrows), Studded Leather Armor"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +11; __Ref__: +9; __Will__: +7"
hp: 63
health:
  - name: "HP"
    desc: "63; __Weaknesses__ silver 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ battle axe +11 (Sweep) __Damage__ 1d8+8 slashing"
  - name: "Melee"
    desc: "⬻ claw +11 (Agile) __Damage__ 1d6+8 slashing"
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d8+8 piercing plus curse of the werewolf"
  - name: "Ranged"
    desc: "⬻ composite shortbow +9 (deadly d10, range increment 60 feet, reload 0) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) Human with fist +11 for 1d4+8 bludgeoning, or wolf with Speed 40 feet and jaws with Knockdown."
  - name: "Curse of the Werewolf"
    desc: "(Curse, Primal)"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Moon Frenzy"
    desc: "(Polymorph, Primal)"
  - name: "Pack Attack"
    desc: "The werewolf's Strikes deal 1d6 extra damage to creatures within reach of at least two of the werewolf's allies."
sourcebook: "_Monster Core_, page 346."
```

```encounter-table
name: Werewolf
creatures:
  - 1: Werewolf
```
