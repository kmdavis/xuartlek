---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Champion Automaton"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/automaton
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Champion Automaton"
level: 10
source: "Monster Core 2"
aon_id: "creature-4092"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4092"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Champion Automaton"
level: "Creature 10"
size: "Large"
trait_01: "Automaton"
trait_02: "Construct"
trait_03: "Rare"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; one other language the champion knew in life (usually Jistkan); telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/lore|Warfare Lore]] +19"
abilityMods: [6, 5, 5, 3, 4, 4]
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +21; __Ref__: +19; __Will__: +17"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|bleed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 10 (except [[srd/pf2e/compendium/equipment/weapons/adamantine-weapon-high-grade|adamantine]])"
speed: "25 feet, climb 15 feet"
attacks:
  - name: "Melee"
    desc: "⬻ pincer +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d12+12 piercing plus Grab"
  - name: "Ranged"
    desc: "⬻ energy beam +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 60 feet) __Damage__ 2d10+10 fire"
abilities_bot:
  - name: "Arcane Slam"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]])"
  - name: "Requirements"
    desc: "The champion has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The champion channels supernatural energy through its pincers, then slams its foe against the ground. The grabbed creature takes 3d6 bludgeoning and 3d6 fire damage, is knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] and must attempt a DC 29 Fortitude save. On a failure the target is [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]] (enfeebled 2 on a critical failure) from the force of the slam. At the end of the Arcane Slam, the grapple ends."
  - name: "Spinning Toss"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The champion has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The champion spins on its axis, using the creature it's holding as an impromptu bludgeon before tossing it aside. The champion attempts an [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] check against the grabbed creature's Fortitude DC."
  - name: "Critical Success"
    desc: "The champion flings its victim. The grapple ends. The grabbed creature is thrown into a space within 10 feet, takes 8d6 bludgeoning damage, and falls [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. All creatures adjacent to the champion take the same amount of bludgeoning damage (DC 29 basic Reflex save)."
  - name: "Success"
    desc: "As critical success, except the grabbed creatures is thrown into a space within 5 feet, and creatures take 4d6 bludgeoning damage."
  - name: "Failure"
    desc: "The champion tosses its victim aside. The grapple ends. The grabbed creature falls prone."
  - name: "Critical Failure"
    desc: "The champion fumbles its grasp on its victim and the grapple ends."
sourcebook: "_Monster Core 2_, page 49."
```

```encounter-table
name: Champion Automaton
creatures:
  - 1: Champion Automaton
```
