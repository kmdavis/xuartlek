---
obsidianUIMode: preview
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
aon_id: "creature-2894"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2894"
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
    desc: "Perception +28; darkvision, lifesense 30 feet, _truesight_"
languages: "Common, Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +28, Athletics +32, Intimidation +33, Religion +26, Stealth +28, Survival +26"
abilityMods: [8, 6, 7, 2, 4, 7]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +27; __Ref__: +30; __Will__: +26 +1 status to all saves vs. magic"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ death effects, void; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Soul Siphon"
    desc: "(aura, divine, force) 30 feet. An astradaemon draws power from the souls of the recently slain. If a Small or larger living creature dies within their aura, the astradaemon gains 5 temporary Hit Points and a +1 status bonus to attack and damage rolls for 1 round, unless the creature was slain by an astradaemon's Devour Soul ability. Incorporeal undead and living spirits that are traveling outside a body take 1d8 spirit damage each round within the daemon's aura as the astradaemon pulls in fragments of their soul."
  - name: "Bent Light"
    desc: "(divine, illusion, visual) An astradaemon appears shifted from their true position, though still in the same space. Creatures targeting the astradaemon must succeed at a DC 11 flat check to do so, as if the astradaemon were hidden, even though the astradaemon remains observed. Abilities that apply to the flat check against hidden creatures also apply against bent light."
speed: "60 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +32 (Magical, reach 10 feet, Unholy) __Damage__ 3d6+8 piercing plus essence drain and Grab"
  - name: "Melee"
    desc: "⬻ claw +32 (Agile, Magical, reach 10 feet, Unholy) __Damage__ 2d6+8 slashing plus essence drain"
  - name: "Melee"
    desc: "⬻ tail +32 (Magical, reach 15 feet, Unholy) __Damage__ 3d10+8 bludgeoning plus essence drain"
abilities_bot:
  - name: "Devour Soul"
    desc: "⬻ (Divine, Incapacitation)"
  - name: "Requirements"
    desc: "The astradaemon hasn't used an action with the attack trait yet this turn"
  - name: "Effect"
    desc: "The astradaemon draws out and consumes the soul of a living creature they have grabbed. The creature must succeed at a DC 35 Fortitude save or instantly die. If it dies, the astradaemon gains 10 temporary Hit Points and a +2 status bonus to attack and damage rolls for 1 minute, or for 1 day if the victim was 15th level or higher. A victim slain in this way can be returned to life normally. A creature that survives is temporarily immune for 1 minute."
  - name: "Essence Drain"
    desc: "(Divine, Void) When an astradaemon hits with their claw, jaws, or tail, they drain the target's spiritual and vital essences. The target takes 2d10 void damage and the astradaemon regains an equal number of Hit Points. The target must succeed at a DC 37 Fortitude save or become doomed 1 and drained 1. If the target was already drained or doomed, it instead increases both conditions' value by 1, to a maximum of 4."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37 - __4th__ Translocate (at will) - __7th__ Interplanar Teleport (×2), Translocate - __8th__ Execute, Pinpoint - __Constant (6th)__ Truesight"
sourcebook: "_Monster Core_, page 75."
```

```encounter-table
name: Astradaemon
creatures:
  - 1: Astradaemon
```
