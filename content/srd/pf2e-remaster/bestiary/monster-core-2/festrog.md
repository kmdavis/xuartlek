---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Festrog"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/medium
statblock: inline
name: "Festrog"
level: 1
source: "Monster Core 2"
aon_id: "creature-4399"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4399"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Festrog"
level: "Creature 1"
size: "Medium"
trait_01: "Undead"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Athletics +6, Stealth +7, Survival +5"
abilityMods: [4, 2, 2, 0, 1, 1]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +7; __Will__: +6"
hp: 25
health:
  - name: "HP"
    desc: "25 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, sleep, unconscious"
abilities_mid:
  - name: "Diseased Pustules"
    desc: "(disease, poison) Whenever the festrog takes piercing or slashing damage, creatures adjacent to the festrog take 1d4 poison damage (DC 14 basic Reflex save)."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ claw +9 (Agile) __Damage__ 1d4+4 slashing plus Grab"
abilities_bot:
  - name: "Feast"
    desc: "⬻ (Manipulate)"
  - name: "Requirements"
    desc: "The festrog's last action was a jaws Strike that damaged a living creature"
  - name: "Effect"
    desc: "The festrog tears into the creature's flesh and gulps it down voraciously, dealing 1d4 slashing damage to the creature and gaining temporary Hit Points equal to the damage dealt. These temporary HP last for 1 minute."
  - name: "On All Fours"
    desc: "⬻"
  - name: "Requirements"
    desc: "The festrog has nothing in their hands"
  - name: "Effect"
    desc: "The festrog Strides with a +10-foot circumstance bonus to their Speed. Whispering Hounds Since the fall of Lastwall and the creation of the Gravelands, festrogs have become more common. They prowl the edges of once-peaceful farmlands and often precede a horde of further horrors. Rumors have begun to circulate that the necromancers of the Whispering Way use these creatures as advance scouts to find vulnerable towns and sow terror. As a result, attacks that once would have been dismissed as the predation of wolf packs now evoke a much greater degree of panic."
sourcebook: "_Monster Core 2_, page 155."
```

```encounter-table
name: Festrog
creatures:
  - 1: Festrog
```
