---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hound Topiary"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/medium
statblock: inline
name: "Hound Topiary"
level: 3
source: "Monster Core 2"
aon_id: "creature-4464"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4464"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hound Topiary"
level: "Creature 3"
size: "Medium"
trait_01: "Plant"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision, scent (imprecise) 40 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [4, 2, 3, -2, 0, 3]
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +12; __Ref__: +9; __Will__: +6"
hp: 50
health:
  - name: "HP"
    desc: "50; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
speed: "30 feet; walk through plants"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +10 __Damage__ 1d8+6 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+6 slashing"
abilities_bot:
  - name: "Pruning"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]]) The hound topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Medium or smaller animal. Until the next time it acts, the topiary has an automatic result of 30 for [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to appear as a mundane topiary."
  - name: "Pack Attack"
    desc: "The hound topiary deals an extra 1d6 damage to any creature within reach of at least two of its allies."
  - name: "Walk Through Plants"
    desc: "The hound topiary [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Ignore Difficult Terrain|ignores difficult terrain]] caused by dense vegetation."
  - name: "Warning Howl"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Trigger"
    desc: "The hound topiary rolls for [[srd/pf2e/books/player-core/chapter-1-introduction/playing-the-game#Initiative|initiative]] using [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]]"
  - name: "Effect"
    desc: "The hound shifts to life and howls, though without breath, no sound comes from its mouth. Creatures within 30 feet must attempt a DC 17 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] 1. They're then immune to all hound topiaries' Warning Howls for 1 hour. Topiary Packs Hound topiaries live communally in their chosen wild areas, mostly mimicking the typical actions of canine packs. However, when they come across someone dying and alone, hound topiaries encircle the body, offering comfort in their last moments. Once the soul has passed, the pack will raise their heads in an eerie, silent howl of mourning and remembrance."
sourcebook: "_Monster Core 2_, page 214."
```

```encounter-table
name: Hound Topiary
creatures:
  - 1: Hound Topiary
```
