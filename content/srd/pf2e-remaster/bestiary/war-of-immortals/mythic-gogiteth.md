---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mythic Gogiteth"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/mythic
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Mythic Gogiteth"
level: 12
source: "War of Immortals"
aon_id: "creature-3400"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3400"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "WoI"
name: "Mythic Gogiteth"
level: "Creature 12"
size: "Large"
trait_01: "Aberration"
trait_02: "Mythic"
trait_03: "Rare"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Sakvroth; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +24, Stealth +28, Survival +17"
abilityMods: [6, 3, 4, -2, 1, 0]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +25; __Ref__: +22; __Will__: +20 mythic resilience (Ref and Will)"
hp: 250
health:
  - name: "HP"
    desc: "250; __Resistances__ poison 10"
abilities_mid:
  - name: "Hazard Immunity"
    desc: ""
  - name: "Skittering Reposition"
    desc: "⬲ (move)"
  - name: "Trigger"
    desc: "A creature that starts its move outside the gogiteth's reach moves into its reach"
  - name: "Effect"
    desc: "The gogiteth moves 10 feet. This does not trigger reactions."
speed: "40 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 __Damage__ 3d10+12 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ leg +26 (Agile, reach 10 feet) __Damage__ 3d6+12 piercing"
abilities_bot:
  - name: "Mythic Power"
    desc: "3 Mythic Points _Mythic Skill_ ⭓"
  - name: "Cost"
    desc: "1 Mythic Point; Athletics or Stealth (page 168)_Remove a Condition_ ⬻ (concentrate)"
  - name: "Cost"
    desc: "1 Mythic Point"
  - name: "Effect"
    desc: "The gogiteth ends one condition affecting it."
  - name: "Carry Off Prey"
    desc: "The gogiteth can move at its full Speed while it has a creature grabbed in its jaws, bringing the grabbed creature along."
  - name: "Constrict"
    desc: "⬻ 3d6+12 bludgeoning, DC 32"
  - name: "Skittering Assault"
    desc: "⬺ The gogiteth Strides three times. Once per Stride, it can attempt a leg Strike against a creature in its reach at any point during the Stride; it must make each attack against a different creature, but it doesn't apply its multiple attack penalty until after making all its Strikes. If the result of any of the Strikes is a critical failure, Skittering Assault ends."
sourcebook: "_War of Immortals_, page 170."
```

```encounter-table
name: Mythic Gogiteth
creatures:
  - 1: Mythic Gogiteth
```
