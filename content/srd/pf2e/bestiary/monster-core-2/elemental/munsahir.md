---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Munsahir"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/munsahir
  - pf2e/creature/trait/medium
statblock: inline
name: "Munsahir"
level: 2
source: "Monster Core 2"
aon_id: "creature-4484"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4484"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Munsahir"
level: "Creature 2"
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Humanoid"
trait_04: "Munsahir"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +4, [[srd/pf2e/compendium/rules-elements/skills/lore|Plane of Fire Lore]] +6"
abilityMods: [3, 1, 4, 2, 2, 0]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/hammer/light-hammer|light hammers]] (5), [[srd/pf2e/compendium/equipment/armor#Scale Mail|Scale Mail]], [[srd/pf2e/compendium/equipment/weapons/hammer/warhammer|Warhammer]]"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +10; __Ref__: +5; __Will__: +8"
hp: 40
health:
  - name: "HP"
    desc: "40; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 4"
abilities_mid:
  - name: "Heat of the Forge"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) 10 feet. A munsahir's skin radiates heat like forge fire. A creature that starts its turn in the area must succeed at a DC 16 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] while it remains in the area. Creatures immune to environmental heat effects or with any fire resistance are immune."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d8+3 bludgeoning plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ light hammer +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d6+3 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ light hammer +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 20 feet]]) __Damage__ 1d6+3 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Burning Touch"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The munsahir's Strikes deal an extra 1d6 fire damage (included above). When the munsahir successfully performs a [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]], [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Reposition]], or [[srd/pf2e/compendium/rules-elements/actions/player-core#Shove|Shove]], they also deal 1d6 fire damage to their target."
  - name: "Scorch"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Requirements"
    desc: "The munsahir is wielding a light hammer"
  - name: "Effect"
    desc: "The munsahir shrouds the light hammer in flames and hurls it forward, dealing 2d6 fire damage to each creature in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Munsahirs On Other Planes While the majority of munsahirs live on the [[srd/pf2e/compendium/gm/planes#Plane of Fire|Plane of Fire]], a few groups have emigrated to other planes. On Golarion, a number of large communities exist in the Flume Warrens, part of the Darklands beneath the Mindspin Mountains. Another group has taken up residence under the Five Kings Mountains after a harrowing escape from oppression in Medina Mudii'a. Legends speak of an ancient elemental nation led by an immortal munsahir who ruled a portion of the Valashmai Jungle in Tian Xia, but the fate of this nation is unknown, and few of its ruins remain."
sourcebook: "_Monster Core 2_, page 230."
```

```encounter-table
name: Munsahir
creatures:
  - 1: Munsahir
```
