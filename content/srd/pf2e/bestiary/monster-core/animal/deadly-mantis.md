---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deadly Mantis"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Deadly Mantis"
level: 11
source: "Monster Core"
aon_id: "creature-3095"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3095"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Deadly Mantis"
level: "Creature 11"
size: "Gargantuan"
trait_01: "Animal"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22"
abilityMods: [8, 3, 5, -5, 3, -2]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +24; __Ref__: +20; __Will__: +18"
hp: 220
health:
  - name: "HP"
    desc: "220"
speed: "50 feet, climb 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+14 piercing"
  - name: "Melee"
    desc: "⬻ leg +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d10+14 piercing plus Grab"
abilities_bot:
  - name: "Fling"
    desc: "⬻ The deadly mantis flings a [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] creature into the air, up to 30 feet overhead and up to 30 feet away from the mantis (the creature takes damage from the fall as normal). If the flung creature lands on another creature, the creature it lands on takes the same amount of bludgeoning damage with a DC 31 basic Reflex save."
  - name: "Leaping Grab"
    desc: "⬺ The mantis Leaps up to 40 feet vertically and 20 feet horizontally. At any point during the jump, it can make a leg Strike. If it hits, it automatically Grabs the target, bringing the creature along until the end of the jump."
  - name: "Rending Mandibles"
    desc: "⬻ The mantis makes a mandibles Strike against a creature it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]. If that Strike hits and the creature is wearing armor with Hardness 12 or lower, the armor is [[srd/pf2e/compendium/rules-elements/conditions#Broken|broken]]. This Strike doesn't further damage armor that's already broken."
  - name: "Sudden Strike"
    desc: "On the first round of combat, creatures that haven't acted are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the deadly mantis. Sacred Insects Deadly mantises are sacrosanct to followers of Achaekek, the Mantis God. His adherents, including the infamous Red Mantis assassins, invite or lure deadly mantises close to their settlements, seeing the towering creatures as a sign of their god's favor. Achaekek's followers offer sacrifices of livestock or captured enemies to keep the massive insects well fed. Clerics of Achaekek defend a deadly mantis's territory as if it were their own, believing it to be holy ground."
sourcebook: "_Monster Core_, page 229."
```

```encounter-table
name: Deadly Mantis
creatures:
  - 1: Deadly Mantis
```
