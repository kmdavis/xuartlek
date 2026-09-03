---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Comozant Wyrd"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/small
statblock: inline
name: "Comozant Wyrd"
level: 5
source: "Rage of Elements"
aon_id: "creature-2616"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2616"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Comozant Wyrd"
level: "Creature 5"
size: "Small"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Incorporeal"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "Sussuran"
skills:
  - name: "Skills"
    desc: "Diplomacy +11, Nature +12"
abilityMods: [-5, 4, 0, -1, 3, 4]
abilities_top:
  - name: "Plasmatic Form"
    desc: "Unlike other incorporeal creatures, a comozant wyrd can't move into or through solid objects. If a comozant wyrd isn't adjacent to a solid object or surface of its size or larger at the end of its turn, it loses 10 HP. This HP loss cannot be mitigated or avoided in any way."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +7; __Ref__: +15; __Will__: +12"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ disease, electricity, paralyzed, poison, precision; __Resistances__ all damage 5 (except force or _ghost touch_; double resistance vs. non-magical)"
abilities_mid:
  - name: "Illuminating Flames"
    desc: "(aura, electricity, light, primal) 30 feet. The comozant wyrd sheds bright light in the emanation and dim light for another 30 feet. Heatless flames similar to the wyrd's own surround any creature in the emanation. A visible creature can't become concealed while in the emanation, and an invisible creature becomes concealed rather than undetected. The wyrd can communicate empathically with any non-mindless creature affected by illuminating flames, even if they don't share a language."
speed: "15 feet, fly 25 feet"
attacks:
  - name: "Ranged"
    desc: "⬻ lightning lash +15 (Electricity, range 30 feet) __Damage__ 2d12 electricity"
abilities_bot:
  - name: "Leap the Gap"
    desc: "⬺"
  - name: "Requirements"
    desc: "The comozant wyrd is adjacent to a solid object or surface of its size or larger"
  - name: "Effect"
    desc: "The wyrd Flies up to its Speed in a straight line, ending its movement adjacent to a different solid object or surface of its size or larger; this movement doesn't trigger reactions. The wyrd can move through other creatures during this movement, and all creatures it moves through take 2d12 electricity damage with a DC 22 basic Reflex save."
  - name: "Wyrd Wisdom"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The comozant wyrd is communicating empathically with another creature through illuminating flames"
  - name: "Effect"
    desc: "The comozant wyrd's odd means of communication brings strange insight. One creature the wyrd is empathically conversing with gains the benefits of an _augury_ spell, though only about this conversation topic, rather than any topic of the creature's choice. Comozant Communication Creatures of emotion and instinct, comozant wyrds use simple images and concepts to convey deep and layered meanings. They're quite insightful, able to leap to solid conclusions as rapidly as they leap across solid surfaces. Most who “converse” with a comozant wyrd find the process enlightening, but have little desire make it a regular experience."
sourcebook: "_Rage of Elements_, page 81."
```

```encounter-table
name: Comozant Wyrd
creatures:
  - 1: Comozant Wyrd
```
