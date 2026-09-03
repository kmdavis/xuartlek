---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hadrinnex"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Hadrinnex"
level: 8
source: "Monster Core 2"
aon_id: "creature-4432"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4432"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hadrinnex"
level: "Creature 8"
size: "Large"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]; telepathy ([[srd/pf2e/books/player-core/chapter-7-spells/ranges-areas-and-targets#Touch Range|touch]])"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +16, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +11"
abilityMods: [6, 4, 6, -3, 3, -3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +17"
hp: 120
health:
  - name: "HP"
    desc: "120; __Resistances__ energy 15, physical 15 (see Rapid Evolution)"
abilities_mid:
  - name: "Rapid Evolution"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/morph|morph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]])"
  - name: "Trigger"
    desc: "The hadrinnex takes damage of a physical or energy damage type (bludgeoning, piercing, or slashing for physical; [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/force|force]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/sonic|sonic]] for energy)"
  - name: "Effect"
    desc: "The hadrinnex reconfigures its husk (if triggered by physical damage) or its energy gland (if triggered by energy damage). Any reconfiguration applies to the triggering damage and lasts until the next time the hadrinnex uses Rapid Evolution."
  - name: "Energy Gland"
    desc: "Reconfiguring the energy gland changes both the hadrinnex's energy damage resistance and the damage of its energy ray to the triggering energy damage type. By default, the energy gland is configured to sonic."
  - name: "Husk"
    desc: "The hadrinnex's physical damage resistance and the damage of its weapon arm Strikes change to the triggering type. Weapon arm Strikes gain an additional trait depending on the current damage type: bludgeoning adds [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|shove]], piercing adds [[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], and slashing adds [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|sweep]]. By default, the husk is configured to bludgeoning."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ weapon arm +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+9 physical (see Rapid Evolution)"
  - name: "Ranged"
    desc: "⬻ energy ray +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], range 120 feet) __Damage__ 5d6 energy (see Rapid Evolution)"
abilities_bot:
  - name: "Extend Limbs"
    desc: "⬺ The hadrinnex makes two weapon arm Strikes, each targeting a different creature. The hadrinnex's reach increases to 20 feet for these Strikes."
  - name: "Vent Energy"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The hadrinnex purges the energy in its energy gland for an external discharge. It either blasts the energy to deal 7d6 energy damage to creatures in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] (DC 26 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) or directs the energy to its weapon arms, making its weapon arm Strikes deal an extra 2d6 energy damage for 1 minute. Either one expends the damage type stored in the hadrinnex's energy gland, which then goes dormant. The hadrinnex loses its energy resistance and can't use energy ray until it uses Rapid Evolution to reconfigure its energy gland again. Directing energy to its weapon arms again removes any previous energy boost to its weapon arm. Hibernation Pods Hadrinnexes can be found hibernating in remote areas, their husks shaped into ovoid pods. These pods are usually centered in craters, suggesting the hadrinnex fell from above. Leaving hibernation takes 2 months as it extrudes its limbs and restarts biological processes. This can be accelerated with a daily influx of energy to its energy gland."
sourcebook: "_Monster Core 2_, page 185."
```

```encounter-table
name: Hadrinnex
creatures:
  - 1: Hadrinnex
```
