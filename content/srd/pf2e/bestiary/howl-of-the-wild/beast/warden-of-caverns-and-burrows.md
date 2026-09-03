---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Warden of Caverns and Burrows"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Warden of Caverns and Burrows"
level: 22
source: "Howl of the Wild"
aon_id: "creature-3325"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3325"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Warden of Caverns and Burrows"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Earth"
trait_03: "Unique"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, tremorsense (imprecise) 60 feet"
languages: "voice of nature"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +42, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +37, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +37, [[srd/pf2e/compendium/rules-elements/skills/lore|Subterranean Lore]] +35"
abilityMods: [12, 8, 10, 6, 8, 9]
abilities_top:
  - name: "Voice of Nature"
    desc: ""
  - name: "Warden's Crown"
    desc: ""
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +39; __Ref__: +36; __Will__: +33 +1 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 500
health:
  - name: "HP"
    desc: "500; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 10 (except adamantine), [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] 20; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 20"
abilities_mid:
  - name: "Magmatic Reflex"
    desc: "⬲"
  - name: "Trigger"
    desc: "The warden is targeted with an [[srd/pf2e/compendium/rules-elements/traits/player-core/attack|attack]]"
  - name: "Effect"
    desc: "The warden issues a spray of magma as they jump away from danger. This spray deals 6d12 fire damage to all adjacent creatures (DC 42 basic Reflex save). They then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leap]] or Step away, gaining a +2 circumstance bonus to their AC against the triggering attack."
speed: "40 feet, burrow 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horned crown +41 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 4d12+22 piercing"
  - name: "Melee"
    desc: "⬻ mandible +41 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 4d10+22 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ chirp +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 60 feet) __Damage__ 4d10+18 sonic"
  - name: "Ranged"
    desc: "⬻ magma jet +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet) __Damage__ 4d8+13 fire plus 2d6 persistent fire plus Obsidian Cage"
abilities_bot:
  - name: "Bury Beneath Stone"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Requirements"
    desc: "The warden has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The warden attempts to wedge a creature they have grabbed in their mandibles within a crack in the earth that opens beneath them. The warden attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the grabbed creature's Reflex DC. If they succeed, they bury the creature in the ground. The creature takes 10d10 bludgeoning damage. It is also [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]], [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]], and has to hold its breath or start [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Mounted Defenses|suffocating]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 42). If the creature is still buried at the end of its turn, it takes 5d10 bludgeoning damage."
  - name: "Called to Depths"
    desc: "The depths call to the warden, especially as they move through the air. When they [[srd/pf2e/compendium/rules-elements/actions/player-core#Long Jump|Long Jump]], they can use any unused movement from the Long Jump to [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]]. Additionally, the warden can Burrow through any earthen matter, including rock. When they do so, they move at their full burrow Speed."
  - name: "Erupting Jump"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The warden draws out a stream of lava, then jumps off the solidifying mass as it cools. The warden [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] up to twice their Speed. When they land, the force of the impact deals 6d12 bludgeoning damage to all creatures within a 15-foot emanation with a DC 42 basic Fortitude save. On a critical failure, the creature is also pushed 10 feet away from the warden."
  - name: "Obsidian Cage"
    desc: "Rapidly cooling obsidian clings to the target's body and stiffens around their limbs. The target must attempt a DC 42 Reflex save. On a failure, the target is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until they [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] (DC 42). On a critical failure, the target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] for as long as they remain immobilized."
  - name: "Vibratory Excavation"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The warden screeches with a resonant call that tears apart earth and stone. They create a 10-foot-square, 50-foot-deep pit in earthen material or stone within 60 feet."
  - name: "Wall Cling"
    desc: "The Warden of Caverns and Burrows clings to surfaces with their segmented feet. They do not need to use a hand to hold on to walls or ceilings."
sourcebook: "_Howl of the Wild_, page 203."
```

```encounter-table
name: Warden of Caverns and Burrows
creatures:
  - 1: Warden of Caverns and Burrows
```
