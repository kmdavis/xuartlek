---
noteType: pf2eMonster
aliases: "Esipil"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Esipil"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4533"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Esipil"
level: "Creature 1"
size: "Tiny"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; telepathy (touch)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +6, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7"
abilityMods: [0, 4, 2, 1, 2, 2]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/Binding Circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +9; __Will__: +5"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 2"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 1d8 slashing plus 1d4 spirit and Grab"
  - name: "Melee"
    desc: "⬻ claw +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 1d6 slashing plus 1d4 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]]) The esipil transforms into a Tiny cat, dog, or other unassuming domestic animal. This doesn't affect the esipil's statistics, but it could change the damage type of its Strikes."
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 15 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]]"
sourcebook: "_Monster Core 2_, page 274."
```

```encounter-table
name: Esipil
creatures:
  - 1: Esipil
```
