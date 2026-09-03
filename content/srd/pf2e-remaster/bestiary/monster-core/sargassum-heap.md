---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sargassum Heap"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/large
statblock: inline
name: "Sargassum Heap"
level: 6
source: "Monster Core"
aon_id: "creature-3171"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3171"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sargassum Heap"
level: "Creature 6"
size: "Large"
trait_01: "Amphibious"
trait_02: "Plant"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; wavesense (precise) 60 feet"
skills:
  - name: "Skills"
    desc: "Athletics +17, Stealth +14"
abilityMods: [5, 4, 5, -4, 2, 0]
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +17; __Ref__: +14; __Will__: +10"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ critical hits, precision, unconscious; __Resistances__ cold 5; __Weaknesses__ slashing 5"
abilities_mid:
  - name: "Mirage Spores"
    desc: "(aura, incapacitation, mental) 120 feet. The sargassum heap constantly produces a field of hallucinogenic spores that causes those affected to see the monster as whatever they desire most. Each creature within the emanation must succeed a DC 22 Will save or become fascinated with the sargassum heap and compelled to move toward it on the creature's turn. Creatures fascinated this way are also off-guard. If the sargassum heap attacks, the fascinated condition ends only for the creature that is attacked. On a successful save, a creature is temporarily immune to mirage spores for 24 hours."
speed: "10 feet, climb 10 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +17 (reach 10 feet) __Damage__ 2d8+8 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d8+3 bludgeoning, DC 23"
sourcebook: "_Monster Core_, page 295."
```

```encounter-table
name: Sargassum Heap
creatures:
  - 1: Sargassum Heap
```
