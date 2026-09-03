---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vampire Servitor"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/vampire
  - pf2e/creature/trait/medium
statblock: inline
name: "Vampire Servitor"
level: 4
source: "Monster Core"
aon_id: "creature-3224"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3224"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Vampire Servitor"
level: "Creature 4"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Vampire"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; plus one regional language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [3, 5, 1, -1, 3, 2]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +13; __Will__: +11"
hp: 40
health:
  - name: "HP"
    desc: "40 (coffin restoration, fast healing 5, void healing); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ physical 5 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]])"
abilities_mid:
  - name: "Vampire Vulnerabilities"
    desc: ""
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d8+6 slashing plus Grab"
abilities_bot:
  - name: "Drink Blood"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) When Drinking Blood, the servitor regains 5 HP."
  - name: "Sneak Attack"
    desc: "The servitor deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 336."
```

```encounter-table
name: Vampire Servitor
creatures:
  - 1: Vampire Servitor
```
