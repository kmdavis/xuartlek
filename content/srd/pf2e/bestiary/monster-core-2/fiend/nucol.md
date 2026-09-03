---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nucol"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Nucol"
level: 4
source: "Monster Core 2"
aon_id: "creature-4534"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4534"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Nucol"
level: "Creature 4"
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, scent (imprecise) 100 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +10, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [4, 2, 3, 0, 3, 2]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/binding-circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +10; __Will__: +11"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tusk +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d8+6 piercing plus 1d4 spirit and nervous consumption"
abilities_bot:
  - name: "Nervous Consumption"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Saving Throw"
    desc: "DC 21 Fortitude"
  - name: "Onset"
    desc: "1 minute"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1 and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 1 and stupefied 2 (1 day)"
  - name: "Stage 3"
    desc: "clumsy 2 and stupefied 3 (1 day)"
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Spray Pus"
    desc: "⬻ The nucol flexes one of its infected wounds, releasing a spray of pus in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]] or targeting an individual creature within 30 feet. A creature targeted or in the area is exposed to nervous consumption."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/grease|Grease]] (×3) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/cleanse-affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] (at will)"
sourcebook: "_Monster Core 2_, page 275."
```

```encounter-table
name: Nucol
creatures:
  - 1: Nucol
```
