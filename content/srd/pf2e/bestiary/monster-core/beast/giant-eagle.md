---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Eagle"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Giant Eagle"
level: 3
source: "Monster Core"
aon_id: "creature-2969"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2969"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Eagle"
level: "Creature 3"
size: "Large"
trait_01: "Beast"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8"
abilityMods: [3, 4, 1, 0, 2, 2]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +11; __Will__: +9"
hp: 45
health:
  - name: "HP"
    desc: "45"
abilities_mid:
  - name: "Evasive Maneuvers"
    desc: "When a giant eagle rolls a success on a Reflex save, it gets a critical success instead."
speed: "10 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +12 __Damage__ 2d8+5 piercing"
  - name: "Melee"
    desc: "⬻ talon +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d10+5 slashing plus Grab"
abilities_bot:
  - name: "Carry"
    desc: "A giant eagle can [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Fly]] at half Speed while it has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its talons, carrying that creature along with it."
  - name: "Eagle Dive"
    desc: "⬺ The giant eagle [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a talon Strike. Allies in the Skies Aeries of giant eagles can make potent allies to those who respect their territories and approach without malice in their hearts. Giant eagles are just as likely to swoop in and provide unsolicited aid to those in the lowlands of their realm against obvious dangers, but if not offered respect in turn, the eagles may abandon an unpleasant victim to its fate rather than suffer more insults."
sourcebook: "_Monster Core_, page 137."
```

```encounter-table
name: Giant Eagle
creatures:
  - 1: Giant Eagle
```
