---
noteType: pf2eMonster
aliases: "Clay Effigy"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Clay Effigy"
level: 10
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2881"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Clay Effigy"
level: "Creature 10"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "+16; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24"
abilityMods: [6, -1, 6, -5, 0, -5]
abilities_top:
  - name: "Sacred Art"
    desc: "The creator of a clay effigy can dedicate the effigy to a deity while constructing it. If the deity allows a [[srd/pf2e/books/player-core/chapter-1-introduction/Religion#Deities|divine sanctification]], the effigy is sanctified to that deity, gaining the [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|unholy]] trait as appropriate."
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +23; __Ref__: +16; __Will__: +17"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Resistances__ physical 10 (except adamantine), spells 10 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Cold|cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Earth|earth]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|water]])"
abilities_mid:
  - name: "Effigy's Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) When a creature damages the clay effigy, it must succeed at a DC 27 Will save or be afflicted with the effigy's curse. The accursed becomes [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]] when it carries part of the effigy or any item the effigy was assigned to guard. This fatigue can't be removed until the creature has given up such items for at least 24 hours."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sanctified|Sanctified]]) __Damage__ 2d10+6 bludgeoning plus 2d6 spirit"
abilities_bot:
  - name: "Cast Out"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sanctified|Sanctified]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|Spirit]]) A 20-foot emanation of spiritual energy pushes against intruders, as though trying to drive their souls away. Each creature in the area takes 8d6 spirit damage depending on a DC 29 Will save. The clay effigy can't Cast Out again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and 3d6 persistent spirit damage. The persistent damage ends if the creature moves over 60 feet from the clay effigy or the effigy is destroyed."
  - name: "Critical Failure"
    desc: "As failure, except the persistent damage is increased to 6d6."
  - name: "Heavy Stride"
    desc: "⬺ The clay effigy Strides and can move through the spaces of Medium and smaller creatures. Each creature it moves through must succeed at a DC 29 Reflex save or be knocked [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. Clay Shards The remains of clay effigies are worth more to archaeologists and scholars than to merchants. The magnificent treasures often guarded by these ancient wardens, however, are another matter entirely."
sourcebook: "_Monster Core_, page 64."
```

```encounter-table
name: Clay Effigy
creatures:
  - 1: Clay Effigy
```
