---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Homunculus"
tags:
  - pf2e/creature/level/0
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/tiny
statblock: inline
name: "Homunculus"
level: 0
source: "Monster Core"
aon_id: "creature-3056"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3056"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Homunculus"
level: "Creature 0"
size: "Tiny"
trait_01: "Construct"
modifier: 3
perception:
  - name: "Perception"
    desc: "Perception +3; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language); master link"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +5"
abilityMods: [-1, 3, 0, 0, 1, -2]
abilities_top:
  - name: "Master Link"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) A homunculus can't speak, but it is telepathically linked to its creator. It can share information back and forth, including its master's knowledge and everything the homunculus hears. The range of this link is 1,500 feet. The homunculus typically has a similar attitude to its creator and is utterly faithful. If the homunculus is destroyed, the master takes 2d10 mental damage. If the master is slain, the homunculus becomes [[srd/pf2e/compendium/rules-elements/traits/player-core/mindless|mindless]], claims its current location as its lair, and instinctively attacks anyone who comes near."
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +2; __Ref__: +7; __Will__: +3"
hp: 17
health:
  - name: "HP"
    desc: "17; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]"
speed: "15 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d4 piercing plus homunculus poison"
abilities_bot:
  - name: "Homunculus Poison"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) A homunculus has one dose of poison in a reservoir in its head. It can refill this poison from its reserves with an Interact action"
  - name: "Saving Throw"
    desc: "DC 15 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison and [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (1 round). Soulbound Homunculi Most homunculi use a dose of their creator's blood as their spark of life, but it's possible to use a technique similar to that used in the crafting of a soulbound doll to give a homunculus a personality and the semblance of life. These homunculi gain the [[srd/pf2e/compendium/rules-elements/traits/monster-core/soulbound|soulbound]] trait, lose immunity to [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], can speak, and do not have a special link to a creator, yet the process tends to warp the soul used so that, more often than not, what rises in the new homunculus body is a parody of its prior life. As such, soulbound homunculi are generally created by cruel spellcasters as a method of humiliating and tormenting vanquished enemies."
sourcebook: "_Monster Core_, page 200."
```

```encounter-table
name: Homunculus
creatures:
  - 1: Homunculus
```
