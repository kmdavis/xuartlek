---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Titanosaur"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Titanosaur"
level: 16
source: "Howl of the Wild"
aon_id: "creature-3265"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3265"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Titanosaur"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +34"
abilityMods: [10, 4, 9, -4, 5, 6]
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +33; __Ref__: +28; __Will__: +29"
hp: 370
health:
  - name: "HP"
    desc: "370"
abilities_mid:
  - name: "Majestic Presence"
    desc: "(aura, emotion, visual) 90 feet, DC 38. Creatures of Huge size or smaller that enter the aura must attempt a Will save. Regardless of the result of the saving throw, the creature is temporarily immune to the titanosaur's Majestic Presence for 1 hour."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is fascinated by the titanosaur for 1 round."
  - name: "Failure"
    desc: "The creature is fascinated for 2 rounds."
  - name: "Critical Failure"
    desc: "The creature is fascinated for 1 minute."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +32 (reach 30 feet) __Damage__ 3d8+16 bludgeoning plus Improved Knockdown"
  - name: "Melee"
    desc: "⬻ foot +32 (reach 15 feet) __Damage__ 3d12+16 bludgeoning"
abilities_bot:
  - name: "Seismic Slam"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The titanosaur rears up on its hind legs before slamming its forelegs back on the ground with a thunderous crash, creating a localized tremor with the effects of an _earthquake_ spell centered on itself, though the effect is non-magical. Fissures do not form under the titanosaur."
  - name: "Sweeping Tail"
    desc: "⬺ The titanosaur lashes its tail in a 30-foot cone. Creatures in the area take 8d10 bludgeoning damage (DC 38 basic Reflex save). The momentum of the titanosaur's swing then makes it off-guard until the beginning of its next turn."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 38"
sourcebook: "_Howl of the Wild_, page 138."
```

```encounter-table
name: Titanosaur
creatures:
  - 1: Titanosaur
```
