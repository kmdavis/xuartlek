---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adlet"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Adlet"
level: 9
source: "Monster Core 2"
aon_id: "creature-4011"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4011"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adlet"
level: "Creature 9"
size: "Medium"
trait_01: "Cold"
trait_02: "Humanoid"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; low-light vision, scent (imprecise) 30 feet"
languages: "Adlet, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Athletics +21, Stealth +20, Survival +18"
abilityMods: [5, 6, 4, 0, 4, 0]
abilities_top:
  - name: "Items"
    desc: "_+1 striking spear_ (2)"
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +20; __Ref__: +22; __Will__: +16"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ cold; __Weaknesses__ fire 10"
abilities_mid:
  - name: "Wolfstorm"
    desc: "(aura, cold, primal) 60 feet. A clammy, frigid mist billows forth ahead of the adlet. Creatures within the mist become concealed, and creatures outside the mist become concealed to creatures within it. An adlet can see through the aura without penalty."
  - name: "Avenging Bite"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of an adlet's jaws Strike attacks one of the adlet's allies"
  - name: "Effect"
    desc: "The adlet makes a jaws Strike against the triggering creature."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spear_ +20 (Magical) __Damage__ 2d6+9 piercing plus 1d6 cold"
  - name: "Melee"
    desc: "⬻ jaws +19 __Damage__ 2d8+9 piercing plus 1d6 cold"
  - name: "Ranged"
    desc: "⬻ spear +21 (Magical, thrown 20 feet) __Damage__ 2d6+9 piercing plus 1d6 cold"
abilities_bot:
  - name: "Frozen Weapons"
    desc: "(Primal) Weapons wielded by an adlet gain the effect of the _frost_ property rune."
  - name: "Pack Attack"
    desc: "An adlet's Strikes deal an additional 2d6 damage to creatures that are within the reach of at least two of the adlet's allies."
  - name: "Wolfrime"
    desc: "⬻ (Cold, concentrate, primal) An adlet's mist turns biting cold and coalesces into a thick rime of frost that deals 6d6 cold damage to creatures inside the adlet's wolfstorm aura (DC 26 basic Fortitude), and the aura is deactivated until the start of the adlet's next turn. Lost Cousins Legends about adlets’ origins suggest they might have fox-like kin. Some believe these kin are kitsune, while others point to the more powerful vulpinals as more likely progenitors."
sourcebook: "_Monster Core 2_, page 9."
```

```encounter-table
name: Adlet
creatures:
  - 1: Adlet
```
