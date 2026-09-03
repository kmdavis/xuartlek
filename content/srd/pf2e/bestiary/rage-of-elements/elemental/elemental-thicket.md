---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elemental Thicket"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/huge
statblock: inline
name: "Elemental Thicket"
level: 11
source: "Rage of Elements"
aon_id: "creature-2679"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2679"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Elemental Thicket"
level: "Creature 11"
size: "Huge"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23"
abilityMods: [7, 4, 6, 1, 2, 1]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +20; __Ref__: +13; __Will__: +25"
hp: 240
health:
  - name: "HP"
    desc: "240 , regeneration 15 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 10, fire 15"
abilities_mid:
  - name: "Entangling Growth"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/plant|plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 30 feet. Plant life erupts out of any and all soil surrounding the elemental thicket, making the area greater difficult terrain out to 5 feet and difficult terrain out to 30 feet. This ability requires soil and has no effect on terrain without it, such as worked stone, solid rock, open water, etc."
speed: "25 feet, burrow 25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ gnarled branch +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+7 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d12+7 bludgeoning, DC 30."
  - name: "Engulf"
    desc: "⬺ DC 30, 8d10 bludgeoning, Escape DC 27, Rupture 20."
sourcebook: "_Rage of Elements_, page 210."
```

```encounter-table
name: Elemental Thicket
creatures:
  - 1: Elemental Thicket
```
