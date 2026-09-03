---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Majungasaurus"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/huge
statblock: inline
name: "Majungasaurus"
level: 6
source: "Howl of the Wild"
aon_id: "creature-3262"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3262"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Majungasaurus"
level: "Creature 6"
size: "Huge"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +16, Intimidation +14, Stealth +16"
abilityMods: [6, 5, 4, -4, 2, 4]
abilities_top:
  - name: "Startling Roar"
    desc: "When the majungasaurus rolls initiative using Stealth, it can attempt to Demoralize each creature within 30 feet as a free action. Regardless of the effect, each creature is then temporarily immune for 1 hour."
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +17; __Will__: +12"
hp: 120
health:
  - name: "HP"
    desc: "120"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 (reach 15 feet) __Damage__ 2d8+6 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ foot +16 (Agile) __Damage__ 2d6+6 bludgeoning"
abilities_bot:
  - name: "Crack Bones"
    desc: "⬻"
  - name: "Requirements"
    desc: "The majungasaurus has a creature grabbed in its jaws"
  - name: "Effect"
    desc: "The majungasaurus deals that creature 3d8 bludgeoning damage (DC 24 basic Fortitude save). A creature that fails this save is clumsy 1 until it recovers to full Hit Points."
  - name: "Frightened Prey"
    desc: "Frightened creatures are off-guard to a majungasaurus."
sourcebook: "_Howl of the Wild_, page 137."
```

```encounter-table
name: Majungasaurus
creatures:
  - 1: Majungasaurus
```
