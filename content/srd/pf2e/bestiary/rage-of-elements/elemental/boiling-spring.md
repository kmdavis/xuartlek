---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Boiling Spring"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/water
  - pf2e/creature/trait/large
statblock: inline
name: "Boiling Spring"
level: 13
source: "Rage of Elements"
aon_id: "creature-2661"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2661"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Boiling Spring"
level: "Creature 13"
size: "Large"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Fire"
trait_04: "Water"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, steam vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +26"
abilityMods: [7, 7, 7, 2, 4, 2]
abilities_top:
  - name: "Steam Vision"
    desc: "The boiling spring ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from mist and steam."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +23; __Ref__: +26; __Will__: +20"
hp: 255
health:
  - name: "HP"
    desc: "255; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 15"
abilities_mid:
  - name: "Freeze and Shatter"
    desc: "If the boiling spring is destroyed with cold damage, their body freezes over and explodes, sending out a wave of frigid air and ice shards that deal 4d6 piercing damage plus 4d6 cold damage to creatures in a 20-foot emanation (DC 36 basic Reflex save)."
  - name: "Sweltering Heat"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) 25 feet. The boiling spring radiates heat, raising the air temperature around them. A creature that starts its turn in the emanation must succeed at a DC 33 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] while it remains in the area; creatures immune to environmental heat effects or with any fire resistance are immune."
  - name: "Evaporate"
    desc: "⬲"
  - name: "Trigger"
    desc: "An effect would deal fire damage to the boiling spring, even if they would ignore the damage"
  - name: "Effect"
    desc: "The boiling spring evaporates into the air. Until the beginning of the boiling spring's next turn, they can't be attacked or targeted. They still occupy their space, and their auras still function as normal."
speed: "fly 30 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ blistering fist +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) __Damage__ 3d8+13 fire"
  - name: "Ranged"
    desc: "⬻ heat wave +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], range increment 50 feet) __Damage__ 3d12 fire"
abilities_bot:
  - name: "Scalding Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The boiling spring breathes out a cloud of steam in a 30-foot cone that deals 14d6 fire damage to each creature in the area (DC 33 basic Reflex save). The boiling spring can't use Scalding Breath again for 1d4 rounds."
sourcebook: "_Rage of Elements_, page 181."
```

```encounter-table
name: Boiling Spring
creatures:
  - 1: Boiling Spring
```
