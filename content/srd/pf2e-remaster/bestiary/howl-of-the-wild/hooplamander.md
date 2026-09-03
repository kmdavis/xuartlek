---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hooplamander"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Hooplamander"
level: 5
source: "Howl of the Wild"
aon_id: "creature-3292"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3292"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Hooplamander"
level: "Creature 5"
size: "Large"
trait_01: "Beast"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +12, Stealth +10"
abilityMods: [5, 5, 3, -2, 0, 2]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +12; __Ref__: +15; __Will__: +9"
hp: 78
health:
  - name: "HP"
    desc: "78"
abilities_mid:
  - name: "Flexible Dodge"
    desc: "⬲"
  - name: "Requirements"
    desc: "The hooplamander is Unfurled"
  - name: "Trigger"
    desc: "The hooplamander is targeted by a Strike"
  - name: "Effect"
    desc: "The hooplamander gains a +2 circumstance bonus to AC against the triggering attack and enters its Wheels Up stance."
speed: "25 feet (40 feet in Wheels Up)"
attacks:
  - name: "Melee"
    desc: "⬻ hookclaw +13 (Agile, versatile P) __Damage__ 1d4+5 slashing plus 3d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ ridged tail +13 (Sweep) __Damage__ 2d6+5 bludgeoning"
abilities_bot:
  - name: "Wheels Up"
    desc: "⬻ (Stance)"
  - name: "Requirements"
    desc: "The hooplamander is Unfurled"
  - name: "Effect"
    desc: "The hooplamander Leaps and then rolls into its wheeled form. Any creature within 5 feet must succeed at a DC 22 Reflex save or be off-guard for one round. While it's Wheels Up, the hooplamander can't make Strikes and its Speed increases to 40 feet."
  - name: "Rollout Trample"
    desc: "⬽"
  - name: "Requirements"
    desc: "The hooplamander is Wheels Up"
  - name: "Effect"
    desc: "As Trample (Large or smaller, ridged tail, DC 22), except targets that critically fail their Reflex save are stunned 1, and the hooplamander Unfurls at the end of its movement."
  - name: "Unfurl"
    desc: "⬻"
  - name: "Requirements"
    desc: "The hooplamander is Wheels Up"
  - name: "Effect"
    desc: "The hooplamander releases its tail, Leaping up to 20 feet as it exists its wheeled shape and unfurls to land on its four legs."
sourcebook: "_Howl of the Wild_, page 161."
```

```encounter-table
name: Hooplamander
creatures:
  - 1: Hooplamander
```
