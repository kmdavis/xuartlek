---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Air Wisp"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/tiny
statblock: inline
name: "Air Wisp"
level: 0
source: "Monster Core 2"
aon_id: "creature-4394"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4394"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Air Wisp"
level: "Creature 0"
size: "Tiny"
trait_01: "Air"
trait_02: "Elemental"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Plane of Air Lore +4, Stealth +7"
abilityMods: [0, 3, 1, 0, 2, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +3; __Ref__: +9; __Will__: +4"
hp: 12
health:
  - name: "HP"
    desc: "12; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Resonance"
    desc: "(aura, air) 30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. Creatures in the area gain a +1 status bonus to attack and damage rolls for effects that have the air trait; a creature with the elemental and air traits gains this bonus to all attack and damage rolls."
  - name: "Accord Essence"
    desc: "⬲ (air)"
  - name: "Trigger"
    desc: "An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack"
  - name: "Effect"
    desc: "The wisp detonates themself in an elemental explosion. This grants temporary Hit Points equal to half the wisp's current Hit Points to allies within 30 feet who have benefited from the wisp's resonance in the last hour. These temporary Hit Points last 1 hour. A wisp that uses this reaction is permanently destroyed, and they can be restored by only a _wish_ ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +7 (reach 10 feet) __Damage__ 1d4 bludgeoning"
abilities_bot:
  - name: "In Concert"
    desc: "When an air wisp rolls a critical failure on a check to Aid, they get a failure instead, and when they roll a success, they get a critical success instead."
sourcebook: "_Monster Core 2_, page 152."
```

```encounter-table
name: Air Wisp
creatures:
  - 1: Air Wisp
```
