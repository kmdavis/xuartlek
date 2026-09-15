---
noteType: pf2eMonster
aliases: "Charnel Creation"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Charnel Creation"
level: 8
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2878"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Charnel Creation"
level: "Creature 8"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19"
abilityMods: [5, -1, 3, -5, 0, -5]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +14; __Will__: +15"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]], [[srd/pf2e/compendium/rules-elements/Conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Resistances__ physical 5 (except adamantine), spells 5 (except [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]])"
abilities_mid:
  - name: "Berserk"
    desc: "A severely damaged charnel creation has a chance of going berserk. If it has 40 or fewer HP at the start of its turn, the creation must succeed at a DC 5 flat check or go berserk. A berserk creation wildly attacks the nearest living creature, or the nearest object if no creatures are nearby. A creation loses its immunity to [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] effects while berserk."
  - name: "Electric Healing"
    desc: "Any time a charnel creation would be affected by an effect with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] trait, it loses any [[srd/pf2e/compendium/rules-elements/Conditions#Slowed|slowed]] condition it has and gains HP equal to half the damage the spell would have dealt. If the creation starts its turn in an area that deals electricity damage, it gains 2d4 HP."
  - name: "Electric Reflexes"
    desc: "⬲"
  - name: "Trigger"
    desc: "The creation would be affected by an effect with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Electricity|electricity]] trait and a creature is in its reach"
  - name: "Effect"
    desc: "The creation lashes out and tries to grab a nearby creature. The creation attempts an [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] a creature within reach. The creature also takes 3d6 electricity damage on a success, or 6d6 electricity damage on a critical success."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 2d10+7 bludgeoning"
abilities_bot:
  - name: "Berserk Slam"
    desc: "⬻"
  - name: "Requirements"
    desc: "The charnel creation is berserk"
  - name: "Effect"
    desc: "The charnel creation Strikes with its fist at a –1 circumstance penalty. If it hits, it deals 1d6 extra damage and knocks the target [[srd/pf2e/compendium/rules-elements/Conditions#Prone|prone]]. Useless Remnants Few buyers want anything to do with the remains of a destroyed charnel creation. An adventurer's best bet for profiting off of a charnel creation body is to disassemble it piece by piece, extract the few contraptions of steel and copper meant to harness electricity, and sell the parts to tinkerers who ask few questions."
sourcebook: "_Monster Core_, page 61."
```

```encounter-table
name: Charnel Creation
creatures:
  - 1: Charnel Creation
```
