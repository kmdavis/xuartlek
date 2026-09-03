---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sinswarm"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Sinswarm"
level: 9
source: "Battlecry!"
aon_id: "creature-3937"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3937"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Sinswarm"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Troop"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, sin scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], Thassilonian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [6, 3, 4, 1, 2, 1]
abilities_top:
  - name: "Sin Scent"
    desc: "A sinswarm can smell creatures reflecting any one of the seven primary sins as the scent ability. The GM determines which creatures are appropriately sinful."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +18; __Will__: +15"
hp: 150
health:
  - name: "HP"
    desc: "150 (4 segments); __Immunities__ controlled; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 10; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Reactive Attack"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] of the sinswarm uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]] action or a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action, makes a ranged attack, or leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The sinswarm lashes out at the triggering creature, dealing 2d8+9 piercing or slashing damage (DC 25 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). If the creature critically fails the save and the trigger was a manipulate action, that action is disrupted."
  - name: "Troop Defenses"
    desc: ""
speed: "30 feet; troop movement"
abilities_bot:
  - name: "Sinful Assault"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The sinswarm makes a coordinated attack against each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], with a DC 25 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 1d8+2 piercing or slashing damage ⬺ 2d8+9 piercing or slashing damage plus sinful bite ⬽ 3d8+11 piercing or slashing damage plus sinful bite"
  - name: "Sinful Bite"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) A creature bitten by a sinspawn must attempt a DC 28 Will save as it is assailed by sinful thoughts. The sinswarm can't inflict the same sin effect on multiple targets in the same round until it has inflicted all seven sins at least once."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
  - name: "Failure"
    desc: "The creature is sickened 2."
  - name: "Critical Failure"
    desc: "The creature is sickened 2 and takes one of the following additional effects, chosen by the GM: [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled]] 2 for 1 minute (envy), [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1 (gluttony), [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 for 1 minute (greed), [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 for 1 minute (lust), clumsy 1 and enfeebled 1 for 1 minute (pride), –10-foot status penalty to all Speeds for 1 minute (sloth), or drained 1 and enfeebled 1 for 1 minute (wrath)."
sourcebook: "_Battlecry!_, page 191."
```

```encounter-table
name: Sinswarm
creatures:
  - 1: Sinswarm
```
