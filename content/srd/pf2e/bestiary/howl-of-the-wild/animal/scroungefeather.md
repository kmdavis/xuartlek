---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Scroungefeather"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Scroungefeather"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3304"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3304"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Scroungefeather"
level: "Creature 5"
size: "Small"
trait_01: "Animal"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; low-light vision"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Stealth +12, Thievery +14"
abilityMods: [3, 5, 2, -4, 1, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +14; __Ref__: +16; __Will__: +8"
hp: 76
health:
  - name: "HP"
    desc: "76"
speed: "20 feet; fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +12 (Finesse) __Damage__ 2d8+3 piercing"
  - name: "Melee"
    desc: "⬻ talon +12 (Agile, Finesse) __Damage__ 2d6+3 slashing"
abilities_bot:
  - name: "Grab Debris"
    desc: "⬻"
  - name: "Requirements"
    desc: "The scroungefeather is in its nest or another environment rich with debris"
  - name: "Effect"
    desc: "The scroungefeather uses an Interact action to grab an item with its beak, selected randomly; roll 1d4 to determine the type of debris. The scroungefeather gains access to the listed abilities until it uses Tossed Scraps to discard the debris or until it Releases the debris. The scroungefeather can't use its beak attack while it is using its beak to Grab Debris. __d4__"
  - name: "Item"
    desc: ""
  - name: "Effect"
    desc: "1 Armor scrap The scroungefeather gains a +2 circumstance bonus to its AC. 2 Shattered blade The scroungefeather gains a broken blade melee Strike with a +12 attack modifier that deals 2d10+6 slashing damage. 3 Unexploded bomb When the scroungefeather throws this with Tossed Scraps, all the damage is fire damage, and the bomb also deals 3 fire splash damage. 4 Faulty wand The scroungefeather gains a magic bolt ranged Strike with a +14 attack modifier that deals 2d6+6 force damage."
  - name: "Junk Nest"
    desc: "The scroungefeather's nest of sharp metallic junk covers a 15-foot-by-15-foot area. The area is difficult terrain and hazardous terrain to any non-scroungefeather creatures. A creature that moves on the ground through the nest takes 3 piercing damage for each square of the area it moves into. Scroungefeathers can Take Cover at any point in the nest."
  - name: "Tossed Scraps"
    desc: "⬻"
  - name: "Requirements"
    desc: "The scroungefeather has Grabbed Debris"
  - name: "Effect"
    desc: "The scroungefeather flings the debris at a target within 20 feet, making an attack roll with a +12 modifier. On a success, the target takes 2d10+5 bludgeoning damage."
sourcebook: "_Howl of the Wild_, page 177."
```

```encounter-table
name: Scroungefeather
creatures:
  - 1: Scroungefeather
```
