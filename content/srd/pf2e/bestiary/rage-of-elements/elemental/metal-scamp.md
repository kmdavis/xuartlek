---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Metal Scamp"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/small
statblock: inline
name: "Metal Scamp"
level: 1
source: "Rage of Elements"
aon_id: "creature-2644"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2644"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Metal Scamp"
level: "Creature 1"
size: "Small"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Talican|Talican]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [2, 0, 2, -2, 0, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +5; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20 (fast healing 2 (while touching metal)); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 3"
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 __Damage__ 1d6+2 slashing"
abilities_bot:
  - name: "Breathe Shrapnel"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/metal|Metal]]) The metal scamp breathes a 15-foot cone of jagged metal flakes that deals 2d4 slashing damage and 1d4 persistent bleed damage to each creature within the area (DC 17 basic Reflex save). The metal scamp can't Breathe Shrapnel again for 1d4 rounds."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 17, attack +9 - __2nd__ Magnetic Attraction"
sourcebook: "_Rage of Elements_, page 153."
```

```encounter-table
name: Metal Scamp
creatures:
  - 1: Metal Scamp
```
