---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Iron Hag"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Iron Hag"
level: 6
source: "Monster Core"
aon_id: "creature-3042"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3042"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Iron Hag"
level: "Creature 6"
size: "Large"
trait_01: "Hag"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "Aklo, Common, Jotun"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Athletics +14, Deception +13, Diplomacy +11, Intimidation +13, Stealth +16"
abilityMods: [6, 4, 4, 1, 4, 3]
abilities_top:
  - name: "Coven"
    desc: "An iron hag adds _earthbind_, _impaling spike_, and _spellwrack_ to their coven's spells. Their spell DC when leading a coven is 24."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +12; __Will__: +14 +1 status to all saves vs. magic"
hp: 80
health:
  - name: "HP"
    desc: "80; __Resistances__ physical 3 (except adamantine)"
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, cold iron, Magical, reach 10 feet) __Damage__ 2d8+6 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ jaws +16 (cold iron, Magical) __Damage__ 2d6+6 piercing"
abilities_bot:
  - name: "Bonds of Iron"
    desc: "⬺ (Attack, Occult)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The hag causes a cage built of cold iron fingernails to spring out of nothingness around one creature within 30 feet, attempting an Athletics check to Grapple against the target's Fortitude DC; if the target has a weakness to cold iron, the iron hag gains a +2 circumstance bonus to this check. On a success, the creature is grabbed by the magical fingernails (or restrained on a critical success). If the creature successfully Escapes (DC 24), the cage crumbles into rust. Any creature can attempt to destroy the cage by attacking it. It has an AC of 19, Hardness 10, and 40 Hit Points."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Occult, Polymorph) The iron hag can take on the appearance of any Medium female humanoid. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Embrace of Iron"
    desc: "⬻"
  - name: "Requirements"
    desc: "A creature is grabbed or restrained by the iron hag's claw"
  - name: "Effect"
    desc: "The hag's nails tear into their captured victim, dealing 2d8 piercing damage (the nails are cold iron). Then the hag can attempt to Reposition the creature. If the creature is adjacent to the hag, they can then attempt a jaws Strike against it."
sourcebook: "_Monster Core_, page 190."
```

```encounter-table
name: Iron Hag
creatures:
  - 1: Iron Hag
```
