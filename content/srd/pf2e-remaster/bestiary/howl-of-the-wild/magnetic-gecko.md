---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Magnetic Gecko"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Magnetic Gecko"
level: 1
source: "Howl of the Wild"
aon_id: "creature-3282"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3282"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Magnetic Gecko"
level: "Creature 1"
size: "Small"
trait_01: "Animal"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision, greater electrolocation 20 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +6, Athletics +6, Stealth +6"
abilityMods: [2, 3, 4, -4, 2, -1]
abilities_top:
  - name: "Greater Electrolocation"
    desc: "A magnetic gecko can sense minute electrical charges in living creatures, which it can use as a precise sense at a range of 20 feet. This distance increases to 100 feet against any creature that has used an electricity effect within the last minute."
  - name: "Uncanny Climber"
    desc: "A magnetic gecko's feet allow it to climb virtually any surface, no matter how slick or sheer. If a gecko attempts an Athletics check to Climb and critically fails, it gets a failure instead."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +10; __Ref__: +7; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ electricity"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ tongue +7 (Electricity, Finesse, reach 10 feet) __Damage__ 2d4 electricity plus static cling"
abilities_bot:
  - name: "Launch Metal"
    desc: "⬺ The gecko repulses the metal attached to its body in all directions, dealing 2d6 bludgeoning damage (DC 17 basic Reflex save) to all creatures in a 10-foot emanation. The gecko can't use Launch Metal again for 1d4 rounds."
  - name: "Repel"
    desc: "⬻ The gecko manipulates its magnetic field to repel metal, humming audibly and gaining resistance 2 to damage from metal weapons and metal effects until the beginning of its next turn."
  - name: "Static Cling"
    desc: "If the gecko hits Small or smaller creature with its tongue, and the target is made of metal or is wearing metallic armor, the gecko's tongue latches on to the creature. The creature must attempt a DC 17 Reflex save or become grabbed. While the gecko is Grabbing a creature in this way, it can attempt an Athletics check against the target's Fortitude DC to pull the creature to a space adjacent to the gecko. A creature grabbed in this way can Escape normally."
sourcebook: "_Howl of the Wild_, page 152."
```

```encounter-table
name: Magnetic Gecko
creatures:
  - 1: Magnetic Gecko
```
