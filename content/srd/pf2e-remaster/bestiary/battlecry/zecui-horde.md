---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zecui Horde"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Zecui Horde"
level: 11
source: "Battlecry!"
aon_id: "creature-3946"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3946"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Zecui Horde"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Troop"
trait_03: "Uncommon"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +21, Stealth +23"
abilityMods: [4, 7, 3, 1, 3, 1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +24; __Will__: +18"
hp: 195
health:
  - name: "HP"
    desc: "195 (4 segments); __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet, burrow 20 feet, climb 20 feet; troop movement"
abilities_bot:
  - name: "Harden Chitin"
    desc: "⬻ The zecuis fuse their chitin into black metallic shells. The horde gains resistance 10 to all damage (except mental and spirit) until they next take a move action."
  - name: "Mandible Frenzy"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The horde makes a vicious bite attack against each enemy in a 5-foot emanation (DC 27 basic Reflex save). The damage dealt depends on the number of actions. ⬻ 1d8+2 piercing damage ⬺ 2d8+12 piercing damage ⬽ 3d8+15 piercing damage"
  - name: "Mucus Deluge"
    desc: "⬺ The horde spits a volley of larva-infested mucus as a 10-foot burst within 30 feet. Each creature in the area must succeed at a DC 27 Reflex save or be stuck to the nearest surface, immobilized until they Escape (DC 30). Any creature so immobilized is exposed to zecui larvae at the end of each of its turns. When the zecui horde is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Subterranean Ambush"
    desc: "⬻"
  - name: "Requirements"
    desc: "The zecui horde has burrowed into an ambush position just beneath a surface of dirt, sand, or a similar loose material"
  - name: "Effect"
    desc: "The horde bursts from the ground and moves up to its Speed. The horde deals 1d8+2 piercing damage (DC 29 basic Reflex save) to each enemy in a 5-foot emanation at the end of this movement."
  - name: "Zecui Larvae"
    desc: "(Disease)"
  - name: "Saving Throw"
    desc: "DC 30 Fortitude"
  - name: "Stage 1"
    desc: "visible lumps as the larvae move but no ill effect (1 day)"
  - name: "Stage 2"
    desc: "drained 1 (1 day)"
  - name: "Stage 3"
    desc: "drained 2 (1 day)"
  - name: "Stage 4"
    desc: "drained 3 and controlled by the zecui larva (1 day)"
  - name: "Stage 5"
    desc: "the creature dies and an adult zecui can emerge from the corpse as an Interact action."
sourcebook: "_Battlecry!_, page 195."
```

```encounter-table
name: Zecui Horde
creatures:
  - 1: Zecui Horde
```
