---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kraken"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Kraken"
level: 18
source: "Monster Core"
aon_id: "creature-3075"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3075"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Kraken"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Beast"
trait_03: "Uncommon"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +38, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +32, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +35, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +33"
abilityMods: [9, 4, 9, 5, 6, 5]
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +35; __Ref__: +28; __Will__: +32"
hp: 360
health:
  - name: "HP"
    desc: "360; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 20"
abilities_mid:
  - name: "Altered Weather"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) A kraken reshapes the weather within 2 miles of it, with the effect of the [[srd/pf2e/compendium/spells/rituals/control-weather|_control weather_]] ritual centered on the kraken and based on its emotional state, at the GM's discretion. If the kraken dies, the weather returns to normal immediately."
speed: "10 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ arm +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 40 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 4d10+17 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ tentacle +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 60 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d10+17 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ beak +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 3d10+17 piercing"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d10+17 bludgeoning, DC 40 (page 358). On a failed save, a creature that is holding its breath loses 1d4 rounds worth of air."
  - name: "Double Attack"
    desc: "⬻ The kraken makes two Strikes with two different arms or tentacles, each limb targeting a different creature. Double Attack counts as two attacks toward the kraken's multiple attack penalty, but the penalty doesn't increase until after both attacks are made. If the kraken subsequently uses the Grab action, it Grabs any number of creatures it hit with Double Attack."
  - name: "Ink Cloud"
    desc: "⬻ The kraken releases a cloud of black, venomous ink in an 80- foot emanation. This cloud has no effect outside water. Creatures inside the ink cloud are exposed to kraken ink poison and are [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] while inside the cloud. The kraken can't use Ink Cloud again for 2d6 rounds, and the cloud dissipates after 1 minute."
  - name: "Jet"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]]) The kraken moves through the water up to 280 feet in a straight line without triggering reactions."
  - name: "Kraken Ink"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) Krakens are immune to this poison"
  - name: "Saving Throw"
    desc: "DC 39 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "4d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (1 round)"
  - name: "Stage 2"
    desc: "5d6 poison damage and sickened 2 (1 round) Kraken Locations A kraken dwells in deep ocean trenches, sunken cities, or caves and reefs near hydrothermal vents. It seeks food near the surface, however, where it can prey on seagoing vessels. Kraken Treasure A kraken's hoard includes the plunder of ships lost at sea and the wealth of sunken cities. Virtually anything could be found in a kraken lair, but they especially covet scrolls, spell books, and other tomes of ancient lore, as well as gemstones and rarefied raw materials found only in the ocean depths."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 40 - __7th__ [[srd/pf2e/compendium/spells/rank-2/resist-energy|Resist Energy]] - __8th__ [[srd/pf2e/compendium/spells/rank-8/punishing-winds|Punishing Winds]] - __10th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]] (animals only)"
sourcebook: "_Monster Core_, page 212."
```

```encounter-table
name: Kraken
creatures:
  - 1: Kraken
```
