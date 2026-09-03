---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Slithering Pit"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Slithering Pit"
level: 7
source: "Monster Core 2"
aon_id: "creature-4552"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4552"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Slithering Pit"
level: "Creature 7"
size: "Medium"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: "Rare"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; no vision, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [7, -5, 7, -5, 0, -5]
abilities_top:
  - name: "Transparent"
    desc: "A slithering pit is so clear it's difficult to spot. A successful DC 30 [[srd/pf2e/books/player-core/chapter-1-introduction/character-creation#Perception|Perception]] check is required to notice a stationary slithering pit, and a creature must be Searching to attempt this check. A creature that walks into the pit's space might fall into any active Dimensional Pit."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +18; __Ref__: +6; __Will__: +11"
hp: 220
health:
  - name: "HP"
    desc: "220; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Critical Hits|critical hits]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Breach Vulnerability"
    desc: "Ingesting an extradimensional space like that found in a spacious pouch deals 6d8 force damage to the slithering pit and its occupants. The slithering pit then immediately uses Out You Go."
speed: "10 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+9 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Dimensional Pit"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/extradimensional|Extradimensional]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) The slithering pit opens an extradimensional, 20-foot-deep pit that covers its own space and all adjacent squares unless they're walls or similar blocking terrain. Any other creature occupying or entering pit spaces must succeed at a DC 22 Reflex save or [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Falling|fall]] into the pit, taking damage from the fall (typically 10 bludgeoning damage). Any creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the slithering pit falls in and is no longer grabbed, even if it was outside the pit squares. While a Dimensional Pit is open, the slithering pit is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], can't be forced to move, and can make pseudopod Strikes originating from the walls of the pit. A creature that starts its turn at the bottom of the pit takes 2d6 acid damage. [[srd/pf2e/compendium/rules-elements/actions/player-core#Climb|Climbing]] the walls of the pit requires a DC 22 [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check. When the slithering pit dies, the Dimensional Pit closes and creatures inside are ejected, with the effects of Out You Go."
  - name: "Flurry of Pods"
    desc: "⬺ The slithering pit makes a single pseudopod Strike against each target within range it doesn't already have [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]. These attacks count toward the slithering pit's multiple attack penalty, but the penalty doesn't increase until after all of these attacks."
  - name: "Out You Go"
    desc: "⬻ The slithering pit closes all pit spaces it created using Dimensional Pit, ejecting all its occupants onto the ground into random free spaces where the pit opened. Each occupant takes 4d6 bludgeoning damage (DC 22 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A Living Pit, Really? Slithering pit lore is as strange and confusing as the creature itself. Was it created by a [[srd/pf2e/compendium/rules-elements/traits/player-core/wizard|wizard]] in need of a handy garbage disposal? Did it result from some unfortunate accident involving hungry [[srd/pf2e/compendium/gm/creature-families/ooze|oozes]] and one spacious pouch too many? Why do its insides mimic the appearance of stone, but without the same toughness? Is it some form of camouflage, letting them pass for an oftignored hazard? So many questions..."
sourcebook: "_Monster Core 2_, page 293."
```

```encounter-table
name: Slithering Pit
creatures:
  - 1: Slithering Pit
```
