---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hound Of Tindalos"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/time
  - pf2e/creature/trait/medium
statblock: inline
name: "Hound Of Tindalos"
level: 7
source: "Monster Core 2"
aon_id: "creature-4623"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4623"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Hound Of Tindalos"
level: "Creature 7"
size: "Medium"
trait_01: "Aberration"
trait_02: "Rare"
trait_03: "Time"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; greater darkvision"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +15, Occultism +17, Stealth +17, Survival +13"
abilityMods: [4, 6, 2, 6, 4, 2]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +13; __Ref__: +17; __Will__: +15"
hp: 90
health:
  - name: "HP"
    desc: "90; __Immunities__ controlled, emotion; __Resistances__ mental 10, physical 10, poison 10"
abilities_mid:
  - name: "Otherworldly Mind"
    desc: "(mental) Whenever a creature targets the hound with a mental effect, that creature takes 4d6 mental damage (DC 25 basic Will save). On a critical failure, it also becomes confused for 1d4 rounds."
  - name: "Ripping Gaze"
    desc: "(aura, occult, visual) 30 feet. The hound of Tindalos's eyes glow balefully, causing painful but bloodless wounds to rip open in the body of a creature that meets its awful gaze. When a creature ends its turn in the aura's emanation, it takes 4d6 slashing damage (DC 25 basic Fortitude save). A creature that critically succeeds at its save is temporarily immune for 24 hours."
  - name: "Vulnerable to Curved Space"
    desc: "When a hound of Tindalos is not adjacent to a structural angle of 90° (or more acute), its resistance to physical damage is suppressed and it becomes sickened 1. It can't recover from this sickened condition, but the condition ends automatically once the hound is again adjacent to a suitable angle."
speed: "30 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +17 __Damage__ 2d10+7 piercing"
  - name: "Melee"
    desc: "⬻ claw +17 (Agile) __Damage__ 2d8+7 slashing"
abilities_bot:
  - name: "Angled Entry"
    desc: "⬻ The hound of Tindalos casts a 4th-rank _translocate_ spell, but it must transport itself into a space adjacent to an angle of 90° (or more acute) in the structure or environment around it. For example, it could teleport to a space adjacent to a wall (using the angle between the wall and floor) or a corner in a room, or adjacent to a sizable tree growing straight up out of the ground, but not to a flat plain or a room with only curved corners and edges. Once per day, the hound can use this ability to interplanar teleport to or from the Dimension of Time, with the same restrictions on what angles it can appear next to. Tindalos Ancient texts refer to these relentless temporal hunters as the hounds of Tindalos, yet they never seem to explore what Tindalos actually is. In some references, the implication is that Tindalos is one of the Great Old Ones or Outer Gods, but if this is the case, they're among the most obscure of these entities. Other tomes refer to Tindalos as a location, perhaps even a city or nation that once existed before time began and that can be reached only by methods impossible for any creature bound by the laws of time. In all likelihood, both and neither are right—what Tindalos is, is simply impossible for mortal minds to comprehend."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21 - __2nd__ Invisibility (self only) - __3rd__ Haste, Slow - __4th__ Planar Tether - __8th__ Pinpoint"
sourcebook: "_Monster Core 2_, page 183."
```

```encounter-table
name: Hound Of Tindalos
creatures:
  - 1: Hound Of Tindalos
```
