---
noteType: pf2eMonster
aliases: "Tarn Linnorm"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/acid
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Tarn Linnorm"
level: 20
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3085"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Tarn Linnorm"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Acid"
trait_02: "Amphibious"
trait_03: "Dragon"
trait_04: "Uncommon"
modifier: 35
perception:
  - name: "Perception"
    desc: "+35; darkvision, scent (imprecise) 60 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +32, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +38, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +34"
abilityMods: [10, 6, 8, -1, 7, 8]
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +36; __Ref__: +32; __Will__: +31 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 400
health:
  - name: "HP"
    desc: "400 , regeneration 15 (deactivated by [[srd/pf2e/compendium/equipment/materials/Cold Iron|cold iron]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]; __Weaknesses__ cold iron 15"
abilities_mid:
  - name: "Curse of Death"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]) When a creature slays the tarn linnorm, it must succeed at a DC 46 Will save or it can no longer recover Hit Points via any means, such as [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]] spells, the [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] skill, or natural healing from rest. This has an unlimited duration."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "35 feet, fly 100 feet, swim 80 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d12+18 piercing plus tarn linnorm venom"
  - name: "Melee"
    desc: "⬻ claw +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d8+18 slashing"
  - name: "Melee"
    desc: "⬻ tail +38 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 30 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 4d6+18 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d6+18 bludgeoning, DC 44"
  - name: "Corrosive Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The tarn linnorm can expel either a 120-foot line or a 60-foot cone of acid, dealing 20d6 acid damage to creatures within the area (DC 44 basic Reflex save). The linnorm can't use Corrosive Breath or Double Breath again for 1d4 rounds. The acid creates toxic fumes. At the beginning of the linnorm's next turn, those who failed the breath weapon's Reflex save must succeed at a DC 42 Fortitude save or gain [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 4]] from the poisonous fumes."
  - name: "Double Bite"
    desc: "⬻ The tarn linnorm Strides and then makes a jaws Strike with each of their heads, each against a different target. Both attacks count toward the tarn linnorm's multiple attack penalty, but the multiple attack penalty doesn't increase until after the tarn linnorm makes all of these attacks."
  - name: "Double Breath"
    desc: "⬽ The tarn linnorm uses Corrosive Breath twice. A creature attempts only one save and can take damage only once. The linnorm can't use Corrosive Breath or Double Breath again for 2d4 rounds."
  - name: "Tarn Linnorm Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 44 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "7d6 acid damage and [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "11d6 acid damage and drained 2 (1 round)"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 42 - __8th__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]] - __Constant (9th)__ [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 221."
```

```encounter-table
name: Tarn Linnorm
creatures:
  - 1: Tarn Linnorm
```
