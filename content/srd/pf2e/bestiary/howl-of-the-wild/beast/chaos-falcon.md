---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Chaos Falcon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/air
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/electricity
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Chaos Falcon"
level: 10
source: "Howl of the Wild"
aon_id: "creature-3270"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3270"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Chaos Falcon"
level: "Creature 10"
size: "Huge"
trait_01: "Air"
trait_02: "Beast"
trait_03: "Electricity"
trait_04: "Fire"
trait_05: "Rare"
trait_06: "Water"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, stormsight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19"
abilityMods: [5, 7, 3, 4, 4, 3]
abilities_top:
  - name: "Stormsight"
    desc: "Wind, precipitation, and clouds don't impair a chaos falcon's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from storms, mist, precipitation, and the like."
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +19; __Ref__: +22; __Will__: +16"
hp: 180
health:
  - name: "HP"
    desc: "180; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10"
abilities_mid:
  - name: "Storm Nexus"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 15 feet, 3d6 fire, DC 26 basic Reflex save. The chaos falcon is surrounded by a cloud of volcanic ash, lightning arcing within the cloud as it glows hot in some areas and collects ice in others. A chaos falcon can change the damage type of this aura to cold, electricity, or fire as an action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d10+10 piercing"
  - name: "Melee"
    desc: "⬻ talon +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 3d6+10 slashing"
  - name: "Ranged"
    desc: "⬻ bolt +23 (range 120 feet) __Damage__ 6d6 fire plus storm bolt"
abilities_bot:
  - name: "Dive-bomb"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Requirements"
    desc: "The chaos falcon is [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flying]]"
  - name: "Effect"
    desc: "The chaos falcon Flies twice straight down. If they reach the ground or a similarly solid object at the end of this movement, their landing shatters that surface into sharp shards and droplets of molten stone deal 4d6 fire and 3d8 piercing damage (DC 26 basic Reflex save) to all other creatures within 20 feet."
  - name: "Flash Storm"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Water condenses around the ash particles in the chaos falcon's 15-foot aura, pelting everything beneath it with driving rain. Creatures in that area must succeed at a DC 26 Reflex save or be pushed 20 feet down, falling [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] if they start or end this movement on the ground."
  - name: "Storm Bolt"
    desc: "The chaos falcon's bolt Strike always deals the damage type of their storm nexus aura."
sourcebook: "_Howl of the Wild_, page 143."
```

```encounter-table
name: Chaos Falcon
creatures:
  - 1: Chaos Falcon
```
