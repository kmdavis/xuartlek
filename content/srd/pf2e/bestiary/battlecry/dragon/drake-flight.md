---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drake Flight"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Drake Flight"
level: 13
source: "Battlecry!"
aon_id: "creature-3911"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3911"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "BC"
name: "Drake Flight"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Troop"
trait_03: "Uncommon"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +24, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +24"
abilityMods: [8, 5, 4, -2, 2, 1]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +23; __Will__: +20"
hp: 240
health:
  - name: "HP"
    desc: "240 (4 segments); __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 5; __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage 10"
abilities_mid:
  - name: "Tail Lashes"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within 10 feet of the drake flight uses an action to Strike or attempt a skill check"
  - name: "Effect"
    desc: "The drakes lash out with their tails, dealing 3d8+10 bludgeoning damage (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). If the triggering creature fails the save, they also take a –2 circumstance penalty to the triggering roll."
  - name: "Troop Defenses"
    desc: ""
speed: "20 feet, fly 50 feet; troop movement"
abilities_bot:
  - name: "Draconic Onslaught"
    desc: "The drakes frenzy, lashing out with fangs and tails. Each enemy in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] attempts a DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save. The damage depends on the number of actions. ⬻ 2d8 piercing or bludgeoning damage ⬺ 3d8+10 piercing or bludgeoning damage ⬽ 4d8+14 piercing or bludgeoning damage"
  - name: "Drake Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) Certain drakes within the flight bring their breath weapon (or similar ability) to bear, exhaling energy that explodes in a 15-foot burst within 120 feet. This explosion deals 5d6 acid, cold, fire, or poison damage; the ability gains the corresponding trait. The drake flight can't choose the same damage type until it uses this ability with a different damage type. When the drakes are reduced to 2 segments, this area decreases to a 10-foot burst."
  - name: "Speed Surge"
    desc: "⬻"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The drake flight Strides or Flies twice."
sourcebook: "_Battlecry!_, page 178."
```

```encounter-table
name: Drake Flight
creatures:
  - 1: Drake Flight
```
