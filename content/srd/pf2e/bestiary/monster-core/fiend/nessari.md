---
obsidianUIMode: preview
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
aon_id: "creature-2911"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2911"
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
    desc: "Perception +37; greater darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +34, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +32, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +39, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +39, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +37, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +36, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +34"
abilityMods: [9, 8, 9, 8, 9, 8]
abilities_top:
  - name: "Recall Knowledge - Fiend"
    desc: "([[srd/pf2e/compendium/rules-elements/skills/religion|Religion]]): DC 40"
  - name: "Unspecific Lore"
    desc: ": DC 38"
  - name: "Specific Lore"
    desc: ": DC 35 [[srd/pf2e/bestiary/monster-core/fiend/nessari|Nessari]] Large Devil Fiend Unholy"
  - name: "Shape Devils"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/downtime|downtime]]) The nessari reshapes a large number of [[srd/pf2e/bestiary/monster-core/fiend/ort|orts]] within a 600-foot emanation into more powerful devils to swell [[srd/pf2e/compendium/gm/planes#Hell|Hell's]] legions. The nessari must have available the number of orts listed on the table in the sidebar below. The nessari can shape 100 orts per day, to a maximum of 1,100 orts in 11 days. Devils created in this way are in thrall to the nessari and follow their orders, with the exception of created nessaris or other devils of similar power, which are always independent. As a result, few nessaris choose to create peers. At the end of the Shape Devils activity, the nessari attempts an [[srd/pf2e/books/gm-core/chapter-1-running-the-game/difficulty-classes#Adjusting Difficulty|incredibly hard]] [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] check [[srd/pf2e/books/gm-core/chapter-1-running-the-game/difficulty-classes#Level-Based DCs|of the desired devil's level]], with results as follows."
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
    desc: "46; __Fort__: +37; __Ref__: +32; __Will__: +35 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 335
health:
  - name: "HP"
    desc: "335 , regeneration 30 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 15 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 15; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Commander's Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) 100 feet. Commanded or allied [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] creatures in the aura of lower level than the nessari gain a +1 circumstance bonus to attack rolls, damage rolls, AC, saves, and skill checks."
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 20 feet, DC 42"
  - name: "Reactive Strike"
    desc: "⬲ The nessari can make a Reactive Strike when a creature within reach uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] action, in addition to the usual trigger. The devil can disrupt triggering concentrate actions, and they disrupt actions on any hit, not only a critical hit."
speed: "35 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +40 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d10+17 piercing plus nessari venom"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d6+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d10+17 bludgeoning plus Improved Grab"
  - name: "Melee"
    desc: "⬻ wing +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 4d6+17 slashing"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) 2d10+17 bludgeoning, DC 43"
  - name: "Fast Swoop"
    desc: "⬻ The nessari Flies and makes a wing Strike at any point during its movement."
  - name: "Masterful Quickened Casting"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "If the nessari's next action is to cast an 8th-rank or lower innate spell, reduce the number of actions to cast it by 1 (minimum 1 action)."
  - name: "Nessari Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 43 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "6d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 round)"
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
    desc: "DC 42 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]] (at will), [[srd/pf2e/compendium/spells/rank-7/divine-decree|Divine Decree]] (at will), [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] (at will), [[srd/pf2e/compendium/spells/rank-6/scrying|Scrying]], [[srd/pf2e/compendium/spells/rank-4/wall-of-fire|Wall of Fire]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-9/seize-soul|Seize Soul]] (at will) - __10th__ [[srd/pf2e/compendium/spells/rank-9/falling-stars|Falling Stars]], [[srd/pf2e/compendium/spells/rank-10/manifestation|Manifestation]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
  - name: "Rituals"
    desc: "DC 42 - __1st__ [[srd/pf2e/compendium/spells/rituals/diabolic-pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 92."
```

```encounter-table
name: Nessari
creatures:
  - 1: Nessari
```
