---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Verdure's Moonflower"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Verdure's Moonflower"
level: 8
source: "Dark Archives (Remastered)"
aon_id: "creature-4649"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4649"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "DA"
name: "Verdure's Moonflower"
level: "Creature 8"
size: "Huge"
trait_01: "Plant"
trait_02: "Rare"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "telepathy 1 mile (other moonflowers only) Skills Athletics +19 (can't Jump or Swim), Stealth +14 (+18 in thick vegetation)"
abilityMods: [7, 0, 4, -2, 4, 3]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +10; __Will__: +16"
hp: 120
health:
  - name: "HP"
    desc: "120 (fast healing 10); __Immunities__ electricity; __Resistances__ physical 10 (except slashing); __Weaknesses__ fire 10"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ maw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+10 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ root +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+10 bludgeoning"
abilities_bot:
  - name: "Pod Prison"
    desc: "⭓"
  - name: "Requirements"
    desc: "A creature is swallowed by the moonflower"
  - name: "Effect"
    desc: "The moonflower wraps the swallowed creature in a cocoon and extrudes it into an adjacent square. The creature continues to be Swallowed Whole and takes half damage from any damage dealt to the cocoon. Once the cocoon is Ruptured, it deflates and decays."
  - name: "Pod Spawn"
    desc: "If a Small or larger creature dies within a pod prison, the pod transforms into an adult moonflower with full Hit Points after 1d4 hours of growth. The dead creature's equipment remains inside the new moonflower and can be retrieved if the moonflower is slain."
  - name: "Spray Blossoms"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) The moonflower expels mind-warping petals in a 30-foot cone. Creatures in the area take 4d6 mental damage and 4d6 poison damage (DC 26 basic Will save). A creature that fails is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 for 1 minute, and confused for 1 round if it got a critical failure. The moonflower can't Spray Blossoms again for 1d4 rounds."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 2d10+10 bludgeoning and 2d6 acid, Rupture 21"
sourcebook: "_Dark Archives (Remastered)_, page 153."
```

```encounter-table
name: Verdure's Moonflower
creatures:
  - 1: Verdure's Moonflower
```
