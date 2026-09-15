---
noteType: pf2eMonster
aliases: "Kimenhul"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Kimenhul"
level: 20
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4538"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kimenhul"
level: "Creature 20"
size: "Huge"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 35
perception:
  - name: "Perception"
    desc: "+35; darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +36, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +33, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +34, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +38, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +33, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +35, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +36"
abilityMods: [10, 8, 9, 5, 7, 7]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/Binding Circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +33; __Ref__: +32; __Will__: +35 +4 status bonus vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] effects"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 20"
abilities_mid:
  - name: "Feed on Fear"
    desc: "The kimenhul regains 30 Hit Points at the start of its turn as long as any [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] creature is within 100 feet of it."
  - name: "Reactive Strike"
    desc: "⬲ If the triggering creature is [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]], the kimenhul can make two claw Strikes against the creature instead of one Strike."
speed: "45 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 4d12+18 piercing plus 3d6 spirit"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 4d8+18 slashing plus 3d6 spirit and Improved Grab"
abilities_bot:
  - name: "Eternal Fear"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) The kimenhul contorts its faces and presents itself to its enemies in a terrifying and traumatic display that causes lingering fear. Each creature within 100 feet that can observe the kimenhul must attempt a DC 42 Will save. They are then temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] 3."
  - name: "Failure"
    desc: "The target becomes frightened 3 and is fleeing as long as it’s frightened. Even after recovering from the initial experience, the trauma is lodged in the target’s mind for 1 year. Once per day, the kimenhul can communicate telepathically with the target for 1 minute as long as both creatures are on the same plane. Any time a creature under the effect of Eternal Fear is in a stressful situation (such as combat or intense social pressure), they must succeed at a DC 11 flat check or become frightened 2. While Eternal Fear lasts, the target always becomes fleeing as long as it’s frightened, regardless of the source of the fear. The target can attempt a new saving throw each week to remove these effects, but they can otherwise be removed by only powerful magic such as a [[srd/pf2e/compendium/spells/rituals/Wish|_wish_]] ritual."
  - name: "Critical Failure"
    desc: "As failure, but the effects are permanent, and the target doesn’t get to attempt a weekly save to end the effect."
  - name: "Frightening Flurry"
    desc: "⬺ The kimenhul makes one jaws Strike and two claw Strikes against a single target, in any order. The target becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] with a condition value equal to the number of Strikes that hit it, to a maximum of frightened 3 if all three Strikes hit."
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|Teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/Planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Snatch Between"
    desc: "When using Skip Between, the kimenhul can bring along any creatures it has [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]]."
  - name: "Unsettled Mind"
    desc: "Any creature affected by any of a kimenhul's mental spells or abilities becomes [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied]] 3 for the duration of that effect and for 1d4 rounds thereafter."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __9th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]] (at will), [[srd/pf2e/compendium/spells/rank-7/Mask of Terror|Mask of Terror]] (at will), [[srd/pf2e/compendium/spells/rank-9/Phantasmagoria|Phantasmagoria]], [[srd/pf2e/compendium/spells/rank-6/Phantasmal Calamity|Phantasmal Calamity]], [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (at will), [[srd/pf2e/compendium/spells/rank-7/Warp Mind|Warp Mind]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-8/Hidden Mind|Hidden Mind]], [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core 2_, page 278."
```

```encounter-table
name: Kimenhul
creatures:
  - 1: Kimenhul
```
