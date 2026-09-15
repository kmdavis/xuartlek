---
noteType: pf2eMonster
aliases: "Aghash"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Aghash"
level: 4
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4340"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Aghash"
level: "Creature 4"
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +9, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +12, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +12, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +10, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +10"
abilityMods: [3, 4, 3, 1, 2, 4]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +10; __Will__: +12 +1 status to all saves vs. magic"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]]; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Hatred of Art"
    desc: "While aghashes hate all mortals, they particularly despise beautiful objects and artistic mortals. When not in physical peril, an aghash is compelled to destroy art and other works of beauty. An aghash can't enter an area of pristine beauty without first marring it in some way. Given a choice, an aghash will attack a foe who is an obvious crafter or performer of some kind. A [[srd/pf2e/compendium/character/classes/Bard|bard]] casting a composition spell, a runesmith tracing a rune, a street magician performing a daring escape, and similar abilities as determined by the GM draw the aghash's ire. If the aghash is barred from attacking such foes, either by force or some magical effect, they take 1d6 mental damage at the end of their turn."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d6+5 slashing"
abilities_bot:
  - name: "Cursed Gaze"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) The aghash fixes their gaze on one creature they can see within 20 feet. The creature must attempt a DC 21 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes 2d6 mental damage and becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] 1."
  - name: "Failure"
    desc: "The creature takes 4d6 mental damage and becomes either frightened 2 or [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] 1 (the aghash's choice)."
  - name: "Critical Failure"
    desc: "The creature takes 8d6 mental damage and becomes frightened 2 and stunned 2."
  - name: "Sandstorm"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The aghash creates a temporary sandstorm in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] that lasts for 1 minute. Creatures within the emanation take a –4 circumstance penalty to [[srd/pf2e/books/player-core/chapter-1-introduction/Character Creation#Perception|Perception]] checks and must succeed at a DC 18 Fortitude save. On a failure, they're forced to hold their breath or else they start suffocating. A creature within the sandstorm at the end of its turn takes 1d6 slashing damage. Divs are immune to all effects of an aghash's Sandstorm."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Stupefy|Stupefy]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|Outcast's Curse]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]]"
  - name: "Rituals"
    desc: "DC 21 - __1st__ Div Pact"
sourcebook: "_Monster Core 2_, page 111."
```

```encounter-table
name: Aghash
creatures:
  - 1: Aghash
```
