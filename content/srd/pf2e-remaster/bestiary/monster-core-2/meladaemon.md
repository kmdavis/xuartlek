---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Meladaemon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Meladaemon"
level: 11
source: "Monster Core 2"
aon_id: "creature-4305"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4305"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Meladaemon"
level: "Creature 11"
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, lifesense (imprecise) 30 feet"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +21, Deception +23, Intimidation +23, Religion +20, Stealth +23, Survival +19"
abilityMods: [7, 5, 6, 3, 4, 6]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +23; __Ref__: +20; __Will__: +19 +1 status to all saves vs. magic"
hp: 225
health:
  - name: "HP"
    desc: "225; __Immunities__ death effects; __Weaknesses__ holy 10"
abilities_mid:
  - name: "Consumptive Aura"
    desc: "(aura, divine) 20 feet. A meladaemon emanates an aura of intense hunger. Each round a creature begins its turn in the aura, it must attempt a DC 27 Fortitude save. On a failure, the creature takes 1d6 void damage (2d6 on a critical failure) and becomes fatigued. This fatigue ends as soon as the creature eats any food."
  - name: "Withering Opportunity"
    desc: "⬲"
  - name: "Trigger"
    desc: "The meladaemon is attacked by an adjacent creature, and the attack misses"
  - name: "Effect"
    desc: "The meladaemon swipes at the triggering creature, which must immediately attempt a save against the meladaemon's withering touch."
speed: "25 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 (Magical, reach 10 feet, unholy) __Damage__ 2d12+16 plus daemonic famine"
  - name: "Melee"
    desc: "⬻ claw +24 (Agile, magical, reach 10 feet, unholy) __Damage__ 2d8+16 slashing plus Grab and withering touch"
abilities_bot:
  - name: "Daemonic Famine"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 29 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "enfeebled 1 (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 2 (1 day)"
  - name: "Stage 4"
    desc: "as stage 3"
  - name: "Stage 5"
    desc: "enfeebled 3 (1 week)"
  - name: "Stage 6"
    desc: "dead"
  - name: "Withering Touch"
    desc: "(Divine, unholy) When the meladaemon hits with a claw Strike or a creature begins its turn grabbed or restrained by the meladaemon, the creature must attempt a DC 30 Fortitude save. On a failure, the creature takes 1d6 void damage and becomes fatigued. This fatigue ends when the creature drinks. Formed In His Image Meladaemons have always been gaunt and bestial, but they didn't always resemble jackals. When Trelmarixian overthrew the previous Apocalypse Rider of Famine, one of his first acts as a ruler of Abaddon was to forcibly twist the appearance of his deacon caste to resemble his own wicked form. He went on to imbue meladaemons with other jackal-like aspects as it suited him, further warping them and cementing their fealty."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31 - __4th__ Translocate (at will) - __5th__ Translocate, Fear, Force Barrage (at will) - __6th__ Phantom Pain"
  - name: "Rituals"
    desc: "DC 31 - __4th__ Blight"
sourcebook: "_Monster Core 2_, page 79."
```

```encounter-table
name: Meladaemon
creatures:
  - 1: Meladaemon
```
