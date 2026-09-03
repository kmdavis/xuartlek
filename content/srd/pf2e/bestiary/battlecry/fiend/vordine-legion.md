---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vordine Legion"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Vordine Legion"
level: 10
source: "Battlecry!"
aon_id: "creature-3941"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3941"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Vordine Legion"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Troop"
trait_04: "Unholy"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; greater darkvision"
languages: "Common, Diabolic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +22, Athletics +24, Intimidation +22, Religion +19, Warfare Lore +22"
abilityMods: [5, 5, 7, 2, 3, 2]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +22; __Ref__: +19; __Will__: +16 +1 status to all saves vs. magic"
hp: 180
health:
  - name: "HP"
    desc: "180 (4 segments); __Immunities__ fire; __Resistances__ physical 10 (except silver), poison 10; __Weaknesses__ area damage 10, holy 10, splash damage 10"
abilities_mid:
  - name: "Reactive Attack"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the vordine legion's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The creature takes 2d8+11 piercing damage (DC 26 basic Reflex save); this damage has the magical and unholy traits. If the creature critically fails its saving throw and the trigger was a manipulate action, the legion disrupts that action."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Burning March"
    desc: "⬺ (Divine, Fire, Unholy) The vordine legion Strides, leaving an orderly pattern of burning hoofprints in each square they enter. The hoofprints continue to burn for 1 minute. Any creature on the ground that begins its turn in, or enters a square with, burning hoofprints takes 2d8 fire damage."
  - name: "Impaling Barrage"
    desc: "⬺ (Magical, Unholy) The vordine legion releases a hail of tridents. This hail is a 10-foot burst within 40 feet that deals 4d8 piercing damage (DC 26 basic Reflex save). Creatures that fail the saving throw are clumsy 1 until the start of the vordine legion's next turn (clumsy 2 on a critical failure). When the vordines are reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Tines of Dis"
    desc: "(Magical, Unholy)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The vordines of the legion make coordinated melee attacks with their tridents. Each enemy within a 5-foot emanation must attempt a DC 26 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+2 piercing damage ⬺ 2d8+11 piercing damage ⬽ 3d8+14 piercing damage"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __4th__ Translocate (at will)"
sourcebook: "_Battlecry!_, page 193."
```

```encounter-table
name: Vordine Legion
creatures:
  - 1: Vordine Legion
```
