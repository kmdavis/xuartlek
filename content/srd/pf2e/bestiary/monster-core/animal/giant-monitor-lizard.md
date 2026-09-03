---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Monitor Lizard"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Monitor Lizard"
level: 2
source: "Monster Core"
aon_id: "creature-3088"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3088"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Monitor Lizard"
level: "Creature 2"
size: "Medium"
trait_01: "Animal"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +9, Stealth +6"
abilityMods: [3, 2, 3, -4, 1, -2]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +8; __Will__: +5"
hp: 36
health:
  - name: "HP"
    desc: "36"
abilities_mid:
  - name: "Gnashing Grip"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature grabbed by the giant monitor lizard's jaws fails a check to Escape"
  - name: "Effect"
    desc: "The giant monitor lizard's jaws deal 1d6 piercing damage and the triggering creature is exposed to monitor lizard venom."
speed: "30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +11 __Damage__ 1d10+3 piercing plus Grab and monitor lizard venom"
abilities_bot:
  - name: "Lurching Charge"
    desc: "⬺ The giant monitor lizard Strides twice and then makes a jaws Strike. If the lizard moved at least 20 feet away from its starting position, it gains a +2 circumstance bonus to this attack roll."
  - name: "Monitor Lizard Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core_, page 224."
```

```encounter-table
name: Giant Monitor Lizard
creatures:
  - 1: Giant Monitor Lizard
```
