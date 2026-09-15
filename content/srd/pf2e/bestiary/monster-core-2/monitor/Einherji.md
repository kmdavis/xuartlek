---
noteType: pf2eMonster
aliases: "Einherji"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/aesir
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Einherji"
level: 10
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4016"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Einherji"
level: "Creature 10"
size: "Medium"
trait_01: "Aesir"
trait_02: "Monitor"
modifier: 17
perception:
  - name: "Perception"
    desc: "+17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Hallit|Hallit]], [[srd/pf2e/compendium/rules-elements/Languages#Jotun|Jotun]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +16, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21"
abilityMods: [7, 4, 6, 0, 1, 3]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+1 striking]] [[srd/pf2e/compendium/equipment/runes/Returning|returning]] [[srd/pf2e/compendium/equipment/weapons/knife/Dagger|dagger]]_, _[[srd/pf2e/compendium/equipment/weapons/Magic Weapon|+1 striking]] [[srd/pf2e/compendium/equipment/weapons/sword/Longsword|longsword]]_, [[srd/pf2e/compendium/equipment/shields/Duskwood Shield|standard-grade duskwood shield]] (Hardness 5, HP 20, BT 10)"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +22; __Ref__: +18; __Will__: +17 (+21 vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]])"
hp: 175
health:
  - name: "HP"
    desc: "175; __Resistances__ piercing 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile P]]) __Damage__ 2d8+13 slashing"
  - name: "Melee"
    desc: "⬻ fist +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 2d6+13 bludgeoning"
  - name: "Melee"
    desc: "⬻ _dagger_ +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+13 piercing"
  - name: "Ranged"
    desc: "⬻ _dagger_ +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 2d4+13 piercing __Champion Devotion Spells 2 Focus Points,__ DC 29 - __5th__ [[srd/pf2e/compendium/spells/focus/Spectral Advance|Spectral Advance]]"
abilities_bot:
  - name: "Challenge Foe"
    desc: "⬻ The einherji challenges one creature they can see to single combat, attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralize]] that target. This target remains the einherji's foe until it's defeated, it flees, or the encounter ends. The einherji gains a circumstance bonus to damage equal to their number of weapon damage dice against their designated foe but takes an equivalent circumstance penalty to damage against any other creature. If the einherji is defeated by their challenged foe, the shame causes them to lose use of their champion devotion spells for 1 week or until they challenge the same foe again and emerge victorious, whichever comes first."
  - name: "Instant Repair"
    desc: "⬻ The einherji [[srd/pf2e/compendium/rules-elements/actions/player-core#Repair|Repairs]] their shield. They can't use this ability if the shield is destroyed."
  - name: "Jotun Slayer"
    desc: "The einherji has a +4 circumstance bonus to damage rolls made against [[srd/pf2e/compendium/rules-elements/traits/player-core/Giant|giants]] and creatures that are at least two sizes larger than the einherji. The Final Battle Regardless of the deity they serve, all einherjar follow certain beliefs and mythologies. They assert that, in the final days of existence, [[srd/pf2e/compendium/deities/gods-of-the-inner-sea/Pharasma|Pharasma]] will judge the last soul and spark the beginning of a new existence. Einherjar believe they will be among the last souls left prior to this event, fighting alongside their gods against the forces of entropy. To einherjar, victory in this war—defined as thorough mutual destruction—is the only way to ensure a proper transition into the new existence."
sourcebook: "_Monster Core 2_, page 14."
```

```encounter-table
name: Einherji
creatures:
  - 1: Einherji
```
