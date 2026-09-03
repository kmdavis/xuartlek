---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Xulgath Army"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/xulgath
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Xulgath Army"
level: 6
source: "Battlecry!"
aon_id: "creature-3944"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3944"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Xulgath Army"
level: "Creature 6"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Troop"
trait_03: "Xulgath"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13"
abilityMods: [5, 3, 3, 0, 1, 0]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +17; __Ref__: +14; __Will__: +11"
hp: 99
health:
  - name: "HP"
    desc: "99 (4 segments); __Weaknesses__ area damage 5, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 5"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 24"
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Club Offensive"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The xulgaths make coordinated melee attacks against each enemy in 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]], with a DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage dealt depends on the number of actions. ⬻ 1d6+1 bludgeoning damage ⬺ 2d6+7 bludgeoning damage ⬽ 2d6+12 bludgeoning damage"
  - name: "Javelin Barrage"
    desc: "⬺ The xulgaths draw javelins and launch a coordinated barrage at range. This barrage is a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] within 30 feet that deals 3d6 piercing damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). When the xulgath army is reduced to 2 segments, this area decreases to a 5-foot burst."
  - name: "Rend Flesh"
    desc: "⬺ The xulgaths concentrate their attacks on a single adjacent enemy, clawing and biting with abandon. That creature takes 3d4+5 slashing damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). On a failed save, the creature also takes 1d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]."
sourcebook: "_Battlecry!_, page 194."
```

```encounter-table
name: Xulgath Army
creatures:
  - 1: Xulgath Army
```
