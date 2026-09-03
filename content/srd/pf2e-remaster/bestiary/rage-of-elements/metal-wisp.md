---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Metal Wisp"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/tiny
statblock: inline
name: "Metal Wisp"
level: 0
source: "Rage of Elements"
aon_id: "creature-2642"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2642"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Metal Wisp"
level: "Creature 0"
size: "Tiny"
trait_01: "Elemental"
trait_02: "Metal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, rust vision"
languages: "Talican"
skills:
  - name: "Skills"
    desc: "Athletics +6, Mining Lore +4, Plane of Metal Lore +4"
abilityMods: [2, 1, 3, 0, 2, 0]
abilities_top:
  - name: "Rust Vision"
    desc: "A metal wisp ignores the concealed condition from rust clouds."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +3; __Will__: +6"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ bleed, electricity, paralyzed, poison, sleep; __Resistances__ electricity 2"
abilities_mid:
  - name: "Resonance"
    desc: "(aura, metal) 30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. Creatures in the area gain a +1 status bonus to attack and damage rolls made with metal weapons or effects with the metal trait; a creature with the elemental and metal traits gains this bonus to all attack and damage rolls."
  - name: "Accord Essence"
    desc: "⬲"
  - name: "Trigger"
    desc: "An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack"
  - name: "Effect"
    desc: "The wisp detonates itself in a small elemental explosion. Allies within 30 feet that have benefited from the wisp's resonance in the last hour gain temporary Hit Points equal to half the wisp's current Hit Points. These temporary Hit Points last 1 hour. A wisp that uses this reaction is permanently destroyed, and it can be restored only by a _wish_ ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
  - name: "Rust Cloud"
    desc: "A metal wisp is constantly surrounded by a cloud of rust flakes that cause it to be concealed from creatures more than 5 feet away from it."
speed: "fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +6 (reach 10 feet) __Damage__ 1d4 piercing plus 1 persistent bleed"
abilities_bot:
  - name: "In Concert"
    desc: "When a metal wisp rolls a critical failure on a check to Aid, it gets a failure instead, and when it rolls a success, it gets a critical success instead."
sourcebook: "_Rage of Elements_, page 152."
```

```encounter-table
name: Metal Wisp
creatures:
  - 1: Metal Wisp
```
