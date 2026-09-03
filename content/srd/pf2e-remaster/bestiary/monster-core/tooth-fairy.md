---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tooth Fairy"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/tiny
statblock: inline
name: "Tooth Fairy"
level: -1
source: "Monster Core"
aon_id: "creature-3216"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3216"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tooth Fairy"
level: "Creature -1"
size: "Tiny"
trait_01: "Fey"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Stealth +5, Thievery +6"
abilityMods: [-2, 3, 0, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "pliers"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +2; __Ref__: +7; __Will__: +4"
hp: 8
health:
  - name: "HP"
    desc: "8; __Weaknesses__ cold iron 2"
abilities_mid:
  - name: "Plaque Burst"
    desc: "When killed, a tooth fairy bursts into sticky, foul-smelling white dust. Each creature in a 5-foot emanation must succeed at a DC 16 Fortitude save or become sickened 1 (sickened 2 on a critical failure)."
speed: "10 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pliers +7 (Disarm, Finesse, reach 0 feet) __Damage__ 1d6 bludgeoning plus Tooth Tug"
abilities_bot:
  - name: "Tooth Tug"
    desc: "⬻ (Manipulate)"
  - name: "Requirements"
    desc: "The tooth fairy's last action was a successful pliers Strike against a creature with teeth"
  - name: "Effect"
    desc: "The tooth fairy attempts a Thievery check against the creature's Fortitude DC, dealing 2 persistent bleed damage on any result but a critical failure. On a critical success, it also pulls out one of the target's teeth. If the creature loses a tooth, it takes a –1 status penalty to Charisma-based skill checks and must succeed at a DC 5 flat check to Cast a Spell unless that spell has the subtle trait. These effects last for 1 day, or until the stolen tooth is returned and the target regains at least 1 Hit Point."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 13 - __Cantrips (1st)__ Telekinetic Hand - __1st__ Sleep"
sourcebook: "_Monster Core_, page 327."
```

```encounter-table
name: Tooth Fairy
creatures:
  - 1: Tooth Fairy
```
