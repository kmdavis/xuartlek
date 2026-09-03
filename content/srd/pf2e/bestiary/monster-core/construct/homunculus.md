---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Homunculus"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/tiny
statblock: inline
name: "Homunculus"
level: 0
source: "Monster Core"
aon_id: "creature-3056"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3056"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Homunculus"
level: "Creature 0"
size: "Tiny"
trait_01: "Construct"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
languages: "Common; (can't speak any language); master link"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Stealth +5"
abilityMods: [-1, 3, 0, 0, 1, -2]
abilities_top:
  - name: "Master Link"
    desc: "(arcane, mental) A homunculus can't speak, but it is telepathically linked to its creator. It can share information back and forth, including its master's knowledge and everything the homunculus hears. The range of this link is 1,500 feet. The homunculus typically has a similar attitude to its creator and is utterly faithful. If the homunculus is destroyed, the master takes 2d10 mental damage. If the master is slain, the homunculus becomes mindless, claims its current location as its lair, and instinctively attacks anyone who comes near."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +2; __Ref__: +7; __Will__: +3"
hp: 17
health:
  - name: "HP"
    desc: "17; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void"
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 (Finesse, Magical, reach 0 feet) __Damage__ 1d4 piercing plus homunculus poison"
abilities_bot:
  - name: "Homunculus Poison"
    desc: "(Poison) A homunculus has one dose of poison in a reservoir in its head. It can refill this poison from its reserves with an Interact action"
  - name: "Saving Throw"
    desc: "DC 15 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and enfeebled 1 (1 round). Soulbound Homunculi Most homunculi use a dose of their creator's blood as their spark of life, but it's possible to use a technique similar to that used in the crafting of a soulbound doll to give a homunculus a personality and the semblance of life. These homunculi gain the soulbound trait, lose immunity to spirit, can speak, and do not have a special link to a creator, yet the process tends to warp the soul used so that, more often than not, what rises in the new homunculus body is a parody of its prior life. As such, soulbound homunculi are generally created by cruel spellcasters as a method of humiliating and tormenting vanquished enemies."
sourcebook: "_Monster Core_, page 200."
```

```encounter-table
name: Homunculus
creatures:
  - 1: Homunculus
```
