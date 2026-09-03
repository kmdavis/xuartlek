---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ofalth Stampede"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ofalth Stampede"
level: 15
source: "Battlecry!"
aon_id: "creature-3929"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3929"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Ofalth Stampede"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Troop"
trait_03: "Uncommon"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +32, Stealth +28"
abilityMods: [7, 5, 6, 0, 2, 0]
abilities_top:
  - name: "Refuse Pile"
    desc: "When an ofalth stampede is not in danger, they can spend 1 minute settling into a 20-foot pile that looks like a heap of garbage. Until the next time they take an action, the troop gains a +2 circumstance bonus to AC. A creature that enters the area of the garbage heap or interacts with it must attempt a save against the ofalth stampede's stench."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +29; __Ref__: +24; __Will__: +25"
hp: 270
health:
  - name: "HP"
    desc: "270 (4 segments, filth wallow); __Immunities__ disease, poison; __Weaknesses__ area damage 15, splash damage 15"
abilities_mid:
  - name: "Filth Wallow"
    desc: "A trash stampede gains fast healing 10 when in an area with a high concentration of debris or excrement, such as a refuse heap or sewer."
  - name: "Stench"
    desc: "(aura, olfactory) 30 feet, DC 33"
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; troop movement"
abilities_bot:
  - name: "Offal Rain"
    desc: "⬺ The ofalth stampede hurls a tremendous amount of rotting trash, which rains down in a 10-foot burst within 60 feet. All creatures in the area take 4d10 bludgeoning damage (DC 33 basic Reflex save). Creatures that fail the saving throw are also exposed to wretched weeps. When the troop is reduced to 2 segments, the area decreases to a 5-foot burst."
  - name: "Putrid Pummeling"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The ofalths pummel all enemies in a 10-foot emanation, with a DC 33 basic Reflex save. The damage depends on the number of actions. Creatures that fail the saving throw are exposed to wretched weeps. ⬻ 1d12+3 bludgeoning damage ⬺ 3d12+7 bludgeoning damage ⬽ 4d12+10 bludgeoning damage"
  - name: "Wretched Weeps"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 36 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "2d4 persistent bleed every hour and enfeebled 1 (1 day)"
  - name: "Stage 3"
    desc: "2d6 persistent bleed every hour and enfeebled 2 (1 day)"
sourcebook: "_Battlecry!_, page 186."
```

```encounter-table
name: Ofalth Stampede
creatures:
  - 1: Ofalth Stampede
```
