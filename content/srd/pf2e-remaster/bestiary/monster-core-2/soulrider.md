---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Soulrider"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/soulrider
  - pf2e/creature/trait/tiny
statblock: inline
name: "Soulrider"
level: -1
source: "Monster Core 2"
aon_id: "creature-4557"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4557"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Soulrider"
level: "Creature -1"
size: "Tiny"
trait_01: "Aberration"
trait_02: "Soulrider"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +4, Stealth +4"
abilityMods: [0, 3, 2, -3, 2, -1]
abilities_top:
  - name: "Planar Adaptation"
    desc: "If the soulrider has followed a soul to its final destination, it takes on traits appropriate to that plane. These soulriders gain the celestial and holy, fiend and unholy, or monitor traits as appropriate to the destination."
ac: 14
armorclass:
  - name: "AC"
    desc: "14; __Fort__: +5; __Ref__: +8; __Will__: +2"
hp: 8
health:
  - name: "HP"
    desc: "8; __Weaknesses__ spirit 1"
speed: "20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sucker +6 (Finesse, reach 0 feet, magical) __Damage__ soul attach"
  - name: "Melee"
    desc: "⬻ tail +6 (Agile, finesse, reach 0 feet, sanctified) __Damage__ 1d4 bludgeoning plus 1 spirit"
abilities_bot:
  - name: "Propulsive Launch"
    desc: "⬺ The soulrider Leaps up to 40 feet, then makes a sucker Strike. If it's in the air and not attached to a creature after the Strike, it falls."
  - name: "Soul Attach"
    desc: "(Spirit) When a soulrider succeeds at a sucker Strike against a target with a soul capable of facing judgment, its sucker attaches it to that soul. While attached, both the soulrider and the host creature are off-guard, and the soulrider moves with its host until the soulrider dies or the host pulls it loose (Escape DC 15). If the host dies while the soulrider is attached, the soulrider disappears immediately to follow the soul leaving the body. A creature returned to life before reaching its final destination generally returns with any attached soulrider."
  - name: "Tail Thrash"
    desc: "⬺"
  - name: "Requirements"
    desc: "The soulrider is attached to a creature's soul"
  - name: "Effect"
    desc: "The soulrider makes a tail Strike against the creature whose soul it's attached to, then one against another creature adjacent to the original target. These Strikes count towards the soulrider's multiple attack penalty, but it doesn't increase until after the second attack."
sourcebook: "_Monster Core 2_, page 296."
```

```encounter-table
name: Soulrider
creatures:
  - 1: Soulrider
```
