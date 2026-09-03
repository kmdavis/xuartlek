---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Beast Eidolon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/eidolon
  - pf2e/creature/trait/medium
statblock: inline
name: "Beast Eidolon"
level: 10
source: "NPC Core"
aon_id: "creature-3679"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3679"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Beast Eidolon"
level: "Creature 10"
size: "Medium"
trait_01: "Beast"
trait_02: "Eidolon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, low-light vision, scent (imprecise) 30 feet"
languages: "Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Athletics +21, Intimidation +22, Nature +15"
abilityMods: [5, 2, 4, -1, 3, 2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +19; __Ref__: +18; __Will__: +19"
hp: 180
health:
  - name: "HP"
    desc: "180; __Resistances__ cold 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +22 __Damage__ 2d8+11 piercing plus 1d6 persistent bleed plus Grab"
  - name: "Melee"
    desc: "⬻ hoof +22 (Agile) __Damage__ 2d6+11 bludgeoning"
abilities_bot:
  - name: "Furious Charge"
    desc: "⬺ The eidolon Strides twice and then makes a Strike. As long as it moved at least 20 feet, it gains a +2 circumstance bonus to the attack roll."
  - name: "Primal Roar"
    desc: "⬺ (Auditory) The eidolon attempts to Demoralize each enemy within 30 feet; these Demoralize attempts don't take any penalty for not sharing a language."
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Scent of Blood"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature within the eidolon's scent range is taking bleed damage"
  - name: "Effect"
    desc: "The eidolon flies into a frenzy, gaining 10 temporary HP for 1 minute and a +4 status bonus to damage rolls with its unarmed attacks, but becomes off-guard. It can't voluntarily end the frenzy or start another frenzy while in the frenzy. The frenzy lasts for 1 minute, after which the eidolon is fatigued for 1 minute."
sourcebook: "_NPC Core_, page 219."
```

```encounter-table
name: Beast Eidolon
creatures:
  - 1: Beast Eidolon
```
