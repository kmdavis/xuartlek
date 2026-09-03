---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Dromaar Company"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/dromaar
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/orc
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
  - pf2e/creature/trait/half-orc
statblock: inline
name: "Dromaar Company"
level: 6
source: "Battlecry!"
aon_id: "creature-3912"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3912"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Dromaar Company"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Dromaar"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Orc"
trait_05: "Troop"
trait_06: "Half-Orc"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Orcish|Orcish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11"
abilityMods: [5, 4, 2, 0, 2, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +17; __Will__: +11"
hp: 90
health:
  - name: "HP"
    desc: "90 (4 segments); __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
abilities_mid:
  - name: "Ferocious Fall"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dromaar company is about to lose a segment due to passing a Hit Point threshold"
  - name: "Effect"
    desc: "The dying dromaar mercenaries lash out as they fall. Each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] takes 1d8 slashing damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save); this occurs before the troop loses a segment."
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Bola Hurl"
    desc: "⬺ The dromaars draw bolas and toss them in a 15-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Cone|cone]]. Each creature in this area takes 3d6 nonlethal bludgeoning damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). A creature who fails this saving throw is also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Charge the Fallen"
    desc: "⬺ The dromaar company Strides up to twice, sweeping with their axes. They deal 2d8+5 slashing damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save) to each enemy in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] at the end of their movement. This damage increases by 5 if the target is [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]."
  - name: "Disciplined Strikes"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dromaars coordinate melee attacks with their axes against all enemies in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The damage depends on the number of actions. ⬻ 1d8 slashing damage ⬺ 2d8+5 slashing damage ⬽ 2d8+10 slashing damage"
sourcebook: "_Battlecry!_, page 178."
```

```encounter-table
name: Dromaar Company
creatures:
  - 1: Dromaar Company
```
