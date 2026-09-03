---
obsidianUIMode: preview
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
aon_id: "creature-3085"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3085"
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
    desc: "Perception +35; darkvision, scent (imprecise) 60 feet, _truesight_"
languages: "Aklo, Draconic, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +32, Athletics +38, Stealth +34"
abilityMods: [10, 6, 8, -1, 7, 8]
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +36; __Ref__: +32; __Will__: +31 +1 status to all saves vs. magic"
hp: 400
health:
  - name: "HP"
    desc: "400 , regeneration 15 (deactivated by cold iron); __Immunities__ acid, curse, paralyzed, sleep; __Weaknesses__ cold iron 15"
abilities_mid:
  - name: "Curse of Death"
    desc: "(curse, death, primal) When a creature slays the tarn linnorm, it must succeed at a DC 46 Will save or it can no longer recover Hit Points via any means, such as healing spells, the Medicine skill, or natural healing from rest. This has an unlimited duration."
  - name: "Reactive Strike"
    desc: "⬲ Tail only."
speed: "35 feet, fly 100 feet, swim 80 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (reach 30 feet, Magical) __Damage__ 4d12+18 piercing plus tarn linnorm venom"
  - name: "Melee"
    desc: "⬻ claw +38 (reach 30 feet, Agile, Magical) __Damage__ 4d8+18 slashing"
  - name: "Melee"
    desc: "⬻ tail +38 (reach 30 feet, Agile, Magical) __Damage__ 4d6+18 bludgeoning plus Improved Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 3d6+18 bludgeoning, DC 44"
  - name: "Corrosive Breath"
    desc: "⬺ (Acid, Poison, Primal) The tarn linnorm can expel either a 120-foot line or a 60-foot cone of acid, dealing 20d6 acid damage to creatures within the area (DC 44 basic Reflex save). The linnorm can't use Corrosive Breath or Double Breath again for 1d4 rounds. The acid creates toxic fumes. At the beginning of the linnorm's next turn, those who failed the breath weapon's Reflex save must succeed at a DC 42 Fortitude save or gain sickened 4 from the poisonous fumes."
  - name: "Double Bite"
    desc: "⬻ The tarn linnorm Strides and then makes a jaws Strike with each of their heads, each against a different target. Both attacks count toward the tarn linnorm's multiple attack penalty, but the multiple attack penalty doesn't increase until after the tarn linnorm makes all of these attacks."
  - name: "Double Breath"
    desc: "⬽ The tarn linnorm uses Corrosive Breath twice. A creature attempts only one save and can take damage only once. The linnorm can't use Corrosive Breath or Double Breath again for 2d4 rounds."
  - name: "Tarn Linnorm Venom"
    desc: "(Acid, Poison)"
  - name: "Saving Throw"
    desc: "DC 44 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "7d6 acid damage and drained 1 (1 round)"
  - name: "Stage 2"
    desc: "11d6 acid damage and drained 2 (1 round)"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 42 - __8th__ Truesight - __Constant (9th)__ Unfettered Movement"
sourcebook: "_Monster Core_, page 221."
```

```encounter-table
name: Tarn Linnorm
creatures:
  - 1: Tarn Linnorm
```
