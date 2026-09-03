---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Marsh Giant"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Marsh Giant"
level: 8
source: "Monster Core"
aon_id: "creature-3011"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3011"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Marsh Giant"
level: "Creature 8"
size: "Large"
trait_01: "Amphibious"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Water"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision"
languages: "Aklo, Common, Jotun, Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +15, Nature +15, Religion +17"
abilityMods: [6, 3, 4, 0, 3, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 striking gaff_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +17"
hp: 150
health:
  - name: "HP"
    desc: "150"
speed: "35 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _gaff_ +20 (Magical, reach 10 feet, Trip, versatile P) __Damage__ 2d6+14 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, reach 10 feet) __Damage__ 2d6+14 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spit +20 (Primal, range 60 feet, Water) __Damage__ 5d6 bludgeoning"
abilities_bot:
  - name: "Drowning Hook"
    desc: "⬻ (Primal, Water)"
  - name: "Requirements"
    desc: "A creature is prone within the marsh giant's reach"
  - name: "Effect"
    desc: "The marsh giant uses its gaff to push the creature down as water bubbles up below it. The target becomes submerged in water until they are no longer prone and must hold their breath if they cannot breathe water. They take 4d6 bludgeoning damage (DC 23 basic Fortitude save) and lose 3 rounds worth of air if they fail the save."
  - name: "Twist the Hook"
    desc: "⬺ The marsh giant makes a melee Strike with its gaff. If it hits, it twists and yanks the gaff to knock the target prone and create an awful wound, dealing 2d6 persistent bleed damage to the creature. Gaffs Many marsh giants fight with an oversized gaff—a length of wood with a metal hook affixed to the tip. The giants use them to drown prey as humanoid fishers use them to land fish. A gaff is a common martial weapon in the club group. It deals 1d6 bludgeoning damage and has 1 Bulk. It requires one hand to use and has the trip and versatile P weapon traits. Gaffs are readily available anywhere fishers live, costing 1 gp."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23 - __2nd__ Augury, Mist - __5th__ Mariner's Curse"
sourcebook: "_Monster Core_, page 164."
```

```encounter-table
name: Marsh Giant
creatures:
  - 1: Marsh Giant
```
