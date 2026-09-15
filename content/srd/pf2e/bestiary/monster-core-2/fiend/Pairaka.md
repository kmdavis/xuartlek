---
noteType: pf2eMonster
aliases: "Pairaka"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/div
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Pairaka"
level: 7
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4341"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Pairaka"
level: "Creature 7"
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +20, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +13, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +13, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +16"
abilityMods: [3, 5, 3, 2, 4, 7]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +16; __Will__: +17 +1 status to all saves vs. magic"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]]; __Weaknesses__ [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Hatred of Red"
    desc: "Pairakas hate the color red. They won't wear the color or willingly enter any place painted in a shade of red. Given a choice, they'll attack a creature wearing red before others, seeing their choice to do so as a personal affront. If barred from expressing their displeasure toward the color by force or some magical effect, they take 2d6 mental damage at the end of their turn."
speed: "25 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]]) __Damage__ 2d8+9 slashing plus bubonic plague"
abilities_bot:
  - name: "Bubonic Plague"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|Disease]]) A creature can't remove the [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]] condition while infected"
  - name: "Saving Throw"
    desc: "DC 23 Fortitude; Onset 1 day"
  - name: "Stage 1"
    desc: "fatigued (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled]] 2 and fatigued (1 day)"
  - name: "Stage 3"
    desc: "enfeebled 3, fatigued, and takes 1d6 persistent bleed damage every 1d20 minutes (1 day)"
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|polymorph]]) The pairaka can take the appearance of any Small or Medium humanoid or animal. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their strikes deal."
  - name: "Tormenting Dreams"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The pairaka torments a sleeping creature within 100 feet with visions of betrayals by loved ones and friends. The target must attempt a DC 25 Will save, with the effects of the [[srd/pf2e/compendium/spells/rank-4/Nightmare|_nightmare_]] spell."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|Outcast's Curse]] (at will), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (at will), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will)"
  - name: "Rituals"
    desc: "DC 25 - __1st__ Div Pact"
sourcebook: "_Monster Core 2_, page 112."
```

```encounter-table
name: Pairaka
creatures:
  - 1: Pairaka
```
