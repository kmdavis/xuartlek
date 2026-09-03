---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tripkee Camoufleur"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/tripkee
  - pf2e/creature/trait/small
statblock: inline
name: "Tripkee Camoufleur"
level: 2
source: "NPC Core"
aon_id: "creature-3674"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3674"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tripkee Camoufleur"
level: "Creature 2"
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "Common, Tripkee"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Athletics +5, Crafting +7, Nature +7, Stealth +11, Survival +7"
abilityMods: [1, 4, 1, 1, 3, 0]
abilities_top:
  - name: "Camouflage Specialist"
    desc: "For encounters involving avoiding detection or hiding an object or creature, the camoufleur is a 5th-level challenge."
  - name: "Natural Disguise"
    desc: "The camoufleur can use their disguise kit to disguise a creature or object as natural flora. A creature gains a +2 item bonus to Stealth checks while in a natural environment until its next daily preparations or until its disguise is ruined, whichever comes first. An object in a natural environment can be found only by actively searching (using the Search activity while exploring or the Seek action in an encounter) and uses the camoufleur's Stealth DC."
  - name: "Items"
    desc: "darts (5), Disguise Kit, Hand Adze, Leather Armor"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +5; __Ref__: +11; __Will__: +8"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet, climb 20 feet; forest passage"
attacks:
  - name: "Melee"
    desc: "⬻ hand adze +10 (Agile, Finesse, Sweep) __Damage__ 1d4+3 slashing"
  - name: "Melee"
    desc: "⬻ fist +10 (Agile, Finesse, Nonlethal) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +10 (Agile, thrown 20 feet) __Damage__ 1d4+3 piercing"
  - name: "Ranged"
    desc: "⬻ hand adze +10 (Agile, Sweep, thrown 10 feet) __Damage__ 1d4+3 slashing"
abilities_bot:
  - name: "Forest Passage"
    desc: "The tripkee ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
sourcebook: "_NPC Core_, page 214."
```

```encounter-table
name: Tripkee Camoufleur
creatures:
  - 1: Tripkee Camoufleur
```
