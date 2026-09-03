---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tiger Topiary"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/large
statblock: inline
name: "Tiger Topiary"
level: 5
source: "Monster Core 2"
aon_id: "creature-4465"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4465"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Tiger Topiary"
level: "Creature 5"
size: "Large"
trait_01: "Plant"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [4, 4, 3, -2, 0, 3]
abilities_top:
  - name: "Stalker"
    desc: "When in dense foliage or tall grass, the tiger topiary gains a +1 status bonus to checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]]."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +15; __Ref__: +12; __Will__: +9"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 8"
speed: "40 feet; walk through plants"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d8+7 piercing"
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+7 slashing"
abilities_bot:
  - name: "Pounce"
    desc: "⬻ The tiger topiary [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] and makes a [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]] at the end of that movement. If it began this action [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]], it remains hidden until after this ability's Strike."
  - name: "Pruning"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The tiger topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Large or smaller animal. Until the next time it acts, the topiary has an automatic result of 32 for [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to appear as a mundane topiary."
  - name: "Walk Through Plants"
    desc: "The tiger topiary [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Ignore Difficult Terrain|ignores difficult terrain]] caused by dense vegetation."
sourcebook: "_Monster Core 2_, page 214."
```

```encounter-table
name: Tiger Topiary
creatures:
  - 1: Tiger Topiary
```
