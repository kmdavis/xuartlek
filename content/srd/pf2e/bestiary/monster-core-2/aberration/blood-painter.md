---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Blood Painter"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Blood Painter"
level: 9
source: "Monster Core 2"
aon_id: "creature-4284"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4284"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Blood Painter"
level: "Creature 9"
size: "Large"
trait_01: "Aberration"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; bloodsense (imprecise) 60 feet, darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Art Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +17, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +19, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [5, 4, 3, 6, 4, 3]
abilities_top:
  - name: "Bloodsense"
    desc: "A blood painter can detect exposed blood as an imprecise sense at the listed range, including from creatures taking [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +19; __Will__: +17"
hp: 155
health:
  - name: "HP"
    desc: "155"
abilities_mid:
  - name: "Easily Fascinated"
    desc: "When subject to a visual illusion with the [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] trait, the blood painter doesn't adjust their degree of success due to the incapacitation trait."
speed: "30 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+8 slashing plus 1d8 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]]"
abilities_bot:
  - name: "Dab"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Requirements"
    desc: "The blood painter is within reach of an enemy taking [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]"
  - name: "Effect"
    desc: "The blood painter touches the creature and applies blood to one of their four claws; the blood remains fresh for 1 minute. The target must succeed at a DC 28 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the blood painter."
  - name: "Paint"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Requirements"
    desc: "The blood painter has fresh blood applied to a claw using Dab"
  - name: "Effect"
    desc: "The blood painter expends the blood on one claw to paint an illusion with the effects of one of the following spells: [[srd/pf2e/compendium/spells/rank-2/illusory-creature|_illusory creature_]], [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|_illusory disguise_]], or [[srd/pf2e/compendium/spells/rank-1/illusory-object|_illusory object_]]. The Paint action gains the traits of the spell it's reproducing, and the blood painter can [[srd/pf2e/compendium/rules-elements/actions/player-core#Sustain|Sustain]] these effects. They use a spell attack modifier of +20 and DC 28 for these effects, which are heightened to 5th rank. If they have fresh blood applied to two or more claws, the blood painter can expend the blood on all of them to instead produce the effects of [[srd/pf2e/compendium/spells/rank-5/cloak-of-colors|_cloak of colors_]] or [[srd/pf2e/compendium/spells/rank-6/vibrant-pattern|_vibrant pattern_]]. Any effects produced by this ability have a +2 status bonus to attack rolls, damage rolls, saving throws, skill checks, and AC against the creature whose blood was used to Paint. That creature also takes a –2 status penalty to [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Perception|Perception]] checks and saves against them. Apocryphal Origins Despite blood painters' mysterious origins, the prevailing theory insists the first one arose from overzealous Shelynites so devoted to their art they ceased eating and sleeping, eventually transforming into [[srd/pf2e/compendium/rules-elements/traits/player-core/aberration|aberrations]] that could feed only on their own art. Some believe it possible to “cure” a blood painter, restoring the accursed creature's original memories and form."
sourcebook: "_Monster Core 2_, page 60."
```

```encounter-table
name: Blood Painter
creatures:
  - 1: Blood Painter
```
