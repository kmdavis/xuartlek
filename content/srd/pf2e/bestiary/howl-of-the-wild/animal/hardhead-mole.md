---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hardhead Mole"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Hardhead Mole"
level: 0
source: "Howl of the Wild"
aon_id: "creature-3288"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3288"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Hardhead Mole"
level: "Creature 0"
size: "Small"
trait_01: "Animal"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; low-light vision, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +5, Stealth +5, Survival +6"
abilityMods: [2, 3, 3, -4, 2, 0]
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +5; __Ref__: +8; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20; __Resistances__ bludgeoning 3"
abilities_mid:
  - name: "Burrowing Retreat"
    desc: "⬲ (move)"
  - name: "Trigger"
    desc: "The hardhead mole is hit by a Strike"
  - name: "Effect"
    desc: "The hardhead mole immediately Burrows to a burrow hole if there is one within 20 feet. This movement doesn't trigger reactions."
speed: "20 feet, burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +4 __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Shovel Earth"
    desc: "⬻ (Manipulate) The hardhead mole leaves a burrow hole in its square or an adjacent square. The square becomes difficult terrain but can be flattened back into normal terrain with an Interact action."
  - name: "Unbalancing Burrow"
    desc: "⬺ (Move) The hardhead mole Burrows up to 20 feet in a straight line, displacing the earth on the surface. Any creature it passes through takes 1d6 bludgeoning damage (DC 14 basic Reflex save). On a failed save, a creature is knocked prone. This creates a burrow hole at the beginning and end of the line."
sourcebook: "_Howl of the Wild_, page 158."
```

```encounter-table
name: Hardhead Mole
creatures:
  - 1: Hardhead Mole
```
