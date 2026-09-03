---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Witchwarg"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/large
statblock: inline
name: "Witchwarg"
level: 5
source: "Monster Core"
aon_id: "creature-3231"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3231"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Witchwarg"
level: "Creature 5"
size: "Large"
trait_01: "Beast"
trait_02: "Cold"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [6, 4, 4, 2, 3, 2]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +13; __Ref__: +15; __Will__: +10"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5"
abilities_mid:
  - name: "Buck"
    desc: "__ ⬲ DC 21 __Avenging Bite ⬲"
  - name: "Trigger"
    desc: "A creature within reach of the warg's jaws attacks one of the warg's allies"
  - name: "Effect"
    desc: "The warg makes a jaws Strike against the triggering creature."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]]) __Damage__ 1d10+6 piercing plus 1d6 cold and Knockdown"
abilities_bot:
  - name: "Winter Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The witchwarg breathes a cloud of frost in a 15-foot cone that deals 5d8 cold damage (DC 23 basic Reflex save). The witchwarg can't use Winter Breath again for 1d4 rounds."
  - name: "Pack Attack"
    desc: "The witchwarg's Strikes deal 1d6 extra damage to creatures within the reach of at least two of the witchwarg's allies."
sourcebook: "_Monster Core_, page 341."
```

```encounter-table
name: Witchwarg
creatures:
  - 1: Witchwarg
```
