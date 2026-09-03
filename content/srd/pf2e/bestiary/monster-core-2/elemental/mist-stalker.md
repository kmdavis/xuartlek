---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mist Stalker"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/medium
statblock: inline
name: "Mist Stalker"
level: 4
source: "Monster Core 2"
aon_id: "creature-4391"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4391"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Mist Stalker"
level: "Creature 4"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Elemental"
trait_03: "Water"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, mist vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [4, 4, 2, 1, 5, 0]
abilities_top:
  - name: "Mist Cloud"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) 15 feet. The mist stalker is surrounded by mist. Creatures in the aura are [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]]. If wind disperses the aura, it returns automatically at the start of the mist stalker's turn. This cloud is suppressed in water."
  - name: "Mist Vision"
    desc: "The mist stalker ignores the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from mist and fog."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +12; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
speed: "20 feet, climb 20 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+4 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d8+4 bludgeoning, DC 21"
  - name: "Solidify Mist"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) The mist stalker makes its mist cloud congeal, causing the aura to be [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Difficult Terrain|difficult terrain]] until the start of the mist stalker's next turn. In addition, the mist stalker can make the mist even thicker around a single Medium or smaller creature within the cloud. The creature must succeed at a DC 20 Reflex save or become [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] or is no longer in the mist cloud's emanation."
sourcebook: "_Monster Core 2_, page 150."
```

```encounter-table
name: Mist Stalker
creatures:
  - 1: Mist Stalker
```
