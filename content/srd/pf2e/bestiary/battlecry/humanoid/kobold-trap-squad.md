---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kobold Trap Squad"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/kobold
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Kobold Trap Squad"
level: 4
source: "Battlecry!"
aon_id: "creature-3924"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3924"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Kobold Trap Squad"
level: "Creature 4"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: "Troop"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +10, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [1, 4, 0, 0, 2, 2]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +8; __Ref__: +14; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60 (4 segments); __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Group Scamper"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The kobolds Stride up to their Speed plus 5 feet and gain a +2 circumstance bonus to AC against reactions triggered by this movement. If they end this movement with at least 1 segment adjacent to any enemy, the squad is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the beginning of its next turn."
  - name: "Hasty Traps"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]]) The kobolds hastily prepare a handful of rudimentary traps in their vicinity until the beginning of their next turn. The next creature who moves adjacent to the trap squad triggers a trap and must attempt a DC 18 Reflex save. On a failure, the creature takes 1d4 persistent bleed damage (2d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] on a critical failure). A creature taking persistent bleed damage from Hasty Traps takes a –5-foot enhancement penalty to its Speed. This occurs to as many creatures as the kobold trap squad has segments when it performed the action, but a single creature can trigger only one trap per turn."
  - name: "Sling Barrage"
    desc: "⬺ The kobolds draw their slings, then launch a ranged barrage of stones. This barrage is a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 50 feet that deals 3d4 bludgeoning damage with a DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. When the squad is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Spear Jabs"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The kobold trap squad engages in a coordinated melee attack against all enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], with a DC 18 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 1d6 piercing damage ⬺ 2d6+4 piercing damage ⬽ 2d6+7 piercing damage"
sourcebook: "_Battlecry!_, page 184."
```

```encounter-table
name: Kobold Trap Squad
creatures:
  - 1: Kobold Trap Squad
```
