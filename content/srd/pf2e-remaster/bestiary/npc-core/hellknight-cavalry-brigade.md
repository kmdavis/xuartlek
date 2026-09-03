---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hellknight Cavalry Brigade"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Hellknight Cavalry Brigade"
level: 8
source: "NPC Core"
aon_id: "creature-3530"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3530"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Hellknight Cavalry Brigade"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Troop"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common, Diabolic"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +18, Hell Lore +12, Intimidation +17, Religion +12, Society +12"
abilityMods: [7, 1, 4, 2, 2, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +16"
hp: 135
health:
  - name: "HP"
    desc: "135 (4 segments); __Resistances__ mental 5, slashing 5; __Weaknesses__ area damage 8, splash damage 8"
abilities_mid:
  - name: "Mounted Troop"
    desc: "Effects that target only animals or only humanoids might not work on the Hellknight cavalry brigade, subject to the GM's discretion."
  - name: "Troop Defenses"
    desc: ""
speed: "40 feet; trailblazing stride, troop movement"
abilities_bot:
  - name: "Arrow Volley"
    desc: "⬺ The Hellknights draw or reload their longbows, then launch a ranged attack in the form of a volley. This volley is a 10-foot burst within 100 feet that deals 3d8 piercing damage (DC 23 basic Reflex save). When the troop is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Lance Charge"
    desc: "⬽ The brigade Strides twice with a +10-foot circumstance bonus to its Speed. If it moves at least 10 feet, the brigade deals 3d8+14 piercing damage with a DC 26 basic Reflex save to each enemy in a 10-foot emanation at the end of its movement."
  - name: "Stab from the Saddle"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The brigade engages in a coordinated lance attack against each enemy in a 10-foot emanation with a DC 23 basic Reflex save. The damage depends on the number of actions. ⬻ 1d6+3 piercing damage ⬺ 2d6+10 piercing damage ⬽ 3d6+14 piercing damage"
  - name: "Trailblazing Stride"
    desc: "While moving on land, the Hellknight cavalry brigade ignores difficult terrain."
sourcebook: "_NPC Core_, page 93."
```

```encounter-table
name: Hellknight Cavalry Brigade
creatures:
  - 1: Hellknight Cavalry Brigade
```
