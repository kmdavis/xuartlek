---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hippopotamus Topiary"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/huge
statblock: inline
name: "Hippopotamus Topiary"
level: 11
source: "Monster Core 2"
aon_id: "creature-4466"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4466"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hippopotamus Topiary"
level: "Creature 11"
size: "Huge"
trait_01: "Plant"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; branchlocation (precise) 30 feet, low-light vision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +23"
abilityMods: [7, 4, 4, -2, 0, 3]
abilities_top:
  - name: "Branchlocation"
    desc: "The hippopotamus topiary can tap its branches together and use its hearing as a precise sense at the listed range."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +24; __Ref__: +21; __Will__: +18"
hp: 220
health:
  - name: "HP"
    desc: "220; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 14"
speed: "25 feet, swim 30 feet; walk through plants"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 __Damage__ 2d10+15 piercing plus Grab and swamp fever"
  - name: "Melee"
    desc: "⬻ hoof +22 __Damage__ 2d8+15 bludgeoning"
abilities_bot:
  - name: "Absorb Water"
    desc: "When in water or exposed to a [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] effect, the hippopotamus loses its weakness to [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] until the start of its next turn."
  - name: "Jaw Crush"
    desc: "⬻"
  - name: "Requirements"
    desc: "The hippopotamus topiary has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "It forcefully bites down on whatever is in its mouth, dealing 6d8 piercing damage with a DC 27 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. On a critical failure, creatures take 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]."
  - name: "Pruning"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The hippopotamus topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Huge or smaller animal. Until the next time it acts, the topiary has an automatic result of 42 for [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to appear as a mundane topiary."
  - name: "Swamp Fever"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude; Onset 1 day"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 (1 day)"
  - name: "Stage 2"
    desc: "sickened 2 (1 day)"
  - name: "Stage 3"
    desc: "sickened 2 and 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] (1 day)"
  - name: "Stage 4"
    desc: "sickened 2, [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1, and 2d8 persistent bleed damage (1 day)"
  - name: "Stage 5"
    desc: "dead"
sourcebook: "_Monster Core 2_, page 215."
```

```encounter-table
name: Hippopotamus Topiary
creatures:
  - 1: Hippopotamus Topiary
```
