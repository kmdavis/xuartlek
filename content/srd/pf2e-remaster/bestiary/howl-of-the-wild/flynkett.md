---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Flynkett"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Flynkett"
level: 3
source: "Howl of the Wild"
aon_id: "creature-3279"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3279"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Flynkett"
level: "Creature 3"
size: "Small"
trait_01: "Animal"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +11, Athletics +9, Stealth +11"
abilityMods: [2, 4, 3, -4, 2, 0]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +10; __Ref__: +11; __Will__: +7"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ acid 6"
abilities_mid:
  - name: "Spill"
    desc: "⬲ (acid)"
  - name: "Requirements"
    desc: "The flynkett is Kettled Up"
  - name: "Trigger"
    desc: "The flynkett takes physical damage or is knocked prone"
  - name: "Effect"
    desc: "The flynkett spills the contents of its full skin flaps, releasing its digestive juices in a cloud of acidic vapor that deals 2d8 acid damage to all non-flynkett creatures within 20 feet (DC 18 basic Fortitude save). If the flynkett was boiling, the damage is increased to 4d8."
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +9 (Agile) __Damage__ 2d4+4 slashing"
  - name: "Ranged"
    desc: "⬻ acid spit +11 (Acid, range 40 feet) __Damage__ 1d8 persistent acid"
abilities_bot:
  - name: "Glide"
    desc: "⬻ (Move) The flynkett stretches its flaps to glide through the air. It moves 5 feet down and up to 25 feet forward through the air. The flynkett can remain in the air long as it spends at least 1 action Gliding each round and does not Kettle Up."
  - name: "Kettle Up"
    desc: "⬺ The flynkett uses its skin flaps to form a crude kettle. While Kettled Up, the flynkett can't use its claw Strike or take move actions. If the flynkett has been Kettled Up for 1 minute or longer, and its kettle is full of water (usually due to the flynkett being in the rain), the flynkett's kettle begins to boil, emitting a piercing whistle that causes all creatures within 30 feet to take a –2 penalty to Perception checks to hear sources other than the flynkett; this is an auditory effect. The flynkett can stop Kettling Up as a free action."
sourcebook: "_Howl of the Wild_, page 150."
```

```encounter-table
name: Flynkett
creatures:
  - 1: Flynkett
```
