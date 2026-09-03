---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Veiled Current"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/large
statblock: inline
name: "Veiled Current"
level: 8
source: "Rage of Elements"
aon_id: "creature-2618"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2618"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Veiled Current"
level: "Creature 8"
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18"
abilityMods: [2, 6, 4, 2, 1, 3]
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +15; __Ref__: +19; __Will__: +13"
hp: 100
health:
  - name: "HP"
    desc: "100; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The veiled current is [[srd/pf2e/compendium/rules-elements/conditions#Invisible|invisible]] at all times. When they take a hostile action of any kind, the veiled current is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] instead of [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] as the vague outline of their humanoid form becomes faintly visible until the start of their next turn."
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ static fold +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+8 bludgeoning plus Grab"
  - name: "Ranged"
    desc: "⬻ static scream +19 (range increment 50 feet) __Damage__ 2d8+4 sonic"
abilities_bot:
  - name: "Envelop"
    desc: "⬺"
  - name: "Requirements"
    desc: "The veiled current begins their turn with a target of their size or smaller [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The veiled current maintains the Grab and coalesces around the creature, stretching themself into a semisolid veil that smothers the creature within. This thereafter has the same effect as if the veiled current had Engulfed the creature (DC 26, 1d8+8 bludgeoning, Escape DC 26, Rupture 17). As engulfing a creature is a hostile action, the veiled current is [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] instead of [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] every round it has a creature engulfed."
sourcebook: "_Rage of Elements_, page 82."
```

```encounter-table
name: Veiled Current
creatures:
  - 1: Veiled Current
```
