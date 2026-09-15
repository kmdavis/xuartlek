---
noteType: pf2eMonster
aliases: "Vordine"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Vordine"
level: 5
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2906"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vordine"
level: "Creature 5"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +13, Warfare Lore +13, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +12"
abilityMods: [4, 4, 5, 2, 3, 2]
abilities_top:
  - name: "Items"
    desc: "Breastplate, Whip, Trident"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +14; __Ref__: +13; __Will__: +10 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Resistances__ physical 5 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 5; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ trident +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d8+10 piercing"
  - name: "Melee"
    desc: "⬻ hoof +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d4+7 bludgeoning plus 1d4 fire"
  - name: "Ranged"
    desc: "⬻ trident +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 1d8+10 piercing"
  - name: "Melee"
    desc: "⬻ whip +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 1d4+10 bludgeoning"
abilities_bot:
  - name: "Burning Hoofprints"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) The vordine Strides, trailing hoofprints in each square they exit. The hoofprints burn for 1 minute. A creature on the ground that enters a square with burning hoofprints or begins its turn in one takes 1d4 fire damage."
  - name: "Trident of Dis"
    desc: "⬻ The vordine makes a trident Strike, increasing their reach to 10 feet for that Strike. If there is an [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] ally between the vordine and their target, that creature's energy causes the Strike to deal an additional 1d6 spirit damage."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 19 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will)"
  - name: "Rituals"
    desc: "DC 19 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 87."
```

```encounter-table
name: Vordine
creatures:
  - 1: Vordine
```
