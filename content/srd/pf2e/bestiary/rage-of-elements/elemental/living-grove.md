---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Living Grove"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Living Grove"
level: 5
source: "Rage of Elements"
aon_id: "creature-2674"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2674"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Living Grove"
level: "Creature 5"
size: "Large"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; tremorsense 30 feet"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]; (understands but can't speak)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [4, 0, 5, 0, 1, 1]
abilities_top:
  - name: "Defensive Camouflage"
    desc: "The living grove can Hide in natural environments even if it doesn't have cover. While Hiding, its root system is safely covered in dirt, granting the grove a +3 status bonus to AC. A critical hit cracks this protective layer of earth to disperse in the wind, ending the effect."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +7; __Will__: +15"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ axes 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 7"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ branch +15 __Damage__ 2d8+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ nuts +11 (range increment 20 feet) __Damage__ 2d6+4 bludgeoning"
abilities_bot:
  - name: "Engulf"
    desc: "⬺ DC 22, 5d8 bludgeoning, Escape DC 20, Rupture 10. A creature Engulfed by the living grove must also attempt a basic Fortitude save as it's battered between the thin, tightly packed trunks."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is stunned 1."
  - name: "Failure"
    desc: "The creature is stunned 2."
  - name: "Critical Failure"
    desc: "The creature is stunned 4. Slumbering Giants Long before mortal civilization, living groves made their way to the Universe, buried their roots deep for safety, and fell dormant. A handful of these ancient elementals survive to this day, numbering among the oldest non-immortal entities yet living on the plane. Their long separation from the [[srd/pf2e/compendium/gm/planes#Plane of Wood|Plane of Wood]] has sent most into a deep hibernation, but an infusion of planar energy or powerful primal magic could potentially wake them up."
sourcebook: "_Rage of Elements_, page 207."
```

```encounter-table
name: Living Grove
creatures:
  - 1: Living Grove
```
