---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Fire Wisp"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/tiny
statblock: inline
name: "Fire Wisp"
level: 0
source: "Monster Core 2"
aon_id: "creature-4396"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4396"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Fire Wisp"
level: "Creature 0"
size: "Tiny"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision, smoke vision"
languages: "Pyric"
skills:
  - name: "Skills"
    desc: "Acrobatics +5, Plane of Fire Lore +4, Stealth +7"
abilityMods: [1, 3, 2, 0, 2, 0]
abilities_top:
  - name: "Smoke Vision"
    desc: "The fire wisp ignores the concealed condition from smoke."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +7; __Will__: +4"
hp: 15
health:
  - name: "HP"
    desc: "15; __Immunities__ bleed, fire, paralyzed, poison, sleep; __Weaknesses__ cold 2, water 2"
abilities_mid:
  - name: "Resonance"
    desc: "(aura, fire) 30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. Creatures in the area gain a +1 status bonus to attack and damage rolls for effects that have the fire trait; a creature with the elemental and fire traits gains this bonus to all attack and damage rolls."
  - name: "Accord Essence"
    desc: "⬲ (fire)"
  - name: "Trigger"
    desc: "An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack"
  - name: "Effect"
    desc: "The wisp detonates themself in an elemental explosion. This grants temporary Hit Points equal to half the wisp's current Hit Points to allies within 30 feet who have benefited from the wisp's resonance in the last hour. These temporary Hit Points last 1 hour. A wisp that uses this reaction is permanently destroyed, and they can be restored by only a _wish_ ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
speed: "40 feet, fly 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +6 (reach 10 feet) __Damage__ 1d4+1 fire plus 1 persistent fire"
abilities_bot:
  - name: "In Concert"
    desc: "When a fire wisp rolls a critical failure on a check to Aid, they get a failure instead, and when they roll a success, they get a critical success instead."
sourcebook: "_Monster Core 2_, page 153."
```

```encounter-table
name: Fire Wisp
creatures:
  - 1: Fire Wisp
```
