---
noteType: pf2eMonster
aliases: "Aolaz"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Aolaz"
level: 18
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2826"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Aolaz"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Construct"
trait_02: "Rare"
modifier: 33
perception:
  - name: "Perception"
    desc: "+33; low-light vision, flawless hearing"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +35"
abilityMods: [9, 4, 8, -4, 6, 3]
abilities_top:
  - name: "Flawless Hearing"
    desc: "An aolaz has an incredible sense of hearing. It can hear any sound made within 1,000 feet as though it were only 5 feet away from the source of the sound, and any sound within 1 mile as though it were only 30 feet away from the source of the sound. An aolaz's hearing is a precise sense."
ac: 42
armorclass:
  - name: "AC"
    desc: "42; __Fort__: +35; __Ref__: +27; __Will__: +31"
hp: 255
health:
  - name: "HP"
    desc: "255; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|sonic]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Resistances__ physical 15 (except adamantine)"
speed: "50 feet, fly , water walk"
attacks:
  - name: "Melee"
    desc: "⬻ trunk +35 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 5d10+17 bludgeoning plus Grab"
  - name: "Melee"
    desc: "⬻ foot +33 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 5d8+15 bludgeoning"
abilities_bot:
  - name: "Roll"
    desc: "⬻ The aolaz tucks its head down and rolls up into an armored sphere. While Rolling, an aolaz has AC 44, Fort +37, Ref +29, Will +33, and Speed 100 feet, but it can't use its trunk Strikes or its Ultrasonic Blast. It can make foot Strikes while rolling, but only as part of a Trample. The aolaz can use this action again to unroll and resume its standing form."
  - name: "Trample"
    desc: "⬺ Huge or smaller, foot, DC 40"
  - name: "Ultrasonic Blast"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sonic|Sonic]]) The aolaz releases a tremendous blast of sonic energy from its trunk in a 150-foot line, dealing 12d10 sonic damage. The frequency of this sound is such that it is completely imperceptible to humanoids, but the damage it wreaks is all too evident. Each creature in the area must attempt a DC 40 Fortitude save. The aolaz can't use Ultrasonic Blast again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage and is [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned 1]]."
  - name: "Failure"
    desc: "The creature takes full damage and is stunned 2."
  - name: "Critical Failure"
    desc: "The creature takes double damage and is stunned 3. Jistkan Behemoths Thousands of years ago, the Jistka Imperium mastered the art of construct creation, and the aolaz represents the height of its craft. The Jistkans used primal magic to imbue their constructs with spirits of nature. However, when Jistkan creators turned to the outer planes, and to [[srd/pf2e/compendium/rules-elements/traits/player-core/Fiend|fiends]] in particular, as a source to power even greater constructs, they unknowingly orchestrated their own doom."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 40 - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]], [[srd/pf2e/compendium/spells/rank-2/Water Walk|Water Walk]]"
sourcebook: "_Monster Core_, page 22."
```

```encounter-table
name: Aolaz
creatures:
  - 1: Aolaz
```
