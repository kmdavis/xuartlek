---
noteType: pf2eMonster
aliases: "Unicorn"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Unicorn"
level: 3
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3223"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Unicorn"
level: "Creature 3"
size: "Large"
trait_01: "Beast"
trait_02: "Fey"
trait_03: "Holy"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +11, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +9"
abilityMods: [4, 3, 3, 0, 4, 4]
abilities_top:
  - name: "Animal Empathy"
    desc: "The unicorn has a connection to the creatures of the natural world that allows them to communicate with [[srd/pf2e/compendium/rules-elements/traits/player-core/Animal|animals]]. They can ask questions of, receive answers from, and use the [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] skill with animals."
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +10; __Ref__: +8; __Will__: +11 (+2 vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]])"
hp: 45
health:
  - name: "HP"
    desc: "45; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]]"
speed: "45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d10+4 piercing plus 1d4 spirit and ghost touch"
  - name: "Melee"
    desc: "⬻ hoof +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 1d8+4 bludgeoning and ghost touch"
abilities_bot:
  - name: "Ghost Touch"
    desc: "A unicorn's Strikes have the effects of a [[srd/pf2e/compendium/equipment/runes/Ghost Touch|_ghost touch_]] property rune."
  - name: "Powerful Charge"
    desc: "⬺ The unicorn Strides up to double its Speed in a straight line and then makes a horn Strike. If the unicorn moved at least 20 feet, it deals an additional 2d6 damage on a hit. Alicorn In alchemical and occult circles, “alicorn” is the word for the material that makes up a unicorn's horn, also used to describe any object made from that horn. Note that in many markets, alicorn sales are illegal, and those who attempt to sell alicorn are viewed with repugnance—or worse."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Light|Light]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Cleanse Affliction|Cleanse Affliction]], [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (×2) - __5th__ [[srd/pf2e/compendium/spells/rank-5/Nature's Pathway|Nature's Pathway]]"
sourcebook: "_Monster Core_, page 333."
```

```encounter-table
name: Unicorn
creatures:
  - 1: Unicorn
```
