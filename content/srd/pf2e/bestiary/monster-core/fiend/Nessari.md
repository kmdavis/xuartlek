---
noteType: pf2eMonster
aliases: "Nessari"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Nessari"
level: 20
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2911"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nessari"
level: "Creature 20"
size: "Large"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 37
perception:
  - name: "Perception"
    desc: "+37; greater darkvision, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +34, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +32, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +39, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +39, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +37, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +36, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +34"
abilityMods: [9, 8, 9, 8, 9, 8]
abilities_top:
  - name: "Recall Knowledge - Fiend"
    desc: "([[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]]): DC 40"
  - name: "Unspecific Lore"
    desc: ": DC 38"
  - name: "Specific Lore"
    desc: ": DC 35 [[srd/pf2e/bestiary/monster-core/fiend/Nessari|Nessari]] Large Devil Fiend Unholy"
  - name: "Shape Devils"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Downtime|downtime]]) The nessari reshapes a large number of [[srd/pf2e/bestiary/monster-core/fiend/Ort|orts]] within a 600-foot emanation into more powerful devils to swell [[srd/pf2e/compendium/gm/Planes#Hell|Hell's]] legions. The nessari must have available the number of orts listed on the table in the sidebar below. The nessari can shape 100 orts per day, to a maximum of 1,100 orts in 11 days. Devils created in this way are in thrall to the nessari and follow their orders, with the exception of created nessaris or other devils of similar power, which are always independent. As a result, few nessaris choose to create peers. At the end of the Shape Devils activity, the nessari attempts an [[srd/pf2e/books/gm-core/chapter-1-running-the-game/Difficulty Classes#Adjusting Difficulty|incredibly hard]] [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] check [[srd/pf2e/books/gm-core/chapter-1-running-the-game/Difficulty Classes#Level-Based DCs|of the desired devil's level]], with results as follows."
  - name: "Critical Success"
    desc: "The nessari shapes two devils from the massed orts instead of one."
  - name: "Success"
    desc: "The nessari shapes a devil of the desired type and level."
  - name: "Failure"
    desc: "The devil shaped from the orts is 2 levels lower than the intended devil."
  - name: "Critical Failure"
    desc: "The nessari fails to shape any devils and draws the ire of an archdevil for their waste of resources."
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +37; __Ref__: +32; __Will__: +35 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 335
health:
  - name: "HP"
    desc: "335 , regeneration 30 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Resistances__ physical 15 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 15; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Commander's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) 100 feet. Commanded or allied [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] creatures in the aura of lower level than the nessari gain a +1 circumstance bonus to attack rolls, damage rolls, AC, saves, and skill checks."
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 20 feet, DC 42"
  - name: "Reactive Strike"
    desc: "⬲ The nessari can make a Reactive Strike when a creature within reach uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|concentrate]] action, in addition to the usual trigger. The devil can disrupt triggering concentrate actions, and they disrupt actions on any hit, not only a critical hit."
speed: "35 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +40 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d10+17 piercing plus nessari venom"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d6+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d10+17 bludgeoning plus Improved Grab"
  - name: "Melee"
    desc: "⬻ wing +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 4d6+17 slashing"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) 2d10+17 bludgeoning, DC 43"
  - name: "Fast Swoop"
    desc: "⬻ The nessari Flies and makes a wing Strike at any point during its movement."
  - name: "Masterful Quickened Casting"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "If the nessari's next action is to cast an 8th-rank or lower innate spell, reduce the number of actions to cast it by 1 (minimum 1 action)."
  - name: "Nessari Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 43 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "6d6 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "7d6 poison damage and drained 2 (1 round)"
  - name: "Stage 3"
    desc: "8d6 poison damage and drained 3 (1 round) Shape Devils A nessari needs a minimum number of orts in order to shape the roiling mass into a devil of a particular level, as summarized below."
  - name: "Devil Level"
    desc: ""
  - name: "Number of Orts"
    desc: "4 or below45–687–8169–103211–126413–1412815–1625617–1851219–201,024"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-7/Divine Decree|Divine Decree]] (at will), [[srd/pf2e/compendium/spells/rank-3/Fireball|Fireball]] (at will), [[srd/pf2e/compendium/spells/rank-6/Scrying|Scrying]], [[srd/pf2e/compendium/spells/rank-4/Wall of Fire|Wall of Fire]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-9/Seize Soul|Seize Soul]] (at will) - __10th__ [[srd/pf2e/compendium/spells/rank-9/Falling Stars|Falling Stars]], [[srd/pf2e/compendium/spells/rank-10/Manifestation|Manifestation]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 42 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 92."
```

```encounter-table
name: Nessari
creatures:
  - 1: Nessari
```
