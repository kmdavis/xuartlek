---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Great White Shark"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/large
statblock: inline
name: "Great White Shark"
level: 4
source: "Monster Core"
aon_id: "creature-3188"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3188"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Great White Shark"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; blood scent, scent (imprecise) 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +14, Stealth +12, Survival +9"
abilityMods: [6, 2, 4, -4, 1, -4]
abilities_top:
  - name: "Blood Scent"
    desc: "The shark can smell blood in the water from up to 1 mile away."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +10; __Will__: +9"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 1d12+8 piercing"
abilities_bot:
  - name: "Breach"
    desc: "⬺ The shark Swims up to its swim Speed, then Leaps vertically out of the water up to 25 feet high, making a Strike against a creature at any point during the jump (this lets it attack a creature within 30 feet of the water's surface). After the Strike, the shark splashes back down into the water."
  - name: "Savage"
    desc: "⬻"
  - name: "Requirements"
    desc: "The shark hit with a jaws Strike on its most recent action this turn"
  - name: "Effect"
    desc: "The creature the shark hit takes 1d12 slashing damage."
  - name: "Strafing Chomp"
    desc: "⬻ The shark Swims up to half its swim Speed, makes a jaws Strike, and then Swims up to half its Speed further. The Strike deals half damage."
sourcebook: "_Monster Core_, page 307."
```

```encounter-table
name: Great White Shark
creatures:
  - 1: Great White Shark
```
