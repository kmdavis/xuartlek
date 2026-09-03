---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Crawling Hand"
tags:
  - pf2e/creature/level/-1
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Crawling Hand"
level: -1
source: "Monster Core"
aon_id: "creature-2885"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2885"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Crawling Hand"
level: "Creature -1"
size: "Tiny"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5; lifesense 30 feet, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +2"
abilityMods: [1, 3, 0, -4, 0, 0]
ac: 12
armorclass:
  - name: "AC"
    desc: "12; __Fort__: +2; __Ref__: +5; __Will__: +2"
hp: 8
health:
  - name: "HP"
    desc: "8 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
speed: "30 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]]) __Damage__ 1d4+1 slashing plus Throat Grab"
abilities_bot:
  - name: "Mark Quarry"
    desc: "A crawling hand can be assigned a quarry by anointing the hand with a drop of the intended quarry's blood. If the hand ever has no quarry, it automatically gains the next creature it damages as its quarry. The hand gains a +1 circumstance bonus to Perception checks when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeks]] its quarry, to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Tracks]] its quarry, and to damage rolls when it Strikes its quarry."
  - name: "Throat Grab"
    desc: "⬻ This ability functions as Grab, but the crawling hand grips the throat of a Medium or smaller creature. A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] this way has difficulty speaking and must spend an extra action to perform any action that requires speaking, including casting spells."
sourcebook: "_Monster Core_, page 68."
```

```encounter-table
name: Crawling Hand
creatures:
  - 1: Crawling Hand
```
