---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sweet Hag"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Sweet Hag"
level: 4
source: "Monster Core"
aon_id: "creature-3041"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3041"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sweet Hag"
level: "Creature 4"
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "Aklo, Common, Fey, Jotun; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +9, Athletics +11, Deception +10, Nature +8, Occultism +8, Stealth +9"
abilityMods: [5, 3, 3, 2, 2, 4]
abilities_top:
  - name: "Coven"
    desc: "A sweet hag adds _charm_, _honeyed words_, and _outcast's curse_ to their coven's spells."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +11; __Will__: +12 +1 status to all saves vs. magic"
hp: 70
health:
  - name: "HP"
    desc: "70; __Weaknesses__ cold iron 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ candy cane claw +14 (Agile, Magical) __Damage__ 1d10+5 piercing plus soporific touch"
abilities_bot:
  - name: "Betraying Touch"
    desc: "⬻ The sweet hag touches a creature that doesn't realize the hag is an enemy. The betrayed creature is affected by soporific strike with a –4 circumstance penalty to their saving throw."
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Occult, Polymorph) The sweet hag can take on the appearance of any Medium humanoid woman. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Poisoned Candy"
    desc: "⬺ (Occult) The sweet hag casts an innate spell that can normally target 1 creature on a piece of food, typically a sweet treat. The spell is stored in the food. The first creature that eats any of the food is affected by the spell and takes a –4 circumstance penalty to their saving throw against that effect."
  - name: "Soporific Touch"
    desc: "(Incapacitation, Occult) A creature damaged by a sweet hag's claw must succeed at a DC 20 Fortitude save or be enfeebled 1 for 1 day. If the creature critically fails or fails this save while already enfeebled by soporific strike, it falls unconscious and dreams of eating delicious sweets; this is a mental sleep effect. If not woken up before 1 minute passes, the creature wakes up automatically."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 20, attack +14 - __Cantrips (2nd)__ Daze, Figment, Light, Message - __1st__ Charm (at will), Cleanse Cuisine (at will), Spider Sting - __2nd__ Create Food (sweets only), Invisibility (at will), Laughing Fit, Shrink, Sleep - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 189."
```

```encounter-table
name: Sweet Hag
creatures:
  - 1: Sweet Hag
```
