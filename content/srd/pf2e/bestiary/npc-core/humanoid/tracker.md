---
noteType: pf2eMonster
aliases: "Tracker"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Tracker"
level: 3
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3471"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tracker"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Lore|Forest Lore]] +5, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +13"
abilityMods: [2, 4, 2, 0, 4, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]], if the tracker rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and eight additional creatures, and on a critical success, they can take care of twice as many creatures as on a success."
  - name: "Master Tracker"
    desc: "The tracker can [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] while moving at full speed."
  - name: "Items"
    desc: "Composite Longbow (60 arrows), Dagger, Leather Armor"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +7; __Ref__: +11; __Will__: +9"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing"
  - name: "Ranged"
    desc: "⬻ composite longbow +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly 1d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 1d8+5 piercing"
abilities_bot:
  - name: "On the Hunt"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]]) The tracker designates one creature they're observing or tracking as their prey. The tracker gains a +2 circumstance bonus to Perception checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] the prey and to [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] the prey. The first time the tracker hits the designated prey in a round, they deal an additional 1d4 precision damage. These effects last until the tracker uses On the Hunt again."
sourcebook: "_NPC Core_, page 54."
```

```encounter-table
name: Tracker
creatures:
  - 1: Tracker
```
