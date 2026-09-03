---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sportlebore Swarm"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/swarm
  - pf2e/creature/trait/large
statblock: inline
name: "Sportlebore Swarm"
level: 7
source: "Monster Core 2"
aon_id: "creature-4566"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4566"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sportlebore Swarm"
level: "Creature 7"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [2, 6, 4, -4, 2, 4]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +17; __Will__: +13"
hp: 85
health:
  - name: "HP"
    desc: "85; __Immunities__ precision, swarm mind; __Resistances__ bludgeoning 3, piercing 7, slashing 7; __Weaknesses__ area damage 7, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 7"
abilities_mid:
  - name: "Pour Down Throat"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature in the sportlebore swarm's area speaks, Casts a Spell, or opens its mouth"
  - name: "Effect"
    desc: "A portion of the sportlebore swarm attempts to surge down the throat of the triggering creature, who must attempt a DC 25 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature gets a mouthful of sportlebores. They spit the insects out and avoid further damage, but they can't speak for 1 round, and if they were performing a spellcasting action, the spell fails and the caster wastes the action."
  - name: "Failure"
    desc: "The creature takes 4d6 piercing damage from sportlebore bites, can't speak for 1 round, and loses a spell as noted under success."
  - name: "Critical Failure"
    desc: "As failure, but the creature is also exposed to sportlebore infestation."
speed: "35 feet, fly 35 feet"
abilities_bot:
  - name: "Swarming Bites"
    desc: "⬻ Each creature in the sportlebore swarm's area takes 3d6 piercing damage (DC 25 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save)."
  - name: "Sportlebore Infestation"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude"
  - name: "Stage 1"
    desc: "carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 hour)"
  - name: "Stage 3"
    desc: "enfeebled 2 (1 hour)"
  - name: "Stage 4"
    desc: "4d6 bludgeoning damage (DC 25 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save) as the host painfully vomits out a sportlebore swarm and returns to stage 1"
sourcebook: "_Monster Core 2_, page 306."
```

```encounter-table
name: Sportlebore Swarm
creatures:
  - 1: Sportlebore Swarm
```
