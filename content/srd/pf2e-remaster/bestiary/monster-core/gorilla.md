---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gorilla"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Gorilla"
level: 3
source: "Monster Core"
aon_id: "creature-2827"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2827"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gorilla"
level: "Creature 3"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +11, Stealth +7"
abilityMods: [4, 2, 3, -4, 1, -2]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +9; __Will__: +6"
hp: 45
health:
  - name: "HP"
    desc: "45"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, reach 10 feet) __Damage__ 2d6+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +11 (reach 5 feet) __Damage__ 1d8+4 piercing"
abilities_bot:
  - name: "Frightening Display"
    desc: "⬺ (Auditory, Emotion, Fear, Mental) The gorilla beats its chest in a terrifying display. Creatures within 30 feet must attempt a DC 20 Will save. While a creature is frightened by this ability, it is off-guard to the gorilla."
  - name: "Critical Success"
    desc: "No effect and temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is frightened 1."
  - name: "Critical Failure"
    desc: "The creature is frightened 2. Gigantopithecus These fierce kin of orangutans are three times heavier than a gorilla. They are level 4, with statistics roughly akin to an elite gorilla."
sourcebook: "_Monster Core_, page 23."
```

```encounter-table
name: Gorilla
creatures:
  - 1: Gorilla
```
