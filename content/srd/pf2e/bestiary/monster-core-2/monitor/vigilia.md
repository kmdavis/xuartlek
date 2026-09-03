---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vigilia"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Vigilia"
level: 11
source: "Monster Core 2"
aon_id: "creature-4013"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4013"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vigilia"
level: "Creature 11"
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|_see the unseen_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Utopian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/lore|Legal Lore]] +17"
abilityMods: [7, 3, 5, 2, 5, -1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +18; __Will__: +20"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ disease, [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 10"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) __Damage__ 2d10+10 bludgeoning plus 1d10 electricity"
abilities_bot:
  - name: "Electrical Purge"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) The vigilia releases lightning from their body in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] dealing 4d10 electricity damage (DC 30 basic Reflex save) to all creatures that aren't [[srd/pf2e/compendium/rules-elements/traits/gm-core/aeon|aeons]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/construct|constructs]]. The vigilia is then [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round."
  - name: "Lightning Chain"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|Electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]]) The vigilia wraps momentary chains of electrical energy around a creature within 60 feet, dealing 2d10 electricity damage (DC 30 basic Reflex save). A creature that fails its save is also pulled 10 feet toward the vigilia (20 feet on a critical failure)."
  - name: "Take Prisoner"
    desc: "⬻ The vigilia [[srd/pf2e/compendium/rules-elements/actions/player-core#Interact|Interacts]] to pick up a Medium or smaller [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] creature within its reach, then [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]]."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30 - __Constant (2nd)__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]]"
sourcebook: "_Monster Core 2_, page 11."
```

```encounter-table
name: Vigilia
creatures:
  - 1: Vigilia
```
