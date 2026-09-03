---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Plated Python"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Plated Python"
level: 12
source: "Howl of the Wild"
aon_id: "creature-3286"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3286"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Plated Python"
level: "Creature 12"
size: "Huge"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25"
abilityMods: [7, 4, 6, -3, 6, 3]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +24; __Ref__: +20; __Will__: +22"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrification]]"
speed: "40 feet, burrow 30 feet, climb 30 feet; stone tunnel"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+10 piercing plus GrabMelee [one-action] tail +24 (reach 15 feet)"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d10+10 bludgeoning, DC 32"
  - name: "Crumbling Earth"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The plated python lets its breath sink into the ground, transforming it to brittle stone within a 30-foot emanation. The stone is difficult terrain to all other creatures. Other creatures on the ground in this area when it transforms must succeed at a DC 29 Reflex save or be [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] as the stone beneath them crumbles to rubble. A creature immobilized in this way can [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] normally or use three total Interact actions to dig themself free."
  - name: "Petrify Prey"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Requirements"
    desc: "The plated python has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Trigger"
    desc: "The plated python begins its turn"
  - name: "Effect"
    desc: "The python's breath seeps into the grabbed creature. That creature must attempt a DC 32 Fortitude save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature's body hardens and stiffens, causing it to become [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] for 1 round and Swallowed Whole."
  - name: "Critical Failure"
    desc: "The creature is petrified permanently and Swallowed Whole."
  - name: "Stone Tunnel"
    desc: "When a plated python burrows through ground, it petrifies and destroys the material in front of it, leaving a 5-foot diameter tunnel in its wake. A plated python doesn't need to [[srd/pf2e/compendium/rules-elements/actions/player-core#Squeeze|Squeeze]] to pass through any space at least that wide."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/attack|Attack]]) Large, 3d10+5 acid, Rupture 20; this damage ignores the hardness of [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] creatures."
  - name: "Towering Bite"
    desc: "⬺ The plated python lunges to its full length, making a jaws Strike with a reach of 60 feet. If the Strike hits, its target is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] and pulled to an empty space adjacent to the plated python. The python can attack through any material it can burrow through, leaving a stone tunnel as normal."
sourcebook: "_Howl of the Wild_, page 155."
```

```encounter-table
name: Plated Python
creatures:
  - 1: Plated Python
```
