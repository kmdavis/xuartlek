---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elemental Hurricane"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Elemental Hurricane"
level: 11
source: "Monster Core"
aon_id: "creature-2976"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2976"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elemental Hurricane"
level: "Creature 11"
size: "Huge"
trait_01: "Air"
trait_02: "Elemental"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +24, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22"
abilityMods: [6, 7, 4, 0, 3, 0]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +19; __Ref__: +24; __Will__: +18"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "High Winds"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 40 feet. Air within the emanation is difficult terrain for [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flying]] creatures that don't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait."
  - name: "Disperse"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]])"
  - name: "Trigger"
    desc: "The elemental hurricane takes damage from a hostile action"
  - name: "Effect"
    desc: "The elemental hurricane disperses. Until the end of the current turn, it can't be attacked or targeted, doesn't take up space, and its high winds aura is suppressed. At the end of the turn, the elemental hurricane reforms in any unoccupied space within 100 feet of where it dispersed, and its high winds are restored."
speed: "fly 100 feet; swiftness"
attacks:
  - name: "Melee"
    desc: "⬻ gust +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d10+12 bludgeoning plus Push 10 feet"
  - name: "Ranged"
    desc: "⬻ lightning lash +24 (range increment 75 feet) __Damage__ 2d12+6 electricity"
abilities_bot:
  - name: "Gale Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]]) The elemental exhales a 30-foot cone of air. Creatures in the cone must succeed at a DC 29 Fortitude save or be knocked away from the elemental. A creature knocked into a solid object stops moving and takes 10d6 bludgeoning damage (roll the damage once for all creatures). The elemental hurricane can't use Gale Breath again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is pushed 20 feet."
  - name: "Failure"
    desc: "The creature is pushed 40 feet."
  - name: "Critical Failure"
    desc: "The creature is pushed 40 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Swiftness"
    desc: "The elemental's movement doesn't trigger reactions."
sourcebook: "_Monster Core_, page 141."
```

```encounter-table
name: Elemental Hurricane
creatures:
  - 1: Elemental Hurricane
```
