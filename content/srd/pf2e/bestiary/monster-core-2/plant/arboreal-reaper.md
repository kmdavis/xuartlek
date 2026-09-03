---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Arboreal Reaper"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Arboreal Reaper"
level: 7
source: "Monster Core 2"
aon_id: "creature-4062"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4062"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Arboreal Reaper"
level: "Creature 7"
size: "Large"
trait_01: "Plant"
trait_02: "Wood"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; low-light vision"
languages: "Arboreal, [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +14"
abilityMods: [6, 2, 4, 2, 2, 4]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +17; __Ref__: +13; __Will__: +15"
hp: 130
health:
  - name: "HP"
    desc: "130; __Resistances__ bludgeoning 5, piercing 5; __Weaknesses__ axes 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ branch +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ root +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d6+8 bludgeoning plus Knockdown"
  - name: "Ranged"
    desc: "⬻ thorns +16 __Damage__ 2d8+5 piercing plus 1d4 persistent bleed"
abilities_bot:
  - name: "Leech Moisture"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/void|Void]]) The arboreal reaper grows still and focuses intently on a single foe within 50 feet, draining moisture from the target's body. This deals 10d6 void damage (DC 25 basic Fortitude save). The arboreal reaper can't Leech Moisture again for 1d4 rounds."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 22 - __3rd__ [[srd/pf2e/compendium/spells/rank-3/vampiric-feast|Vampiric Feast]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]]"
sourcebook: "_Monster Core 2_, page 34."
```

```encounter-table
name: Arboreal Reaper
creatures:
  - 1: Arboreal Reaper
```
