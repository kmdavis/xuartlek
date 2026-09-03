---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Skeleton Infantry"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/skeleton
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Skeleton Infantry"
level: 11
source: "Monster Core 2"
aon_id: "creature-4549"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4549"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Skeleton Infantry"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Troop"
trait_04: "Undead"
trait_05: "Unholy"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +18"
abilityMods: [5, 3, 4, -5, 2, 0]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +18; __Will__: +19"
hp: 180
health:
  - name: "HP"
    desc: "180 (4 segments); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious; __Resistances__ cold 5, electricity 5, fire 5, piercing 10, slashing 10; __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Form a Phalanx"
    desc: "⬻ Many of the skeletons raise their shields to protect others. The infantry gains a +2 circumstance bonus to AC until the start of their next turn. __Hurl Javelins!__ ⬺ The troop's members throw a volley of javelins. Each creature in a 10-foot burst within 30 feet of the troop takes 2d6+10 piercing damage (DC 27 basic Reflex save). When the troop is reduced to 2 segments, this area decreases to a 5-foot burst. __Lower Spears!__"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The skeletons engage in a coordinated longspear attack against each enemy in a 10-foot emanation basic Reflex save). The damage depends on the number of actions. ⬻ 2d8 piercing damage ⬺ 3d8+7 piercing damage ⬽ 4d8+12 piercing damage"
  - name: "Phalanx Charge"
    desc: "⬺"
  - name: "Requirements"
    desc: "The infantry is in a phalanx"
  - name: "Effect"
    desc: "The skeletons lower their longspears and charge. The troop Strides in a straight line until it's adjacent to an enemy then uses Lower Spears!, dealing 3d8+7 piercing damage. Any creature that fails its save is also knocked prone."
sourcebook: "_Monster Core 2_, page 290."
```

```encounter-table
name: Skeleton Infantry
creatures:
  - 1: Skeleton Infantry
```
