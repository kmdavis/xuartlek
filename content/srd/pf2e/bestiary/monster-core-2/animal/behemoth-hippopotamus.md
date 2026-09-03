---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Behemoth Hippopotamus"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Behemoth Hippopotamus"
level: 10
source: "Monster Core 2"
aon_id: "creature-4439"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4439"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Behemoth Hippopotamus"
level: "Creature 10"
size: "Huge"
trait_01: "Animal"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +23, Stealth +18, Survival +17"
abilityMods: [7, 4, 7, -4, 5, -2]
abilities_top:
  - name: "Deep Breath"
    desc: "The behemoth hippopotamus can hold its breath for 1 hour."
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +22; __Ref__: +17; __Will__: +19"
hp: 190
health:
  - name: "HP"
    desc: "190"
speed: "35 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +23 (deadly d12, reach 10 feet) __Damage__ 2d12+10 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ foot +23 __Damage__ 2d8+10 bludgeoning"
abilities_bot:
  - name: "Aquatic Ambush"
    desc: "⬻ 40 feet"
  - name: "Capsize"
    desc: "⬻ (Attack) The behemoth hippopotamus tries to capsize an adjacent aquatic vessel of its size or smaller. The hippopotamus must succeed at an Athletics check with a DC of 30 (reduced by 5 for each size smaller the vessel is than the hippo) or the pilot's Sailing Lore DC, whichever is higher."
  - name: "Double Chomp"
    desc: "⬻ The behemoth hippo makes a jaws Strike targeting two creatures adjacent to each other. Roll the attack and damage once, and apply it to each creature separately. A Double Chomp counts as two attacks for the multiple attack penalty."
  - name: "Swallow Whole"
    desc: "⬻ Medium, 2d12+10 bludgeoning, Rupture 26"
  - name: "Trample"
    desc: "⬽ Large or smaller, foot, DC 29"
sourcebook: "_Monster Core 2_, page 191."
```

```encounter-table
name: Behemoth Hippopotamus
creatures:
  - 1: Behemoth Hippopotamus
```
