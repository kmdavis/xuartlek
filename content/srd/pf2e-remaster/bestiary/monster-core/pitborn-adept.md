---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pitborn Adept"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/nephilim
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Pitborn Adept"
level: 3
source: "Monster Core"
aon_id: "creature-3140"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3140"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pitborn Adept"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Nephilim"
trait_04: "Uncommon"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Chthonian, Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Arcana +9, Deception +9, Intimidation +7, Occultism +9, Outer Rifts Lore +9, Religion +6, Society +9, Stealth +7"
abilityMods: [0, 2, 0, 4, 1, 2]
abilities_top:
  - name: "Items"
    desc: "Explorer's Clothing, spellbook, Staff"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +5; __Ref__: +7; __Will__: +8"
hp: 29
health:
  - name: "HP"
    desc: "29"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +6 (two-handed 1d8) __Damage__ 1d6 bludgeoning"
abilities_bot:
  - name: "Drain Bonded Item"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The adept hasn't acted yet on this turn"
  - name: "Effect"
    desc: "The adept expends the power stored in its staff. This gives the adept the ability to cast one prepared spell it had already previously cast today (choosing a different spell rank each time), without spending a spell slot. The adept must still Cast the Spell and meet the spell's other requirements."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 21, attack +11 - __Cantrips (2nd)__ Detect Magic, Shield, Tangle Vine, Telekinetic Hand, Void Warp - __1st__ Charm, Enfeeble, Force Barrage - __2nd__ Floating Flame, Invisibility"
  - name: "Divine Innate Spells"
    desc: "DC 17 - __2nd__ Darkness"
sourcebook: "_Monster Core_, page 266."
```

```encounter-table
name: Pitborn Adept
creatures:
  - 1: Pitborn Adept
```
