---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Carnivorous Blob"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/ooze
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Carnivorous Blob"
level: 13
source: "Monster Core 2"
aon_id: "creature-4499"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4499"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Carnivorous Blob"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Ooze"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; motion sense 240 feet, no vision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27"
abilityMods: [8, -3, 6, -5, 0, -5]
abilities_top:
  - name: "Motion Sense"
    desc: "A carnivorous blob can sense nearby creatures through vibration and air or water movement."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +25; __Ref__: +14; __Will__: +19"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Critical Hits|critical hits]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], piercing, precision, slashing, [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Split"
    desc: "When a carnivorous blob that has 10 or more HP is hit by an attack that would deal piercing or slashing damage, it splits into two identical oozes, each with half the original's HP. One ooze is in the same space as the original, and the other is in an adjacent, unoccupied space. If no adjacent space is unoccupied, it automatically pushes creatures and objects out of the way to fill a space (the GM decides if an object or creature is too big or heavy to push)."
  - name: "Retaliating Strike"
    desc: "⬲"
  - name: "Trigger"
    desc: "The carnivorous blob takes damage from any source"
  - name: "Effect"
    desc: "The blob makes a pseudopod Strike against an adjacent target. If an adjacent creature dealt the triggering damage, that creature is the target of this Retaliating Strike."
speed: "20 feet, climb 20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pseudopod +25 __Damage__ 2d12+12 bludgeoning plus 2d6 acid and Grab"
abilities_bot:
  - name: "Carnivorous Blob Acid"
    desc: "A carnivorous blob's acid damages only flesh—not bone, stone, wood, or other materials— but is nonetheless devastating. Whenever a creature takes damage from this acid, it must succeed at a DC 33 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (drained 2 on a critical failure). On each subsequent failure, the drained condition value increases by 1 (or by 2 on a critical failure), to a maximum of drained 4."
  - name: "Constrict"
    desc: "⬻ 2d12 bludgeoning plus 2d6 acid, DC 33"
  - name: "Engulf"
    desc: "⬺ DC 33, 4d10 acid, [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 33, Rupture 20"
sourcebook: "_Monster Core 2_, page 243."
```

```encounter-table
name: Carnivorous Blob
creatures:
  - 1: Carnivorous Blob
```
