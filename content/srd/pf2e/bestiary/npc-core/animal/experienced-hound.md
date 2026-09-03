---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Experienced Hound"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/medium
statblock: inline
name: "Experienced Hound"
level: 7
source: "NPC Core"
aon_id: "creature-3678"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3678"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Experienced Hound"
level: "Creature 7"
size: "Medium"
trait_01: "Animal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [5, 5, 4, -4, 2, 0]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +14; __Will__: +12"
hp: 115
health:
  - name: "HP"
    desc: "115"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 __Damage__ 2d6+9 piercing plus Knockdown"
abilities_bot:
  - name: "Drag"
    desc: "⬻"
  - name: "Requirements"
    desc: "The experienced hound is adjacent to a [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] creature"
  - name: "Effect"
    desc: "The experienced hound attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] the prone creature. The experienced hound can then Step away from the target; if the target is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the hound, it is moved into the hound's previous square and remains grabbed."
  - name: "Humane Bite"
    desc: "The experienced hound doesn't take a penalty to make a [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attack with its jaws."
  - name: "Pack Attack"
    desc: "The hound's Strikes deal 2d6 extra damage to creatures within the reach of at least two of the hound's allies."
sourcebook: "_NPC Core_, page 219."
```

```encounter-table
name: Experienced Hound
creatures:
  - 1: Experienced Hound
```
