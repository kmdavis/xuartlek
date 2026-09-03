---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wemmuth"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/huge
statblock: inline
name: "Wemmuth"
level: 15
source: "Monster Core 2"
aon_id: "creature-4616"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4616"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wemmuth"
level: "Creature 15"
size: "Huge"
trait_01: "Plant"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +29, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +28, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +30, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +27"
abilityMods: [8, 6, 6, -2, 4, 2]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +27; __Ref__: +27; __Will__: +24"
hp: 335
health:
  - name: "HP"
    desc: "335; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20, slashing 15"
speed: "25 feet, burrow 25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ vine +29 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d12]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]]) __Damage__ 4d12+10 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ boulder +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d12]], range increment 60 feet) __Damage__ 4d10+10 bludgeoning"
abilities_bot:
  - name: "Blood Leech"
    desc: "Trigger__ The wemmuth deals damage to a creature with Constrict__ ⬲"
  - name: "Effect"
    desc: "The wemmuth heals a number of Hit Points equal to half the total damage dealt by Constrict."
  - name: "Constrict"
    desc: "⬻ 2d12+10 bludgeoning, DC 36"
  - name: "Engulf"
    desc: "⬺ DC 36, 4d8 bludgeoning, [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 33, Rupture 36"
  - name: "Thorny Mass"
    desc: "Whenever a creature within 10 feet attempts a melee attack against a wemmuth or uses [[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumble Through]] its space, that creature takes 1d12+10 piercing damage (DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Wemmuth Treasure Wemmuths have little interest in using magical items or accumulating treasure out of a sense of greed, but they are smart enough to understand that a few well-placed trinkets and baubles work amazingly well as lures"
sourcebook: "_Monster Core 2_, page 354."
```

```encounter-table
name: Wemmuth
creatures:
  - 1: Wemmuth
```
