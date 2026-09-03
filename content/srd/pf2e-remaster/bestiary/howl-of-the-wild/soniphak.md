---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Soniphak"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/huge
statblock: inline
name: "Soniphak"
level: 9
source: "Howl of the Wild"
aon_id: "creature-3269"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3269"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Soniphak"
level: "Creature 9"
size: "Huge"
trait_01: "Beast"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; no vision, sensitive echolocation (precise) 120 feet"
languages: "Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +20, Survival +17"
abilityMods: [7, 6, 4, -2, 4, 1]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +21; __Will__: +15"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ visual; __Resistances__ sonic 10"
abilities_mid:
  - name: "Disruptive Screech"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 30 feet of the soniphak uses an auditory action"
  - name: "Effect"
    desc: "The soniphak makes a screech Strike against the triggering creature. This disrupts a triggering concentrate action if the Strike is a critical hit."
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +19 (reach 15 feet) __Damage__ 3d8+9 piercing"
  - name: "Melee"
    desc: "⬻ claw +19 (Agile) __Damage__ 3d6+9 slashing plus Grab"
  - name: "Ranged"
    desc: "⬻ screech +19 (range 60 feet, Sonic) __Damage__ 6d6 sonic plus aftershock"
abilities_bot:
  - name: "Aftershock"
    desc: "Whenever a soniphak hits with a screech Strike, feedback deals each creature the soniphak has grabbed or restrained 1d6 sonic damage."
  - name: "Shattering Scream"
    desc: "⬺ (Sonic) The soniphak can focus its screech at a stone or rock surface within 60 feet to create an explosion in a 15-foot burst from the point of impact. Creatures in the area take 5d6 piercing damage (DC 28 basic Reflex save), and the area becomes difficult terrain due to fragments of loose stone."
  - name: "Snatch"
    desc: "The soniphak can Fly at half Speed with a creature grabbed or restrained in its claws, carrying that creature along with it."
sourcebook: "_Howl of the Wild_, page 141."
```

```encounter-table
name: Soniphak
creatures:
  - 1: Soniphak
```
