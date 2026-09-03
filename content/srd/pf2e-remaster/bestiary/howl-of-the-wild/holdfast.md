---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Holdfast"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/small
statblock: inline
name: "Holdfast"
level: 4
source: "Howl of the Wild"
aon_id: "creature-3291"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3291"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Holdfast"
level: "Creature 4"
size: "Small"
trait_01: "Animal"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; low-light vision, scent (imprecise) 30 feet, tremorsense (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +10, Athletics +11, Stealth +12"
abilityMods: [5, 4, 3, -4, 2, 0]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +12; __Will__: +8"
hp: 55
health:
  - name: "HP"
    desc: "55"
abilities_mid:
  - name: "Lithe"
    desc: "A holdfast treats any tight space it can barely fit its head in or wider as difficult terrain and doesn't need to Squeeze to move through it."
  - name: "Hold Tight"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature grabbed by the holdfast's jaws takes damage from another creature's Strike"
  - name: "Effect"
    desc: "The holdfast Constricts the creature in its jaws."
speed: "30 feet, burrow 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +13 __Damage__ 2d6+5 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ talon +13 (Agile) __Damage__ 2d4+5 slashing"
abilities_bot:
  - name: "Burst from Below"
    desc: "⬻ The holdfast Burrows and then Strikes. If the holdfast began this movement hidden, it remains hidden until after this ability's Strike."
  - name: "Constrict"
    desc: "⬻ 2d6+2 piercing plus crush throat, DC 21"
  - name: "Crush Throat"
    desc: "When a creature fails a save against the holdfast's Constrict, the creature's throat is held tight, stopping them from speaking as long as they're grabbed. This prevents the creature from casting spells with vocal incantations, as well as from using many sonic or auditory abilities."
sourcebook: "_Howl of the Wild_, page 160."
```

```encounter-table
name: Holdfast
creatures:
  - 1: Holdfast
```
