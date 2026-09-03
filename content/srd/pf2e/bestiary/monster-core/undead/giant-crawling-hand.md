---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giant Crawling Hand"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Giant Crawling Hand"
level: 5
source: "Monster Core"
aon_id: "creature-2886"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2886"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giant Crawling Hand"
level: "Creature 5"
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; lifesense 30 feet, tremorsense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [4, 2, 4, -4, 3, 0]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +13; __Ref__: +11; __Will__: +10"
hp: 75
health:
  - name: "HP"
    desc: "75 (void healing); __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]"
abilities_mid:
  - name: "Pus Burst"
    desc: "⬲"
  - name: "Trigger"
    desc: "The giant crawling hand takes piercing or slashing damage"
  - name: "Effect"
    desc: "A random creature adjacent to the giant crawling hand is sprayed with vile pus that deals 4d6 void damage. The affected creature must attempt a DC 21 Reflex save."
  - name: "Critical Success"
    desc: "The creature takes no damage."
  - name: "Success"
    desc: "The creature takes half damage and becomes [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]."
  - name: "Failure"
    desc: "The creature takes full damage and becomes sickened 2."
  - name: "Critical Failure"
    desc: "The creature takes double damage and becomes sickened 3."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +15 __Damage__ 2d6+7 slashing plus Grab"
abilities_bot:
  - name: "Mark Quarry"
    desc: "A crawling hand can be assigned a quarry by anointing the hand with a drop of the intended quarry's blood. If the hand ever has no quarry, it automatically gains the next creature it damages as its quarry. The hand gains a +1 circumstance bonus to Perception checks when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seeks]] its quarry, to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks when it [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Tracks]] its quarry, and to damage rolls when it Strikes its quarry."
sourcebook: "_Monster Core_, page 68."
```

```encounter-table
name: Giant Crawling Hand
creatures:
  - 1: Giant Crawling Hand
```
