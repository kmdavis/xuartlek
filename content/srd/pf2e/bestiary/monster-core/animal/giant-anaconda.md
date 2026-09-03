---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Anaconda"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Giant Anaconda"
level: 8
source: "Monster Core"
aon_id: "creature-3203"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3203"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Anaconda"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision, scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [7, 3, 6, -4, 3, -2]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +20; __Ref__: +17; __Will__: +15"
hp: 175
health:
  - name: "HP"
    desc: "175"
abilities_mid:
  - name: "Tighten Coils"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] by the python attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]]"
  - name: "Effect"
    desc: "The DC of the Escape check is increased by 2."
speed: "30 feet, climb 30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+7 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+7 bludgeoning plus Push 10 feet"
abilities_bot:
  - name: "Greater Constrict"
    desc: "⬻ 1d10+7 bludgeoning, DC 26"
  - name: "Slither"
    desc: "⬻ The giant anaconda Strides, [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climbs]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swims]] up to half its Speed, pulling any creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] with it."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 1d10+7 bludgeoning, Rupture 21"
  - name: "Wrap in Coils"
    desc: "⬻"
  - name: "Requirements"
    desc: "A Large or smaller creature is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in the giant anaconda's jaws"
  - name: "Effect"
    desc: "The giant anaconda moves the creature into its coils, freeing its jaws to make attacks, then uses Greater Constrict against the creature. The giant anaconda's coils can hold as many creatures as will fit in its space."
sourcebook: "_Monster Core_, page 317."
```

```encounter-table
name: Giant Anaconda
creatures:
  - 1: Giant Anaconda
```
