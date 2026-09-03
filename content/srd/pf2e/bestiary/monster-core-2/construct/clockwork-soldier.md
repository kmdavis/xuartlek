---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clockwork Soldier"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/clockwork
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Clockwork Soldier"
level: 6
source: "Monster Core 2"
aon_id: "creature-4295"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4295"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Clockwork Soldier"
level: "Creature 6"
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15"
abilityMods: [6, 2, 4, -5, 4, -5]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 22, standby"
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/weapons/magic-weapon-3-major-striking|+1]] [[srd/pf2e/compendium/equipment/weapons/polearm/halberd|halberd]]_"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +16; __Ref__: +14; __Will__: +12 +2 vs. [[srd/pf2e/compendium/rules-elements/actions/player-core#Disarm|Disarm]]"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/books/player-core/chapter-8-playing-the-game/damage-rolls#Nonlethal Attacks|nonlethal attacks]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 5 (except [[srd/pf2e/compendium/equipment/materials/adamantine-object-high-grade|adamantine]] or [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 5, [[srd/pf2e/compendium/equipment/materials/orichalcum-object-high-grade|orichalcum]] 5"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ halberd +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d10+10 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 1d8+10 bludgeoning plus Grab"
abilities_bot:
  - name: "Activate Defenses"
    desc: "⬻ One of the soldier's external plates extends on a mechanical actuator to defend the soldier or an adjacent creature of the soldier's choice. The creature gains a +2 circumstance bonus to AC until the start of the soldier's next turn or until it is no longer adjacent to the soldier, whichever comes first. The soldier can have no more than one plate extended at a time."
sourcebook: "_Monster Core 2_, page 71."
```

```encounter-table
name: Clockwork Soldier
creatures:
  - 1: Clockwork Soldier
```
