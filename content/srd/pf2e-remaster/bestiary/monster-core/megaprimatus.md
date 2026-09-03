---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Megaprimatus"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Megaprimatus"
level: 8
source: "Monster Core"
aon_id: "creature-2828"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2828"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Megaprimatus"
level: "Creature 8"
size: "Gargantuan"
trait_01: "Animal"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +19"
abilityMods: [7, 2, 5, -4, 1, 2]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +19; __Ref__: +16; __Will__: +13"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +21 (Agile, reach 20 feet) __Damage__ 2d8+10 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +21 (reach 10 feet) __Damage__ 2d10+10 piercing"
abilities_bot:
  - name: "Mangling Rend"
    desc: "⬺ A megaprimatus makes two fist Strikes against the same target. If both hit, the attack deals an additional 2d6 bludgeoning damage, the target is off-guard, and the target takes a –20-foot status penalty to all Speeds until the end of its next turn."
  - name: "Terrifying Display"
    desc: "⬺ (Auditory, Emotion, Fear, Mental) The megaprimatus beats its chest in a terrifying display. Creatures within 50 feet must attempt a DC 27 Will save. While a creature is frightened by this ability, it is off-guard to the megaprimatus and to gorillas."
  - name: "Critical Success"
    desc: "No effect and temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is frightened 1."
  - name: "Critical Failure"
    desc: "The creature is frightened 2 and fleeing until the end of its next turn."
sourcebook: "_Monster Core_, page 23."
```

```encounter-table
name: Megaprimatus
creatures:
  - 1: Megaprimatus
```
