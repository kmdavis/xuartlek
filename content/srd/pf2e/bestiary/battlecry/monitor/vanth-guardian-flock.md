---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vanth Guardian Flock"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Vanth Guardian Flock"
level: 13
source: "Battlecry!"
aon_id: "creature-3939"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3939"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Vanth Guardian Flock"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: "Troop"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, lifesense 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/lore|Boneyard Lore]] +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +24, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +22, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27"
abilityMods: [8, 5, 3, 3, 4, 3]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +21; __Will__: +25 +1 status to all saves vs. magic"
hp: 240
health:
  - name: "HP"
    desc: "240 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] 15; __Weaknesses__ area damage 12, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 12"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 20 feet, DC 30"
  - name: "Reactive Relocation"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]])"
  - name: "Trigger"
    desc: "A creature hits the guardian flock with an attack roll"
  - name: "Effect"
    desc: "After the attack roll is resolved, the troop pools dimensional magic to rapidly change their position. They cast 4th-rank [[srd/pf2e/compendium/spells/rank-4/translocate|_translocate_]], except their range is limited to 40 feet."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, fly 40 feet; troop movement"
abilities_bot:
  - name: "Guardians' Curse"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/misfortune|Misfortune]])"
  - name: "Frequency"
    desc: "three times per day; Effect The guardian flock bestows a curse upon all enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] by touching them with their scythes. Each affected creature must attempt a DC 33 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected and is temporarily immune to Guardians' Curse for 24 hours."
  - name: "Success"
    desc: "The target feels a momentary shudder of doom and is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 for 1 minute by the distracting sensation."
  - name: "Failure"
    desc: "The target becomes morose and glum as it accepts its own inevitable fate. For 1 hour, the target is stupefied 2. Each time the target gains the [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] condition, the stupefied condition value increases by 1, to a maximum value of stupefied 4."
  - name: "Critical Failure"
    desc: "As failure, but the effect is permanent."
  - name: "Harvest the Wicked"
    desc: ""
  - name: "Frequency"
    desc: "once per round; Effect The vanths swing their scythes in a coordinated melee attack. Each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must attempt a DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. The slashing damage is treated as adamantine, cold iron, and silver. ⬻ 1d10+1 slashing damage plus 1d6 shepherd's touch ⬺ 2d10+3 slashing damage plus 3d6 shepherd's touch ⬽ 2d10+7 slashing damage plus 4d6 shepherd's touch"
  - name: "Shepherd's Touch"
    desc: "The physical damage dealt by the guardian flock's Harvest the Wicked ability is treated as coming from a weapon with a [[srd/pf2e/compendium/equipment/runes/ghost-touch|ghost touch]] property rune. In addition, the vanths deal the listed damage as void damage to living creatures or [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] damage to [[srd/pf2e/compendium/rules-elements/traits/player-core/undead|undead]]."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __6th__ [[srd/pf2e/compendium/spells/rank-3/holy-light|Holy Light]] (×3), [[srd/pf2e/compendium/spells/rank-3/locate|Locate]] (×3), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
sourcebook: "_Battlecry!_, page 192."
```

```encounter-table
name: Vanth Guardian Flock
creatures:
  - 1: Vanth Guardian Flock
```
