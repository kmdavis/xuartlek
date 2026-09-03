---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stone Mauler"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/large
statblock: inline
name: "Stone Mauler"
level: 9
source: "Monster Core"
aon_id: "creature-2979"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2979"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Stone Mauler"
level: "Creature 9"
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision, tremorsense (imprecise) 80 feet"
languages: "Petran"
skills:
  - name: "Skills"
    desc: "Athletics +21, Stealth +12"
abilityMods: [6, -1, 7, -1, 3, -1]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, a stone mauler is slowed 1 and can't use reactions."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +23; __Ref__: +15; __Will__: +19"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Spike Stones"
    desc: "(aura, earth, primal) 5 feet. Spikes of rock rise up from all stone surfaces in the emanation, creating difficult terrain. A creature moving in the terrain takes 2d6 piercing damage for each square of spikes it moves into (a Large or larger creature takes damage only once for each square it moves, even if its space covers multiple squares of spikes). Creatures with the earth trait ignore all effects within the area. The stone mauler can disable or activate this aura using a single action, which has the concentrate trait."
  - name: "Crumble"
    desc: "⬲ Trigger The elemental takes damage from a hostile source while atop rock or earth; Effect The elemental crumbles into the ground, Burrowingdown 15 feet. This Burrowing does not trigger reactions. The elemental can't Crumble again for 1d4 rounds"
speed: "35 feet, burrow 35 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ fist +21 (reach 10 feet) __Damage__ 2d10+10 bludgeoning plus Push 10 feet"
  - name: "Ranged"
    desc: "⬻ rock +21 (Brutal, range increment 80 feet) __Damage__ 2d12+6 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "The elemental can Burrow through any earthen matter, including rock. When it does so, the elemental moves at its full burrow Speed, leaving no tunnels or signs of its passing."
sourcebook: "_Monster Core_, page 142."
```

```encounter-table
name: Stone Mauler
creatures:
  - 1: Stone Mauler
```
