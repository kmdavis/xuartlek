---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Concert Frog"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Concert Frog"
level: 8
source: "Howl of the Wild"
aon_id: "creature-3281"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3281"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Concert Frog"
level: "Creature 8"
size: "Huge"
trait_01: "Animal"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +16, Athletics +16, Performance +19, Stealth +12"
abilityMods: [5, 3, 6, -4, 2, 4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +19; __Ref__: +13; __Will__: +16"
hp: 150
health:
  - name: "HP"
    desc: "150 (frog, 25 (froglets)); __Immunities__ area damage (froglets)"
abilities_mid:
  - name: "Three-Frog Orchestra"
    desc: "The concert frog has three froglets perched behind its lips, each of a different color. A creature can specifically target a froglet. If any froglets have died, the concert frog attempts a DC 11 flat check at the end of its turn; on a success, new froglets hatch in its stomach and emerge at the concert frog's lips."
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 __Damage__ 2d11+11 piercing"
  - name: "Ranged"
    desc: "⬻ croak +17 (Sonic, range 30 feet) __Damage__ 2d8+9 sonic"
abilities_bot:
  - name: "Conduct"
    desc: "⬻ (Auditory, Mental, Primal) One of the froglets begins to sing, granting one of three effects to the concert frog and all allies within 60 feet until the beginning of the concert frog's next turn."
  - name: "Red"
    desc: "Grants a +10-foot status bonus to their Speeds."
  - name: "Blue"
    desc: "Grants a +1 status bonus to AC and Fortitude saving throws."
  - name: "Yellow"
    desc: "Allies gain a +1 status bonus to attack rolls and deal an additional 1d4 sonic damage on successful melee Strikes as their attacks resonate."
sourcebook: "_Howl of the Wild_, page 151."
```

```encounter-table
name: Concert Frog
creatures:
  - 1: Concert Frog
```
