---
noteType: pf2eMonster
aliases: "Water Orm"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Water Orm"
level: 10
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4614"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Water Orm"
level: "Creature 10"
size: "Huge"
trait_01: "Aquatic"
trait_02: "Beast"
trait_03: "Rare"
trait_04: "Water"
modifier: 21
perception:
  - name: "Perception"
    desc: "+21; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Thalassic|Thalassic]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +23"
abilityMods: [8, 5, 5, -3, 5, 0]
abilities_top:
  - name: "Slow Metabolism"
    desc: "A water orm can go for 10 years without feeding. Beyond this limit, the water orm's hunger causes it to become [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] 1 but doesn't otherwise impact its lifespan. A water orm that's slowed as a result of starvation can remove this condition by using Swallow Whole to gulp down a meal."
  - name: "Undetectable"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) A water orm automatically tries to [[srd/pf2e/books/player-core/chapter-7-spells/Counteracting|counteract]] any [[srd/pf2e/compendium/rules-elements/traits/player-core/Detection|detection]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Revelation|revelation]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Scrying|scrying]] ability attempted against it, using its [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] modifier for the counteract check."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +19; __Will__: +17"
hp: 170
health:
  - name: "HP"
    desc: "170; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]] 10"
speed: "20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d10+11 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ tail +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 2d6+11 bludgeoning"
abilities_bot:
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]]) Large, 2d8+8 bludgeoning, Rupture 22"
  - name: "Water Travel"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]]) A water orm can dissolve into water, appearing only as a long, dark, serpentine stretch of liquid. While in this form, a water orm's swim Speed increases to 600 feet, it automatically succeeds at [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swim]], and it gains a +4 circumstance bonus to [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] checks in water. A water orm can remain in this form for 8 hours, but it can't enter salt water when using this ability. A water orm can return to its normal form by [[srd/pf2e/books/player-core/chapter-7-spells/Durations#Dismissing|Dismissing]] this action. Local Orms People who live by the lakes inhabited by legendary water orms have a tendency to give local lake monsters names that sound somewhat homey or even adorable. As a result, such creatures are often regarded as local mascots or good luck charms— particularly in lakeside settlements that depend on fishing as a significant income source."
sourcebook: "_Monster Core 2_, page 352."
```

```encounter-table
name: Water Orm
creatures:
  - 1: Water Orm
```
