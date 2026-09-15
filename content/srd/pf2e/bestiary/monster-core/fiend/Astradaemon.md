---
noteType: pf2eMonster
aliases: "Astradaemon"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Astradaemon"
level: 16
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2894"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Astradaemon"
level: "Creature 16"
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 28
perception:
  - name: "Perception"
    desc: "+28; darkvision, lifesense 30 feet, [[srd/pf2e/compendium/spells/rank-6/Truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +28, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +32, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +33, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +26, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +28, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +26"
abilityMods: [8, 6, 7, 2, 4, 7]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +27; __Ref__: +30; __Will__: +26 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 15"
abilities_mid:
  - name: "Soul Siphon"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Force|force]]) 30 feet. An astradaemon draws power from the souls of the recently slain. If a Small or larger living creature dies within their aura, the astradaemon gains 5 temporary Hit Points and a +1 status bonus to attack and damage rolls for 1 round, unless the creature was slain by an astradaemon's Devour Soul ability. [[srd/pf2e/compendium/rules-elements/traits/gm-core/Incorporeal|Incorporeal]] [[srd/pf2e/compendium/rules-elements/traits/player-core/Undead|undead]] and living spirits that are traveling outside a body take 1d8 spirit damage each round within the daemon's aura as the astradaemon pulls in fragments of their soul."
  - name: "Bent Light"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|visual]]) An astradaemon appears shifted from their true position, though still in the same space. Creatures targeting the astradaemon must succeed at a DC 11 flat check to do so, as if the astradaemon were [[srd/pf2e/compendium/rules-elements/Conditions#Hidden|hidden]], even though the astradaemon remains [[srd/pf2e/compendium/rules-elements/Conditions#Observed|observed]]. Abilities that apply to the flat check against hidden creatures also apply against bent light."
speed: "60 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d6+8 piercing plus essence drain and Grab"
  - name: "Melee"
    desc: "⬻ claw +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+8 slashing plus essence drain"
  - name: "Melee"
    desc: "⬻ tail +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 3d10+8 bludgeoning plus essence drain"
abilities_bot:
  - name: "Devour Soul"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]])"
  - name: "Requirements"
    desc: "The astradaemon hasn't used an action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|attack]] trait yet this turn"
  - name: "Effect"
    desc: "The astradaemon draws out and consumes the soul of a living creature they have [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]]. The creature must succeed at a DC 35 Fortitude save or instantly die. If it dies, the astradaemon gains 10 temporary Hit Points and a +2 status bonus to attack and damage rolls for 1 minute, or for 1 day if the victim was 15th level or higher. A victim slain in this way can be returned to life normally. A creature that survives is temporarily immune for 1 minute."
  - name: "Essence Drain"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) When an astradaemon hits with their claw, jaws, or tail, they drain the target's spiritual and vital essences. The target takes 2d10 void damage and the astradaemon regains an equal number of Hit Points. The target must succeed at a DC 37 Fortitude save or become [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]] and [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]]. If the target was already drained or doomed, it instead increases both conditions' value by 1, to a maximum of 4."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/Interplanar Teleport|Interplanar Teleport]] (×2), [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-7/Execute|Execute]], [[srd/pf2e/compendium/spells/rank-8/Pinpoint|Pinpoint]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/Truesight|Truesight]]"
sourcebook: "_Monster Core_, page 75."
```

```encounter-table
name: Astradaemon
creatures:
  - 1: Astradaemon
```
