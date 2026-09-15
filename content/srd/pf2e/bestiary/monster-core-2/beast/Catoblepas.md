---
noteType: pf2eMonster
aliases: "Catoblepas"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Catoblepas"
level: 12
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4293"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Catoblepas"
level: "Creature 12"
size: "Large"
trait_01: "Beast"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +20"
abilityMods: [7, 4, 6, -2, 4, 2]
abilities_top:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Olfactory|olfactory]]) 30 feet. A creature entering the aura or starting its turn in the aura must succeed at a DC 30 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 (plus [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 for as long as it's sickened on a critical failure). While within the aura, affected creatures take a –2 circumstance penalty to saves against [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]] and to recover from the sickened condition. A creature that succeeds at its save is temporarily immune for 1 minute."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +22"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Olfactory|olfactory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]"
abilities_mid:
  - name: "Ferocity"
    desc: "⬲"
speed: "35 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d10+13 piercing"
  - name: "Melee"
    desc: "⬻ antler +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d12+13 piercing"
  - name: "Melee"
    desc: "⬻ hoof +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d10+11 bludgeoning"
abilities_bot:
  - name: "Poison Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) The catoblepas breathes a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Cone|cone]] of horrid fumes, dealing 13d6 poison damage (DC 32 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Checks#Basic Saving Throws|basic]] Fortitude save). The area of this cone is reduced to 30 feet underwater. Targets that fail their saving throw also become [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]] 1 (sickened 2 on a critical failure). The catoblepas can't use its Poison Breath again for 1d4 rounds."
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 32 Catoblepas Nests A catoblepas den is an awful place indeed—a filthy nest composed of piles of decaying vegetation, half-finished or half-digested meals of rotting animals, never-quite-dry banks of mud, and tangles of thorny branches. Worse yet, the catoblepas’s stink infuses such a site, imposing the beast’s ungodly stench upon those who would explore and search it for treasure. A catoblepas nest can retain its stink in this way for up to a week after it’s been abandoned by its foul denizen."
sourcebook: "_Monster Core 2_, page 69."
```

```encounter-table
name: Catoblepas
creatures:
  - 1: Catoblepas
```
