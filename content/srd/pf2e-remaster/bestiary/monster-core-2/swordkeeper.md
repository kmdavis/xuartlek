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
    desc: "Acrobatics +21, Athletics +23"
abilityMods: [7, 5, 5, -5, 2, -5]
abilities_top:
  - name: "Central Weapon"
    desc: "A swordkeeper's torso houses a single weapon of a level no higher than the swordkeeper. While the swordkeeper is operational, the chamber requires four successful DC 32 Thievery checks to Disable a Device to open; on a critical failure, magical backlash deals 6d6 force damage (DC 30 basic Reflex save) to the creature attempting the check. If the swordkeeper is grabbed, immobilized, prone, or stunned, both DCs are reduced by 2. If the weapon is removed, the swordkeeper's echoblades vanish."
  - name: "Items"
    desc: "_+1 striking vitalizing longsword_"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +14"
hp: 245
health:
  - name: "HP"
    desc: "245; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ echoblade +23 (Magical, reach 10 feet, versatile P) __Damage__ 2d8+13 slashing plus 1d8 force"
  - name: "Melee"
    desc: "⬻ fist +23 (Agile, reach 10 feet) __Damage__ 2d8+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ echoblade +23 (Agile, magical, thrown 30 feet) __Damage__ 2d8+13 slashing plus 1d8 force"
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
    desc: "The swordkeeper projects an echoblade—a force copy of its central weapon that deals an additional 1d8 force damage and gains thrown 30 feet. Echoblades inherit the weapon damage dice, weapon traits, and runes of the central weapon but no other abilities or activations. The swordkeeper gains access to their critical specialization effects. The swordkeeper can have up to four echoblades at once; unattended echoblades vanish at the end of the swordkeeper's turn."
  - name: "Colossal Echo"
    desc: "⬺ (Force)"
  - name: "Requirements"
    desc: "The swordkeeper has a central weapon"
  - name: "Effect"
    desc: "The swordkeeper projects a massive echoblade held in all four hands, dealing 9d8 force damage to all creatures in a 30-foot line (DC 30 basic Reflex save). It can't use Colossal Echo again for 1d4 rounds."
  - name: "Raise Guard"
    desc: "⬻"
  - name: "Effect"
    desc: "The swordkeeper raises an echoblade to protect itself, gaining a +2 circumstance bonus to AC until the start of its next turn. Treasure Guardians While the sample swordkeeper awards treasure based on its level, you can use a swordkeeper to provide PCs with a powerful or significant weapon— particularly an artifact or relic. To create a swordkeeper with a different weapon, replace the versatile P trait from its echoblade Strikes with those of the new weapon, change the weapon damage dice to match, and apply any runes. Unless you want to significantly change the swordkeeper's level, you should also adjust the Strike damage to make sure it isn't too high or too low."
sourcebook: "_Monster Core 2_, page 314."
```

```encounter-table
name: Swordkeeper
creatures:
  - 1: Swordkeeper
```
