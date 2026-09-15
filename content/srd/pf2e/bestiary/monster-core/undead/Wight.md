---
noteType: pf2eMonster
aliases: "Wight"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/wight
  - pf2e/creature/trait/medium
statblock: inline
name: "Wight"
level: 3
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3239"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Wight"
level: "Creature 3"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Wight"
modifier: 10
perception:
  - name: "Perception"
    desc: "+10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +10, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +9, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +8"
abilityMods: [4, 1, 4, 0, 3, 2]
abilities_top:
  - name: "Grave Weapon"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) The wight is bound to a dagger it was buried with. Other wights can be bound to different weapons."
  - name: "Items"
    desc: "Dagger"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +11; __Ref__: +6; __Will__: +10"
hp: 40
health:
  - name: "HP"
    desc: "40 (fueled by spite, void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Disease|disease]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]], [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]]"
abilities_mid:
  - name: "Final Spite"
    desc: "⬲"
  - name: "Trigger"
    desc: "The wight is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The wight makes a Strike before being destroyed. This Strike can inflict corrupting spite, but fueled by spite doesn't apply."
  - name: "Fueled by Spite"
    desc: "Each time a creature loses Hit Points due to a corrupting spite curse the wight inflicted, the wight gains 3 temporary Hit Points."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 piercing plus corrupting spite"
  - name: "Melee"
    desc: "⬻ claw +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]]) __Damage__ 1d4+6 slashing plus corrupting spite"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+6 slashing plus corrupting spite"
abilities_bot:
  - name: "Corrupting Spite"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) The wight's [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|unarmed]] attacks and bound weapons inflict a curse that makes a creature grow weak and spiteful. If a wight inflicts corrupting spite on a creature already afflicted by it, the victim attempts a new save, ignoring the result if it's better than a failure. A living humanoid that dies while under the curse rises as a wight after 1d4 rounds, [[srd/pf2e/compendium/rules-elements/Conditions#Controlled|controlled]] by the wight that killed it. The wight spawn can't inflict corrupting spite and is [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 2]]. If its creator dies or after roughly a month of existence, the new wight becomes autonomous and turns into a normal wight"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Stage 1"
    desc: "[[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]] (1 round)"
  - name: "Stage 2"
    desc: "drained 2 and doesn't treat any creatures as allies (1 round)"
  - name: "Stage 3"
    desc: "As stage 2, except drained 3 (1 round)"
  - name: "Stage 4"
    desc: "As stage 2, except drained 4 (1 round)."
sourcebook: "_Monster Core_, page 348."
```

```encounter-table
name: Wight
creatures:
  - 1: Wight
```
