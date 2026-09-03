---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Swordkeeper"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Swordkeeper"
level: 10
source: "Monster Core 2"
aon_id: "creature-4574"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4574"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Swordkeeper"
level: "Creature 10"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23"
abilityMods: [7, 5, 5, -5, 2, -5]
abilities_top:
  - name: "Central Weapon"
    desc: "A swordkeeper's torso houses a single weapon of a level no higher than the swordkeeper. While the swordkeeper is operational, the chamber requires four successful DC 32 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disable a Device|Disable a Device]] to open; on a critical failure, magical backlash deals 6d6 force damage (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) to the creature attempting the check. If the swordkeeper is [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]], [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]], [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]], or [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]], both DCs are reduced by 2. If the weapon is removed, the swordkeeper's echoblades vanish."
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1 striking]] [[srd/pf2e/compendium/equipment/runes/vitalizing-greater|vitalizing]] [[srd/pf2e/compendium/equipment/weapons/sword/longsword|longsword]]_"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +14"
hp: 245
health:
  - name: "HP"
    desc: "245; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/damage-rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ echoblade +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d8+13 slashing plus 1d8 force"
  - name: "Melee"
    desc: "⬻ fist +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ echoblade +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 30 feet]]) __Damage__ 2d8+13 slashing plus 1d8 force"
abilities_bot:
  - name: "Echoblade Flurry"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The swordkeeper makes two melee echoblade Strikes. If both Strikes hit the same creature, combine their damage for the purpose of resistances and weakness. Apply the swordkeeper's multiple attack penalty normally."
  - name: "Project Echoblade"
    desc: "⭓"
  - name: "Requirements"
    desc: "The swordkeeper has a central weapon"
  - name: "Effect"
    desc: "The swordkeeper projects an echoblade—a force copy of its central weapon that deals an additional 1d8 force damage and gains thrown 30 feet. Echoblades inherit the weapon damage dice, weapon traits, and runes of the central weapon but no other abilities or activations. The swordkeeper gains access to their [[srd/pf2e/books/player-core/chapter-6-equipment/weapons#Critical Specialization|critical specialization]] effects. The swordkeeper can have up to four echoblades at once; unattended echoblades vanish at the end of the swordkeeper's turn."
  - name: "Colossal Echo"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/force|Force]])"
  - name: "Requirements"
    desc: "The swordkeeper has a central weapon"
  - name: "Effect"
    desc: "The swordkeeper projects a massive echoblade held in all four hands, dealing 9d8 force damage to all creatures in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). It can't use Colossal Echo again for 1d4 rounds."
  - name: "Raise Guard"
    desc: "⬻"
  - name: "Effect"
    desc: "The swordkeeper raises an echoblade to protect itself, gaining a +2 circumstance bonus to AC until the start of its next turn. Treasure Guardians While the sample swordkeeper awards treasure based on its level, you can use a swordkeeper to provide PCs with a powerful or significant weapon— particularly an artifact or relic. To create a swordkeeper with a different weapon, replace the [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]] trait from its echoblade Strikes with those of the new weapon, change the weapon damage dice to match, and apply any runes. Unless you want to significantly change the swordkeeper's level, you should also adjust the Strike damage to make sure it isn't too high or too low."
sourcebook: "_Monster Core 2_, page 314."
```

```encounter-table
name: Swordkeeper
creatures:
  - 1: Swordkeeper
```
