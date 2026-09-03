---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sewer Ooze"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/medium
statblock: inline
name: "Sewer Ooze"
level: 1
source: "Monster Core"
aon_id: "creature-3125"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3125"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sewer Ooze"
level: "Creature 1"
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; motion sense (precise) 60 feet, no vision"
skills:
  - name: "Skills"
    desc: "Stealth +1"
abilityMods: [2, -5, 4, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A sewer ooze can feel nearby motion through vibration and air movement."
ac: 8
armorclass:
  - name: "AC"
    desc: "8; __Fort__: +9; __Ref__: +1; __Will__: +3"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ acid, bleed, critical hits, mental, precision, unconscious, visual"
speed: "10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +9 __Damage__ 1d6+1 bludgeoning plus 1d4 acid"
abilities_bot:
  - name: "Filth Wave"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The sewer ooze unleashes a wave of filth, covering all creatures in a 20-foot emanation. Each creature in the area must succeed at a DC 17 Reflex save or take 1d4 acid damage and take a –10-foot penalty to its Speeds for 1 minute (on a critical failure, the creature also falls prone). A creature can spend an Interact action to clean someone off, decreasing the Speed penalty by 5 feet with each action."
sourcebook: "_Monster Core_, page 256."
```

```encounter-table
name: Sewer Ooze
creatures:
  - 1: Sewer Ooze
```
