---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hippocampus"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/large
statblock: inline
name: "Hippocampus"
level: 1
source: "Monster Core"
aon_id: "creature-3050"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3050"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hippocampus"
level: "Creature 1"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +4, Athletics +7"
abilityMods: [4, 1, 4, -4, 3, 1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +9; __Ref__: +4; __Will__: +6"
hp: 24
health:
  - name: "HP"
    desc: "24"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 17"
speed: "5 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +7 (reach 10 feet) __Damage__ 1d6+4 bludgeoning"
abilities_bot:
  - name: "Sudden Retreat"
    desc: "⬺ The hippocampus makes a tail Strike, then Swims with a +10-foot circumstance bonus to its swim Speed. It gains a +2 circumstance bonus to AC against reactions triggered by this movement. Aquatic Cavalry Protecting the harbor of Absalom and the shores of Starstone Isle, the elite Wave Riders use combat-trained hippocampi as mounts. The Wave Riders harass enemy ships, defend against aquatic foes, and intercept smugglers."
sourcebook: "_Monster Core_, page 196."
```

```encounter-table
name: Hippocampus
creatures:
  - 1: Hippocampus
```
