---
noteType: pf2eMonster
aliases: "Snapdrake"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Snapdrake"
level: 8
source: "Rage of Elements"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2677"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Snapdrake"
level: "Creature 8"
size: "Large"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 16
perception:
  - name: "Perception"
    desc: "+16"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Muan|Muan]]; (can't speak any languages)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +16, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +14"
abilityMods: [4, 6, 3, -2, 3, 4]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +11; __Will__: +19"
hp: 144
health:
  - name: "HP"
    desc: "144; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/Weapon Groups#Axe|axes]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10"
abilities_mid:
  - name: "Alluring Scent"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Olfactory|olfactory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) 30 feet. A creature that enters the emanation must attempt a DC 25 Will save. On a failure, the target is [[srd/pf2e/compendium/rules-elements/Conditions#Fascinated|fascinated]] by the snapdrake and must use at least 1 action on its next turn to Stride closer to the snapdrake. On a success, the target is immune to the snapdrake's alluring scent for 1 hour."
  - name: "Reactive Strike"
    desc: "⬲ Tail scythe only"
speed: "20 feet, fly 50 feet; greater forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +14 __Damage__ 2d12+4 piercing plus Grab and snapdrake pollen"
  - name: "Melee"
    desc: "⬻ tail scythe +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+6 slashing"
abilities_bot:
  - name: "Greater Forest Passage"
    desc: "The snapdrake ignores difficult terrain and greater difficult terrain from plants and fungi."
  - name: "Snapdrake Pollen"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "8 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage plus dazzled 1 (1 round)"
  - name: "Stage 2"
    desc: "1d6 poison damage plus dazzled 1 and sickened 1 (2 rounds)"
  - name: "Stage 3"
    desc: "2d6 poison damage plus [[srd/pf2e/compendium/rules-elements/Conditions#Confused|confused]] and sickened 1 (2 rounds)"
  - name: "Speed Surge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Move|Move]])"
  - name: "Frequency"
    desc: "3 times per day"
  - name: "Effect"
    desc: "The snapdrake moves up to twice its Speed."
  - name: "Spray Pollen"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]]) The snapdrake breathes a blast of pollen in a 40-foot cone. Creatures caught in the blast must succeed at a DC 25 basic Reflex save or be exposed to snapdrake pollen. The snapdrake can't use Spray Pollen again for 1d6 rounds."
sourcebook: "_Rage of Elements_, page 209."
```

```encounter-table
name: Snapdrake
creatures:
  - 1: Snapdrake
```
