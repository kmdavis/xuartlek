---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Street Watcher"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Street Watcher"
level: -1
source: "Monster Core"
aon_id: "creature-3044"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3044"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Halfling Street Watcher"
level: "Creature -1"
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Halfling|Halfling]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +4, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +3, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +5"
abilityMods: [-1, 3, 1, 0, 3, 1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/club/frying-pan|Frying Pan]], Halfling Sling Staff, Leather Armor"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +3; __Ref__: +8; __Will__: +5"
hp: 8
health:
  - name: "HP"
    desc: "8"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ frying pan +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d8]]) __Damage__ 1d4–1 bludgeoning"
  - name: "Ranged"
    desc: "⬻ halfling sling staff +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 80 feet, reload 1) __Damage__ 1d10–1 bludgeoning"
abilities_bot:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] action to find [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] or [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] creatures within 30 feet of it. Whenever the halfling targets a creature that is [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a [[srd/pf2e/compendium/rules-elements/actions/rage-of-elements|hidden]] one."
sourcebook: "_Monster Core_, page 192."
```

```encounter-table
name: Halfling Street Watcher
creatures:
  - 1: Halfling Street Watcher
```
