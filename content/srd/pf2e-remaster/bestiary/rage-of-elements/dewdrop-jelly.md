---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dewdrop Jelly"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/water
  - pf2e/creature/trait/small
statblock: inline
name: "Dewdrop Jelly"
level: 1
source: "Rage of Elements"
aon_id: "creature-2659"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2659"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Dewdrop Jelly"
level: "Creature 1"
size: "Small"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Water"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +6, Stealth +7"
abilityMods: [2, 3, 3, -4, 1, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +10; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20; __Immunities__ bleed, paralyzed, poison, sleep; __Resistances__ fire 5"
abilities_mid:
  - name: "Dissolve"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dewdrop jelly takes damage from a hostile action"
  - name: "Effect"
    desc: "The dewdrop jelly dissolves into a fine mist. Until the start of the jelly's next turn, it can't be attacked or targeted and doesn't take up space. At the end of the round, the jelly re-forms in any open space within 25 feet of where it Dissolved."
speed: "fly 20 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +8 __Damage__ 1d6+2 bludgeoning"
abilities_bot:
  - name: "Overflow"
    desc: "⬽ (Move) The dewdrop jelly flattens its bell and shoots forward, Flying or Swimming twice in a straight line toward its target and attempting a tentacle Strike. On a success, the dewdrop attaches to the target's face, covering its mouth in the suspended water of its gelatinous body. If the target cannot breathe water, it begins to drown. The DC to Escape is 16."
sourcebook: "_Rage of Elements_, page 180."
```

```encounter-table
name: Dewdrop Jelly
creatures:
  - 1: Dewdrop Jelly
```
