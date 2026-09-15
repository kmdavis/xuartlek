---
noteType: pf2eMonster
aliases: "Graveknight"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/graveknight
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Graveknight"
level: 10
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3030"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Graveknight"
level: "Creature 10"
size: "Medium"
trait_01: "Graveknight"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "+19; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +22, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +19, Warfare Lore +20"
abilityMods: [7, 4, 4, 2, 3, 5]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows), _+1 [[srd/pf2e/compendium/equipment/runes/Resilient|resilient]] [[srd/pf2e/compendium/equipment/Armor#Full Plate|full plate]]_, Greatsword"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +21; __Ref__: +19; __Will__: +18"
hp: 175
health:
  - name: "HP"
    desc: "175 (rejuvenation, void healing (page 360)); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Sacrilegious Aura"
    desc: "30 feet. Counteract modifier +17"
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _frost greatsword_ +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 2d12+10 slashing plus 1d6 cold"
  - name: "Melee"
    desc: "⬻ frost fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d6+10 bludgeoning plus 1d6 cold"
  - name: "Ranged"
    desc: "⬻ _frost composite longbow_ +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range increment 100 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 30 feet]]) __Damage__ 2d8+6 piercing plus 1d6 cold"
abilities_bot:
  - name: "Devastating Blast"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|Cold]]) 11d6 cold, DC 29"
  - name: "Graveknight's Curse"
    desc: "DC 33"
  - name: "Phantom Mount"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]]) HP 58; AC 27; Fort +17, Ref +15, Will +14"
  - name: "Weapon Master"
    desc: ""
sourcebook: "_Monster Core_, page 179."
```

```encounter-table
name: Graveknight
creatures:
  - 1: Graveknight
```
