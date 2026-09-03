---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Desert Manticore"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Desert Manticore"
level: 12
source: "Howl of the Wild"
aon_id: "creature-3299"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3299"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Desert Manticore"
level: "Creature 12"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Kelish|Kelish]], [[srd/pf2e/compendium/rules-elements/languages#Osiriani|Osiriani]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +22, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22"
abilityMods: [7, 2, 5, -2, 2, 4]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +22; __Will__: +22"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]"
abilities_mid:
  - name: "Indomitable Beast"
    desc: "⬲"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The desert manticore is reduced to 0 HP"
  - name: "Effect"
    desc: "The desert manticore avoids being knocked out and remains at 1 HP, then can make a stinger Strike against a creature in its reach."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +25 __Damage__ 4d8+10 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 4d6+10 slashing"
  - name: "Melee"
    desc: "⬻ stinger +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+10 piercing plus manticore venom"
abilities_bot:
  - name: "Manticore Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "Fortitude DC 32"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d8 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "4d8 poison damage and drained 2 (1 round)"
  - name: "Stage 3"
    desc: "5d8 poison damage and drained 3 (1 round)"
  - name: "Scorpion Sting"
    desc: "⬺ The desert manticore Strikes an [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creature with its stinger. The attack injects venom deeply, dealing an additional 4d8 poison damage and giving the target a –2 circumstance penalty to their initial save against the poison."
  - name: "Venomous Flight"
    desc: "⬺ The desert manticore [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] twice, dripping venom from its stinger. It chooses a creature it flew directly above during the flight, which is exposed to manticore venom. The desert manticore cannot fly further than 60 feet above the target or the venom becomes too dispersed in fall to take effect."
sourcebook: "_Howl of the Wild_, page 172."
```

```encounter-table
name: Desert Manticore
creatures:
  - 1: Desert Manticore
```
