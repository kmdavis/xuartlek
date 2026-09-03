---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Merfolk Wavecaller"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/merfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Merfolk Wavecaller"
level: 2
source: "Monster Core"
aon_id: "creature-3098"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3098"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Merfolk Wavecaller"
level: "Creature 2"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Merfolk"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +7, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +8, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +8"
abilityMods: [3, 2, 0, 1, 4, 2]
abilities_top:
  - name: "Items"
    desc: "Dagger"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +6; __Will__: +10"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "5 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Hydraulic Asphyxiation"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]])"
  - name: "Requirements"
    desc: "The target is fully submerged in water, within 30 feet of the merfolk wavecaller, and holding its breath"
  - name: "Effect"
    desc: "The merfolk wavecaller commands the tides to crush their foe's throat, rooting the target in place and forcing it to choke up precious air. The target must succeed at a DC 18 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] for 1 round and immediately lose 1d4 rounds' worth of air (or twice that on a critical failure)."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/electric-arc|Electric Arc]], [[srd/pf2e/compendium/spells/cantrips/frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/heal|Heal]], [[srd/pf2e/compendium/spells/rank-1/hydraulic-push|Hydraulic Push]]"
sourcebook: "_Monster Core_, page 231."
```

```encounter-table
name: Merfolk Wavecaller
creatures:
  - 1: Merfolk Wavecaller
```
