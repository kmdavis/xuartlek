---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Therizinosaurus"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Therizinosaurus"
level: 9
source: "Howl of the Wild"
aon_id: "creature-3264"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3264"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Therizinosaurus"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [7, 1, 6, -4, 3, 0]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +16; __Will__: +16"
hp: 210
health:
  - name: "HP"
    desc: "210"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+7 slashing plus winnowing claws"
abilities_bot:
  - name: "Stomp Pests"
    desc: "⬺ The therizinosaurus stomps about, dealing 5d8 bludgeoning damage (DC 28 basic Reflex save) to each adjacent creature. Large or smaller creatures who fail their save are also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Swiping Claws"
    desc: "⬺ The therizinosaurus makes two claw Strikes against different targets. Both attacks count toward its multiple attack penalty, but do not increase the penalty until it has made both attacks."
  - name: "Winnowing Claws"
    desc: "Whenever the therizinosaurus successfully Strikes a Large or smaller creature with its claw, it pulls that creature 5 feet toward it (10 feet on a critical hit)."
sourcebook: "_Howl of the Wild_, page 138."
```

```encounter-table
name: Therizinosaurus
creatures:
  - 1: Therizinosaurus
```
