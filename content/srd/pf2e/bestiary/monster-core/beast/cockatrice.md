---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cockatrice"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/small
statblock: inline
name: "Cockatrice"
level: 3
source: "Monster Core"
aon_id: "creature-2883"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2883"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cockatrice"
level: "Creature 3"
size: "Small"
trait_01: "Beast"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +11"
abilityMods: [-2, 4, 1, -3, 1, -1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +11; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ petrification"
speed: "20 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ ; beak +13 (Finesse, Magical) __Damage__ 1d8–2 piercing plus calcification"
abilities_bot:
  - name: "Calcification"
    desc: "(Incapacitation, Primal) A peck from a cockatrice hardens the flesh of the creature struck. The target must succeed at a DC 20 Fortitude save or become slowed 1 (or slowed 2 on a critical failure). Further failed saves against calcification increase the slowed condition. Once a creature's actions are reduced to 0 by calcification, that creature becomes petrified. If the creature isn't petrified, the slowed conditions end once 1 minute passes without the creature failing a save against calcification. Every 24 hours after it was petrified, the victim can attempt a DC 20 Fortitude save to recover. On a success, it becomes flesh again, but is slowed 1 for the next 24 hours. On a critical success, the creature recovers and isn't slowed. On a failure, the creature remains petrified but can try again in 24 hours. On a critical failure, the petrification is permanent, and the creature can't attempt any more saves. Cockatrice Treasure Cockatrice lairs sometimes include discarded gear from past victims or smooth, pretty stones disgorged from the creature's craw. Gem workers especially prize precious stones that have been polished to perfection in a cockatrice's crop, and may pay a high price for these so-called “cockatrice rocks.” Soft materials suitable for nesting, such as cloth and leather, rarely survive a cockatrice's attentions, but metal goods are often left in fine working order, since cockatrices seem to have little interest in anything shiny they can't fit in their gullet."
sourcebook: "_Monster Core_, page 66."
```

```encounter-table
name: Cockatrice
creatures:
  - 1: Cockatrice
```
