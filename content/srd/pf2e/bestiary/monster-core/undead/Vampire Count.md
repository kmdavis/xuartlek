---
noteType: pf2eMonster
aliases: "Vampire Count"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/vampire
  - pf2e/creature/trait/medium
statblock: inline
name: "Vampire Count"
level: 6
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3225"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vampire Count"
level: "Creature 6"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Vampire"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]; plus one regional language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +14, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +14, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +14, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +13"
abilityMods: [5, 3, 2, 2, 4, 4]
abilities_top:
  - name: "Children of the Night"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Items"
    desc: "Leather Armor, _+1 [[srd/pf2e/compendium/equipment/weapons/sword/Rapier|rapier]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +11; __Ref__: +14; __Will__: +17"
hp: 65
health:
  - name: "HP"
    desc: "65 (coffin restoration, fast healing 7, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Resistances__ physical 7 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]] [[srd/pf2e/compendium/equipment/materials/Silver|silver]])"
abilities_mid:
  - name: "Vampire Vulnerabilities"
    desc: ""
  - name: "Mist Escape"
    desc: "⭓"
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _rapier_ +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|disarm +1]]) __Damage__ 1d6+11 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d8+8 slashing plus Grab"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) Giant bat with fangs +15 for 1d8+9 piercing (page 358)."
  - name: "Create Servitor"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Downtime|Downtime]])"
  - name: "Dominate"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]]) DC 22"
  - name: "Drink Blood"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]]) When Drinking Blood, the vampire count regains 10 HP."
  - name: "Turn to Mist"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]])"
sourcebook: "_Monster Core_, page 336."
```

```encounter-table
name: Vampire Count
creatures:
  - 1: Vampire Count
```
