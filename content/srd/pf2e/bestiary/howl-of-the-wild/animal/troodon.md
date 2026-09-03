---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Troodon"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/dinosaur
  - pf2e/creature/trait/medium
statblock: inline
name: "Troodon"
level: 1
source: "Howl of the Wild"
aon_id: "creature-3260"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3260"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Troodon"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
trait_02: "Dinosaur"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [1, 3, 1, -4, 2, 3]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +4; __Ref__: +8; __Will__: +5"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+1 piercing"
  - name: "Melee"
    desc: "⬻ claw +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+1 slashing"
abilities_bot:
  - name: "Mimicry"
    desc: "⬻ The troodon repeats up to twelve words it heard in the last week. If it succeeds at a [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] check against the listeners' Perception DC, the sound is indistinguishable from the original. The troodon can't duplicate voice-based abilities or spells, although it can mimic the verbal sounds of spellcasting."
  - name: "Running Attack"
    desc: "⬺ The troodon Strides and makes a claw Strike at any point during that movement."
sourcebook: "_Howl of the Wild_, page 136."
```

```encounter-table
name: Troodon
creatures:
  - 1: Troodon
```
