---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sea Serpent"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Sea Serpent"
level: 12
source: "Monster Core"
aon_id: "creature-3177"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3177"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sea Serpent"
level: "Creature 12"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +18, Athletics +26, Stealth +28"
abilityMods: [8, 4, 6, -4, 2, 0]
abilities_top:
  - name: "Undetectable"
    desc: "(primal) A sea serpent automatically tries to counteract any detection, revelation, or scrying effect attempted against it, using its Stealth modifier for its counteract modifier."
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +25; __Ref__: +21; __Will__: +21"
hp: 210
health:
  - name: "HP"
    desc: "210"
speed: "20 feet, swim 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 (reach 20 feet) __Damage__ 3d10+14 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +27 (Agile, reach 30 feet) __Damage__ 2d10+14 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ water spout +25 (Brutal, range increment 100 feet, Water) __Damage__ 2d6+12 bludgeoning plus sea serpent algae"
abilities_bot:
  - name: "Capsize"
    desc: "⬻ (Attack) The sea serpent attempts to capsize an aquatic vessel of its size or smaller that it's adjacent to. It must succeed at an Athletics check with a DC of 35 (reduced by 5 for each size smaller than the sea serpent) or the pilot's Sailing LoreDC, whichever is higher."
  - name: "Constrict"
    desc: "⬻ 1d10+14 bludgeoning, DC 32"
  - name: "Sea Serpent Algae"
    desc: "(Incapacitation, Poison) The water in the ballast organs around the sea serpent's neck is full of psychotropic algae."
  - name: "Saving Throw"
    desc: "DC 34 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "confused and, if flying, spends its first action each turn to descend 20 feet (1 round)"
  - name: "Stage 2"
    desc: "confused and, if flying, descends until reaching the ground or water below (1 round)"
  - name: "Spine Rake"
    desc: "⬺ (Attack) The sea serpent extends the spines along its back and Swims or Strides. Each creature the serpent is adjacent to at any point during its movement takes 4d6+8 slashing damage with a DC 32 basic Reflex save."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Huge, 2d10+6 bludgeoning, Rupture 20 Shipwreck Lairs While an underwater cave will do, sea serpents prefer to “build” lairs by sinking ships. A sea serpent might even create a massive underwater graveyard by crashing several ships in the same location and letting the debris stack up on the ocean floor."
sourcebook: "_Monster Core_, page 299."
```

```encounter-table
name: Sea Serpent
creatures:
  - 1: Sea Serpent
```
