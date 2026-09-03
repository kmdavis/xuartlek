---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elven Court Guard"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Elven Court Guard"
level: 13
source: "NPC Core"
aon_id: "creature-3634"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3634"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Elven Court Guard"
level: "Creature 13"
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; plus vigilance"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; plus one regional language"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +26, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +24, [[srd/pf2e/compendium/rules-elements/skills/lore|Heraldry Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +19"
abilityMods: [4, 5, 2, 2, 3, 1]
abilities_top:
  - name: "Vigilance"
    desc: "A court guard gains a +1 circumstance bonus on Perception checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] and [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] creatures, and if they succeed, they get a critical success instead."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Chain Shirt|chain shirt]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] low-grade cold iron [[srd/pf2e/compendium/equipment/weapons/sword/elven-curve-blade|elven curve blade]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/bow/composite-longbow|composite longbow]]_"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +20; __Ref__: +27; __Will__: +23 +1 status vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] effects"
hp: 225
health:
  - name: "HP"
    desc: "225"
abilities_mid:
  - name: "Interposition"
    desc: "⬲"
  - name: "Trigger"
    desc: "An ally within 15 feet of the guard would take damage"
  - name: "Effect"
    desc: "The guard Strides. This movement does not trigger reactions, and the guard must end the Stride in a space adjacent to the ally. The guard then switches places with the ally, taking all damage and associated effects instead of the ally."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _elven curve blade_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d8+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _composite longbow_ +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/volley|volley 30 feet]]) __Damage__ 2d8+10 piercing"
abilities_bot:
  - name: "Avenge the Fallen"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fortune|Fortune]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The guard is within 30 feet of the creature they were guarding, and that creature is either [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] or died since the guard's last turn"
  - name: "Effect"
    desc: "The guard Strikes the creature that damaged their ally. They roll the attack roll twice and use the higher result."
  - name: "Dancing Blade"
    desc: "⬺ The guard makes a Strike against a creature, then Strides. This Stride doesn't trigger reactions. If the guard ends this Stride in a different space adjacent to the same creature, they make another Strike against it. If both Strikes succeed, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] until the start of the guard's next turn. Each attack counts toward the guard's multiple attack penalty, but the penalty doesn't increase until they've made both attacks."
sourcebook: "_NPC Core_, page 180."
```

```encounter-table
name: Elven Court Guard
creatures:
  - 1: Elven Court Guard
```
