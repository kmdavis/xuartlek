---
noteType: pf2eMonster
aliases: "Nightmare"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Nightmare"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3105"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nightmare"
level: "Creature 6"
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 14
perception:
  - name: "Perception"
    desc: "+14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], Daemonic, [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +14, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +12"
abilityMods: [6, 3, 3, 1, 4, 2]
abilities_top:
  - name: "Smoke"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]]) 15 feet. The nightmare continually exhales black smoke. Creatures within the aura are [[srd/pf2e/compendium/rules-elements/Conditions#Concealed|concealed]] to those outside it, and creatures outside the aura are concealed to creatures within it. Nightmares and their riders can see through this smoke. A creature that begins its turn in the area must succeed at a DC 23 Fortitude save or be [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 2]]. It's then temporarily immune to being sickened by the smoke for 1 minute. This is an [[srd/pf2e/compendium/rules-elements/traits/gm-core/Inhaled|inhaled]] [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], and the nightmare and its rider are immune to it."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +15; __Will__: +12"
hp: 100
health:
  - name: "HP"
    desc: "100; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10"
speed: "40 feet, fly 90 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ hoof +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d8+8 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Flaming Gallop"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) The nightmare Strides or [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]]up to triple its Speed. Its hooves burst with intense flame, dealing 3d6 fire damage with a DC 24 basic Reflex save to each creature other than the nightmare's rider that the nightmare moves adjacent to during its gallop. Each creature can be affected only once during a single use of Flaming Gallop."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24 - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (self and rider only)"
sourcebook: "_Monster Core_, page 238."
```

```encounter-table
name: Nightmare
creatures:
  - 1: Nightmare
```
