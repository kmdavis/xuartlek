---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Goblin Dog"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Goblin Dog"
level: 1
source: "Monster Core"
aon_id: "creature-3028"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3028"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Goblin Dog"
level: "Creature 1"
size: "Medium"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +6, Stealth +7"
abilityMods: [3, 2, 2, -4, 1, -1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +8; __Ref__: +8; __Will__: +5"
hp: 17
health:
  - name: "HP"
    desc: "17"
abilities_mid:
  - name: "Irritating Dander"
    desc: "A creature that hits a goblin dog with an unarmed attack, tries to Grapple it, or otherwise touches it is exposed to goblin pox."
  - name: "Buck"
    desc: "⬲ DC 17"
  - name: "Juke"
    desc: "⬲"
  - name: "Requirements"
    desc: "A creature must be mounted on the goblin dog"
  - name: "Trigger"
    desc: "The rider issues a command to the goblin dog"
  - name: "Effect"
    desc: "The goblin dog Steps before following the command."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 1d6+3 piercing plus goblin pox"
abilities_bot:
  - name: "Goblin Pox"
    desc: "(Disease) Goblins and goblin dogs are immune to goblin pox"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Stage 1"
    desc: "sickened 1 (1 round)"
  - name: "Stage 2"
    desc: "sickened 1 and slowed 1 (1 round)"
  - name: "Stage 3"
    desc: "sickened 2 and can't reduce its sickened value below 1 (1 day)"
  - name: "Scratch"
    desc: "⬺ (Manipulate) The goblin dog vigorously scratches itself, exposing all adjacent creatures to goblin pox. Goblin Dog Stories Goblins adore goblin dogs, and crafting stories of their pets' antics is a time-honored tradition among many goblin tribes. Goblins often seek to outdo prior yarns by increasing the audacity, ridiculousness, and surreality of their adventures. Examples include goblin dogs holding fancy dinners in high society among unwitting humans, goblin dogs tainting dwarven ale in unmentionable ways, and goblins who actually transform into something else as a result of a goblin dog bite. This last tale in particular has some truth to it, as credible accounts confirm the existence of goblin dog werecreatures in certain tribes."
sourcebook: "_Monster Core_, page 176."
```

```encounter-table
name: Goblin Dog
creatures:
  - 1: Goblin Dog
```
