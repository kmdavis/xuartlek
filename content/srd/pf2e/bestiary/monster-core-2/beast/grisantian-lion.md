---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grisantian Lion"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Grisantian Lion"
level: 12
source: "Monster Core 2"
aon_id: "creature-4427"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4427"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Grisantian Lion"
level: "Creature 12"
size: "Huge"
trait_01: "Beast"
trait_02: "Primal"
trait_03: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; low-light vision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +22"
abilityMods: [7, 5, 7, -3, 4, -2]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +25; __Ref__: +22; __Will__: +19"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10, physical 10 (except bludgeoning)"
speed: "35 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 __Damage__ 3d10+14 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Blinding Mane"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "Drawing upon the power of their grogrisant ancestor, the grisantian lion focuses and causes their mane to glow with bright light. All creatures within 20 feet must attempt a DC 29 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] until its next turn begins."
  - name: "Failure"
    desc: "The target is blinded for 1 minute."
  - name: "Critical Failure"
    desc: "The target is blinded permanently."
  - name: "Dual Pounce"
    desc: "⬺ The grisantian lion Strides and makes two claw Strikes against the same creature at the end of that movement. Each attack counts against the grisantian lion's multiple attack penalty, but the penalty doesn't increase until after the grisantian lion makes both attacks. If both attacks hit, combine their damage for the purpose of resistances and weaknesses."
  - name: "Rend"
    desc: "⬻ claw. If the grisantian lion Rends after a successful Dual Pounce, combine the Rend's damage with that from the Dual Pounce for the purpose of resistances and weaknesses."
  - name: "Vicious Rend"
    desc: "⬲"
  - name: "Trigger"
    desc: "The grisantian lion uses Rend"
  - name: "Effect"
    desc: "The target's armor takes damage equal to the damage from Rend. The target can attempt a DC 29 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save to reduce this damage. The Legend Of The Grogrisant Early tales of the founding of Taldor speak of the Grogrisant, an enormous six-eyed lion with a mane that glowed the like the sun. The lion destroyed the city-states of the region, feeding on their livestock and plundering their wealth to line its den. The great hero Taldaris finally slew the terrible beast and went on to become the First Emperor of Taldor. Terrifying six-eyed lions reminiscent of the original make repeated appearances throughout Taldor’s history only to meet their demise at the hands of heroes. While the original Grogrisant of legend is honored with a capitalized name, the remaining grogrisants of history bear the less formal name for the sake of classification."
sourcebook: "_Monster Core 2_, page 180."
```

```encounter-table
name: Grisantian Lion
creatures:
  - 1: Grisantian Lion
```
