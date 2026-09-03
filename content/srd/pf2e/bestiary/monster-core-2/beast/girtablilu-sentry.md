---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Girtablilu Sentry"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/girtablilu
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Girtablilu Sentry"
level: 8
source: "Monster Core 2"
aon_id: "creature-4413"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4413"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Girtablilu Sentry"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Girtablilu"
trait_03: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision, tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Girtablilu"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +16, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [6, 4, 6, 3, 4, 3]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/armor#Hide Armor|Hide Armor]], _[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/spear/longspear|longspear]]_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +20; __Ref__: +16; __Will__: +12"
hp: 160
health:
  - name: "HP"
    desc: "160"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ longspear +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+9 piercing"
  - name: "Melee"
    desc: "⬻ pincer +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 2d8+9 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ stinger +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|unarmed]]) __Damage__ 2d6+9 piercing plus girtablilu venom"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d8+6 bludgeoning, DC 24"
  - name: "Desert Passage"
    desc: "A girtablilu [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Ignore Difficult Terrain|ignores natural difficult terrain]] in the desert."
  - name: "Girtablilu Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 24 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 1 (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 3"
    desc: "3d6 poison damage and enfeebled 2 (1 round)"
sourcebook: "_Monster Core 2_, page 166."
```

```encounter-table
name: Girtablilu Sentry
creatures:
  - 1: Girtablilu Sentry
```
