---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Iceberg Clam"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Iceberg Clam"
level: 13
source: "Monster Core 2"
aon_id: "creature-4445"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4445"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Iceberg Clam"
level: "Creature 13"
size: "Huge"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, wavesense 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +23, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +30, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +25"
abilityMods: [6, 5, 8, -2, 4, 3]
abilities_top:
  - name: "Watery Body"
    desc: "The iceberg clam can occupy the same space as other creatures and is considered [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] to other creatures."
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +26; __Ref__: +23; __Will__: +20"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Ambush Freeze"
    desc: "⬲"
  - name: "Requirements"
    desc: "The iceberg clam does not have a frozen shell"
  - name: "Trigger"
    desc: "An enemy enters or attempts to leave the clam's space"
  - name: "Effect"
    desc: "The iceberg clam uses Frozen Shell."
speed: "5 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ freezing wave +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) __Damage__ 3d12+10 bludgeoning plus 1d12 cold"
  - name: "Ranged"
    desc: "⬻ icicle +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], range increment 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) __Damage__ 3d12+4 piercing plus 1d12 cold"
abilities_bot:
  - name: "Boil"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "All creatures in the iceberg clam's space take 4d10 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent fire damage]] (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Fortitude save) and if the iceberg clam has a frozen shell, the shell takes 20 fire damage that bypasses [[srd/pf2e/books/player-core/chapter-6-equipment/shields#Hardness|Hardness]]. A creature can't recover from this persistent fire damage while in the iceberg clam's space."
  - name: "Frozen Shell"
    desc: "⬻ The iceberg clam covers itself with a frozen shell. All creatures in the iceberg clam's space can't leave those squares for as long as the frozen shell is in place. The shell has AC 10, [[srd/pf2e/books/player-core/chapter-6-equipment/shields#Hardness|Hardness]] 10, and 60 Hit Points, and it's [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Immunity to Critical Hits|immune to critical hits]] and precision damage. If the iceberg clam moves, all creatures trapped within its shell move with the clam. While an iceberg clam has a frozen shell, any attacks originating from outside the iceberg clam's space must target the shell. The iceberg clam can [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismiss]] its shell. If the iceberg clam does so or the shell is reduced to 0 Hit Points, the iceberg clam can't use Ambush Freeze or Frozen Shell again for 1d4 rounds."
  - name: "Heated Jet"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]])"
  - name: "Requirements"
    desc: "The iceberg clam does not have a frozen shell"
  - name: "Effect"
    desc: "The iceberg clam surges along a jet of superheated water, moving up to 60 feet in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] and dealing 4d10 fire damage to creatures along its path (DC 33 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A Deadly Difference Though they appear inhospitable, mundane icebergs often house vibrant ecosystems teeming with life. Jellyfish and other small invertebrates feed on algae that collects along the bottom; small fish make homes in caves that dot the ice; and seabirds, seals, and even whales sometimes utilize them for shelter or as hunting grounds. Conversely, the sea surrounding an iceberg clam is always devoid of life, as local fauna know to stay away from its ceaseless hunger. While the elemental's cunning camouflage can easily trick the uninformed, canny sailors and marine adventurers know to look for these telltale signs before approaching."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 30 - __4th__ [[srd/pf2e/compendium/spells/rank-4/hydraulic-torrent|Hydraulic Torrent]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/crashing-wave|Crashing Wave]], [[srd/pf2e/compendium/spells/rank-5/wall-of-ice|Wall of Ice]] - __6th__ [[srd/pf2e/compendium/spells/rank-4/ice-storm|Ice Storm]]"
sourcebook: "_Monster Core 2_, page 197."
```

```encounter-table
name: Iceberg Clam
creatures:
  - 1: Iceberg Clam
```
