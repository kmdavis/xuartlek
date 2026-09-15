---
noteType: pf2eMonster
aliases: "Sumbreiva"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/void
  - pf2e/creature/trait/large
  - pf2e/creature/trait/negative
statblock: inline
name: "Sumbreiva"
level: 16
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4570"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sumbreiva"
level: "Creature 16"
size: "Large"
trait_01: "Humanoid"
trait_02: "Unholy"
trait_03: "Void"
trait_04: "Negative"
modifier: 29
perception:
  - name: "Perception"
    desc: "+29; greater darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +35, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +29"
abilityMods: [8, 9, 3, 6, 5, 4]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +25; __Ref__: +33; __Will__: +27"
hp: 290
health:
  - name: "HP"
    desc: "290 (void healing); __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]]"
abilities_mid:
  - name: "Hunter's Triumph"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
  - name: "Trigger"
    desc: "The sumbreiva kills a creature"
  - name: "Effect"
    desc: "The sumbreiva lets out a triumphant, bone-chilling howl. Every enemy in a 30-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Area#Emanation|emanation]] must succeed at a DC 36 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]] 3 (and [[srd/pf2e/compendium/rules-elements/Conditions#Fleeing|fleeing]] as long as it's frightened on a critical failure)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sumbreiva huntblade +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 3d8+16 piercing plus huntblade brutality"
  - name: "Melee"
    desc: "⬻ shadow whip +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Disarm|disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 3d4+16 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ sumbreiva huntblade +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 3d8+16 piercing plus huntblade brutality"
abilities_bot:
  - name: "Claim Trophy"
    desc: "⬻ The sumbreiva claims the soul of a creature they killed within the last minute. This works like seize soul, except that no black sapphire is required, and the soul is turned into a glowing blue light called a soul trophy. Anyone who kills the sumbreiva can then free the soul from any soul trophy by touching it and speaking the word for “freedom” in any language."
  - name: "Huntblade Brutality"
    desc: "The sumbreiva's huntblade deals an additional 2d8 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened]], or [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
  - name: "Whip Drain"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]])"
  - name: "Requirements"
    desc: "The sumbreiva has a creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]] with their shadow whip"
  - name: "Effect"
    desc: "The grabbed creature must succeed at a DC 38 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]] 2 (drained 3 on a critical failure). If the creature is already drained, this increases its drained value instead, to a maximum of drained 4. Superior Sumbreivas As sumbreiva hunters attain souls, they grow in power and physically transform. They might increase in stature, grow more limbs or great leathery wings, or form advanced armaments suited to their personalities and hunting methods. These outward manifestations make it easy for other sumbreivas to distinguish superior warriors from the less masterful hunters. The greatest sumbreivas are said to be inexorable giants suited for hunting only kaiju, demigods, and the [[srd/pf2e/compendium/gm/creature-families/Spawn of Rovagug|spawn of Rovagug]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 36 - __4th__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-3/Earthbind|Earthbind]]"
sourcebook: "_Monster Core 2_, page 309."
```

```encounter-table
name: Sumbreiva
creatures:
  - 1: Sumbreiva
```
