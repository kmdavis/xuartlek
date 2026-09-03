---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elananx"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/medium
statblock: inline
name: "Elananx"
level: 6
source: "Monster Core"
aon_id: "creature-2972"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2972"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elananx"
level: "Creature 6"
size: "Medium"
trait_01: "Fey"
trait_02: "Fire"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Fey; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Athletics +14, Survival +14"
abilityMods: [4, 4, 2, -3, 2, -2]
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +12; __Ref__: +16; __Will__: +12"
hp: 95
health:
  - name: "HP"
    desc: "95; __Immunities__ fire; __Weaknesses__ cold iron 5"
abilities_mid:
  - name: "Cinder Dispersal"
    desc: "⬲ (fire, primal)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Trigger"
    desc: "The elananx takes damage from a hostile source"
  - name: "Effect"
    desc: "The elananx disperses into a cloud of smoke and cinders, filling its space and a 20-foot emanation. While in this form, the elananx can't be attacked or targeted, and it doesn't take up space. Anything inside this cloud is concealed, and any creature ending its turn there takes 2d6 fire damage. At the start of its turn, the elananx returns to its normal form in any square the cloud covered. If the elananx Strikes a creature using its first action after returning to its normal form, the target is off-guard and the Strike deals an extra 1d6 fire damage."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +16 (Magical) __Damage__ 2d6+8 piercing and 1d6 fire"
  - name: "Melee"
    desc: "⬻ claw +16 (Agile) __Damage__ 2d6+8 slashing"
abilities_bot:
  - name: "Pack Attack"
    desc: "The elananx's Strikes deal an extra 1d6 damage to creatures within the reach of at least two of its allies."
  - name: "Pounce"
    desc: "⬻ The elananx Strides and makes a Strike at the end of that movement. If the elananx began this action hidden, it remains hidden until after the attack. Hunting Grounds Although many elananxes dwell in the strange realm of the First World, some are also natives of the Universe. Elananxes prefer to dwell in regions where there are ample intelligent creatures to chase, hunt, and eat, and they favor woodlands and hills as their primary hunting grounds."
sourcebook: "_Monster Core_, page 139."
```

```encounter-table
name: Elananx
creatures:
  - 1: Elananx
```
